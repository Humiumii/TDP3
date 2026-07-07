import streamlit as st
from PIL import Image
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from predict import load_model, predict

MODEL_PATH = Path("models/best_model.pth")

st.set_page_config(
    page_title="Clasificador de Frutas",
    layout="centered",
)

st.title("Clasificador de Calidad de Frutas")
st.markdown("Sube una foto de una **manzana, plátano o naranja** y te diré si está **buena o dañada**.")

@st.cache_resource
def get_model():
    if not MODEL_PATH.exists():
        return None
    return load_model()

model = get_model()

if model is None:
    st.warning("Modelo no encontrado. Entrena el modelo primero con `python src/train.py`")
    st.stop()

uploaded_file = st.file_uploader(
    "Selecciona una imagen",
    type=["jpg", "jpeg", "png"],
    help="Formatos aceptados: JPG, JPEG, PNG",
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Tu imagen", use_container_width=True)
    with col2:
        with st.spinner("Analizando..."):
            result = predict(image, model)
        confidence = result["confidence"]
        if result["state"] == "good":
            st.success(f"### {result['display']}")
            st.metric("Confianza", f"{confidence}%")
        else:
            st.error(f"### {result['display']}")
            st.metric("Confianza", f"{confidence}%")

    with st.expander("Ver probabilidades detalladas"):
        probs = result["probabilities"]
        for label, prob in sorted(probs.items(), key=lambda x: x[1], reverse=True):
            st.progress(prob / 100, text=f"{label}: {prob}%")

    st.caption("Esto es una ayuda visual. Siempre usa tu criterio para decidir si una fruta es apta para consumo.")

st.markdown("---")
st.markdown("**Clases:** Manzana (buena/dañada) · Plátano (bueno/dañado) · Naranja (buena/dañada)")
