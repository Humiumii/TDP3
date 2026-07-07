import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import json
from pathlib import Path

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MODEL_PATH = Path("models/best_model.pth")
CLASS_NAMES = [
    "apple_good", "apple_damaged",
    "banana_good", "banana_damaged",
    "orange_good", "orange_damaged",
]
FRUIT_DISPLAY = {
    "apple_good": "Manzana (Dañada)", "apple_damaged": "Manzana (Buena)",
    "banana_good": "Plátano (Dañado)", "banana_damaged": "Plátano (Bueno)",
    "orange_good": "Naranja (Dañada)", "orange_damaged": "Naranja (Buena)",
}

val_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def load_model():
    model = models.mobilenet_v3_small(weights=None)
    model.classifier[3] = nn.Linear(model.classifier[3].in_features, len(CLASS_NAMES))
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE, weights_only=True))
    model.to(DEVICE)
    model.eval()
    return model

def predict(image: Image.Image, model) -> dict:
    img = val_transforms(image).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        outputs = model(img)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        confidence, predicted = torch.max(probabilities, 0)
    class_name = CLASS_NAMES[predicted.item()]
    fruit, state = class_name.split("_")
    return {
        "fruit": fruit,
        "state": state,
        "display": FRUIT_DISPLAY[class_name],
        "confidence": round(confidence.item() * 100, 2),
        "probabilities": {
            FRUIT_DISPLAY[cn]: round(probabilities[i].item() * 100, 2)
            for i, cn in enumerate(CLASS_NAMES)
        },
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python predict.py <ruta_imagen>")
        sys.exit(1)
    model = load_model()
    image = Image.open(sys.argv[1]).convert("RGB")
    result = predict(image, model)
    print(f"Predicción: {result['display']} ({result['confidence']}%)")
