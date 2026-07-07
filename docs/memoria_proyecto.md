# Proyecto de IA: Clasificador de Calidad de Frutas

**Asignatura:** Tendencias de Inteligencia Artificial Aplicada
**Unidad:** 1 - IA, tipos, diseños y aplicaciones
**Estudiante:**
**Fecha:**

---

## FASE 1 · INTELIGENCIA (20%)

### 1.1 Métricas de desempeño (10%)

**¿Cuál es un error aceptable para los objetivos de negocio?**

| Concepto | Valor |
|---|---|
| **Métrica principal** | Accuracy |
| **Umbral aceptable** | ≥ 90% en test |
| **Error aceptable** | < 10% |
| **Error humano de referencia** | ~5-8% (personas no expertas clasificando frutas visualmente) |
| **Error de entrenamiento esperado** | ~2-5% (el modelo memoriza patrones del dataset) |
| **Error de test esperado** | ~8-12% (generalización a nuevas fotos) |
| **Métrica secundaria** | F1-score (ponderado) para mitigar posible desbalanceo |
| **Justificación** | El objetivo es acercarse al error humano. Un 90% de accuracy es suficiente para asistir al consumidor sin reemplazar su criterio. Falsos negativos (clasificar dañado como bueno) se priorizan con F1 alto para seguridad alimentaria. |

Se distingue entre:
- **Error humano:** tasa natural de error al clasificar frutas a simple vista (~5-8%)
- **Error de entrenamiento:** error del modelo sobre los datos con los que fue entrenado (~2-5%)
- **Error de test:** error del modelo sobre datos no vistos (~8-12%)

### 1.2 Alcance (10%)

**Especifica el foco del uso de la IA: ¿sobre qué queremos que actúe?**

| ¿Qué resuelve? | ¿Qué queda FUERA? |
|---|---|
| Clasificar fotos de frutas en 3 tipos (manzana, plátano, naranja) | Estimar peso, tamaño o volumen |
| Determinar si cada fruta está buena (verde/madura) o dañada | Recomendar recetas o usos |
| Mostrar resultado con nivel de confianza (%) | Predecir cuándo se va a deteriorar |
| Funcionar como web app desde cualquier navegador | Funcionalidad móvil nativa (iOS/Android) |
| Ser usado por consumidores finales en ámbito doméstico | Detectar enfermedades no visibles externamente |
| | Funcionar sin conexión a internet |

**Usuario objetivo:** Consumidor final, para uso doméstico.

**Formato:** Web app (subir foto desde navegador).

**Clases totales:** 6 (manzana buena, manzana dañada, plátano bueno, plátano dañado, naranja buena, naranja dañada).

---

## FASE 2 · PROCESO EMPRESARIAL (20%)

### 2.1 Objetivo estratégico (10%)

**¿Cuál es el objetivo estratégico con la IA?**

| Elemento | Descripción |
|---|---|
| **Cliente del producto** | Consumidores finales que compran fruta y quieren evitar consumir fruta dañada |
| **Soluciones para el cliente** | - Reducir desperdicio identificando rápidamente fruta en mal estado
- Ayudar a decidir si una fruta aún es consumible
- Educar visualmente sobre signos de deterioro |
| **Externalidades de red** | - A más usuarios, más datos para mejorar el modelo (feedback loop)
- Normalización del hábito de revisar calidad con IA
- Datos agregados sobre tendencias de deterioro |

**Frase resumen del objetivo estratégico:**
> *"Ser la herramienta de referencia para que consumidores verifiquen la calidad de su fruta en segundos, reduciendo el desperdicio alimentario doméstico."*

### 2.2 Objetivo operativo (10%)

**¿Cuál es el objetivo operativo? Áreas impactadas y metas de mejora medibles.**

| Área impactada | Impacto | Meta (trimestre 1) |
|---|---|---|
| **Talento humano** | Estudiante único desarrollador | Completar desarrollo funcional en 6 semanas |
| **Finanzas** | Hosting web gratuito + GPU gratuita (Colab) | Costo operativo < 5€/mes |
| **Operaciones** | Pipeline dataset → entrenamiento → deploy automatizado | Pipeline end-to-end funcional |
| **Marketing** | Landings, redes sociales, blog de tecnología | 100 usuarios beta en semana 1 post-lanzamiento |

**Metas operativas específicas y medibles:**

1. **Dataset:** ≥ 1.500 fotos balanceadas (250 por clase × 6 clases)
2. **Modelo:** Accuracy ≥ 90%, F1 ≥ 0.88, latencia < 2s por predicción
3. **Web app:** Carga de foto + resultado en < 3s
4. **MVP listo:** 6 semanas desde inicio
5. **Cobertura:** manzana, plátano, naranja en estado bueno y dañado

---

## FASE 3 · TECNOLOGÍA DE LA IA (20%)

### 3.1 Propiedad intelectual — PI (10%)

**¿Qué tecnologías o modelos de IA utilizarás? Considera licencias y uso de código open source.**

| Componente | Tecnología | Licencia | Open source |
|---|---|---|---|
| Framework de Deep Learning | PyTorch 2.x | BSD | Sí |
| Visión por computadora | torchvision | BSD | Sí |
| Modelo base | MobileNetV3 (pre-entrenado en ImageNet) | BSD (pesos) | Sí |
| Web app | Streamlit | Apache 2.0 | Sí |
| Dataset | Fruit-360 | ODbL / CC BY-SA | Sí |
| Procesamiento imágenes | Pillow + OpenCV | PIL / Apache 2.0 | Sí |
| Métricas | scikit-learn | BSD | Sí |

**Justificación de la elección tecnológica:**

- **MobileNetV3:** 5.4M parámetros, inferencia < 1s en CPU. Ideal para consumidor final sin GPU. Arquitectura eficiente diseñada para dispositivos con recursos limitados.
- **Transfer learning:** Reutilizamos pesos pre-entrenados en ImageNet. Requiere pocos datos (~200 imágenes por clase) para obtener buen rendimiento.
- **PyTorch:** Framework más utilizado en investigación, amplia comunidad, documentación extensa. Ideal para fine-tuning.
- **Streamlit:** Permite crear web app interactiva con solo Python, sin necesidad de HTML/CSS/JS. Deploy gratuito en Streamlit Cloud.
- **Stack 100% open source:** Sin costos de licencias, reproducible, auditable.

### 3.2 Estrategia de datos (10%)

**¿Dónde capturas los datos y qué gobierno de datos usarás?**

| Aspecto | Estrategia |
|---|---|
| **Fuente principal** | Fruit-360 (Kaggle) — dataset público con ~90 frutas, imágenes 100×100px |
| **Subconjunto** | Filtrar solo manzana, plátano, naranja (~3.000 imágenes iniciales) |
| **Aumento de datos** | Rotaciones (±20°), flip horizontal, brillo variable, zoom (±10%), -> multiplica dataset ~4x |
| **Etiquetado** | Fruit-360 ya viene etiquetado por tipo. Se re-etiqueta estado (bueno/dañado) mediante criterios visuales: manchas, magulladuras, color anómalo = dañado |
| **Calidad** | Balanceo de clases (igual nº bueno/dañado por fruta). Eliminar borrosas o mal iluminadas. División 70/15/15 train/val/test |
| **Gobierno** | Versionado del dataset (v1.0, v1.1...). Pipeline reproducible con seed fijo. Documentación de criterios de etiquetado |
| **Privacidad** | Las imágenes solo contienen frutas, sin datos personales. No se almacenan fotos de usuarios tras la predicción. Si hay feedback loop, se anonimiza antes de agregar |

**Pipeline de datos:**
```
Fruit-360 → filtrar 3 frutas → separar bueno/dañado → augment → train/val/test → modelo
```

---

## FASE 4 · PROCESO DE CAMBIO — TINKERING / CREACIÓN (20%)

### 4.1 Desarrollo de software (8%)

**Versionamiento, MLOps, DevSecOps, plan de pruebas, metodologías ágiles y UX/UI.**

| Práctica | Implementación |
|---|---|
| **Versionamiento** | Git + GitHub. Ramas: `main`, `develop`, `feature/*`. Commits semánticos (`feat:`, `fix:`, `docs:`) |
| **MLOps básico** | Pipeline reproducible: `train.py` que descarga datos → aumenta → entrena → evalúa → guarda modelo. Seed fijo. Logging de métricas |
| **DevSecOps** | No exponer API keys (`.env` + `.gitignore`). Validar archivos subidos (solo imágenes, <10MB, jpg/png). Rate limiting básico |
| **Plan de pruebas** | - Unit tests: `pytest` para funciones de preprocesado y métricas
- Integration test: pipeline end-to-end con 10 imágenes de prueba
- Validation test: accuracy en conjunto de validación post-entreno
- UI test: manual con Streamlit (cargar foto, ver resultado) |
| **Metodología ágil** | Sprint semanal de 1 persona con backlog priorizado. Cada sprint produce un incremento funcional |
| **UX/UI** | Streamlit: drag & drop de foto, spinner de carga, resultado con color (verde = buena, rojo = dañada), confianza visible, tooltips explicativos |

### 4.2 Recursos y costos (6%)

**Datos, infraestructura y gestión de datos, hardware/software, licencias y personal.**

| Recurso | Detalle | Costo |
|---|---|---|
| Datos | Fruit-360 (Kaggle, descarga gratuita) + aumento de datos | 0 € |
| Infraestructura | Google Colab (GPU gratuita para entrenamiento) | 0 € |
| Hardware/Software | Laptop personal + Python 3.10, PyTorch | 0 € |
| Licencias | Todo open source (BSD, Apache 2.0, MIT) | 0 € |
| Personal | 1 estudiante-desarrollador | 0 € |
| Hosting web app | Streamlit Community Cloud | 0 € |
| Dominio | Subdominio gratuito (`.streamlit.app`) | 0 € |
| **TOTAL MENSUAL** | | **0 €** |

**Costo de tiempo:** ~60 horas totales (6 semanas × 10h/semana)

### 4.3 Rentabilidad y monetización (6%)

**Análisis de ROI/beneficios y modelo de monetización.**

**Uso interno (MVP):**
- Proyecto académico. Beneficio principal: aprendizaje + calificación.
- Sin ingresos directos en etapa inicial.

**Como servicio a terceros (post-MVP):**

| Plan | Precio | Incluye |
|---|---|---|
| **Gratuito** | 0 € | 10 clasificaciones/día |
| **Premium** | 3,99 €/mes | Clasificaciones ilimitadas, historial, reportes semanales |
| **API** | 0,01 €/llamada | Integración para terceros (supermercados, apps) |

**ROI estimado (escenarios):**

| Escenario | Costo anual | Ingreso anual | ROI |
|---|---|---|---|
| 100 usuarios premium | 84 € | 4.788 € | ~57x |
| 500 usuarios premium | 84 € | 23.940 € | ~285x |
| API (10k llamadas/mes) | 84 € | 1.200 € | ~14x |

**Beneficio adicional:** Datos agregados anónimos sobre deterioro de frutas por región/estación → potencial venta a supermercados, agricultores o cadenas de suministro.

---

## CRITERIO TRANSVERSAL · COHERENCIA E IMPACTO (20%)

### T.1 Integración y viabilidad (10%)

**Integra las cuatro fases de forma coherente y viable, de principio a fin.**

| Fase | Output | Conexión |
|---|---|---|
| 1. Inteligencia | Métrica: ≥90% accuracy. Alcance: 3 frutas × 2 estados | Define qué datos y métricas necesito |
| 2. Proceso Empresarial | Objetivo: reducir desperdicio doméstico | Justifica por qué existe el proyecto |
| 3. Tecnología IA | Stack open source + dataset Fruit-360 | Define cómo se construye técnicamente |
| 4. Cambio/Creación | GitHub + pruebas + costos + monetización | Cierra el ciclo con plan de desarrollo y sostenibilidad |

**Conexiones fuertes entre fases:**
- Las métricas de Fase 1 se verifican empíricamente en Fase 4 (evaluación del modelo)
- Cada costo de Fase 4 se justifica con las tecnologías elegidas en Fase 3 (todo open source)
- El modelo de monetización de Fase 4 responde directamente al objetivo estratégico de Fase 2
- El alcance de Fase 1 define los límites del dataset en Fase 3

**Viabilidad:** Proyecto 100% viable con inversión 0€, herramientas gratuitas (Colab, Streamlit Cloud), stack open source y conocimientos básicos de Python/ML.

### T.2 Impacto social y ética (10%)

**Beneficios y desafíos de la IA en la sociedad; riesgos y ética.**

| Dimensión | Análisis |
|---|---|
| **Beneficios sociales** | - Reduce desperdicio alimentario doméstico (~30% de la comida se desperdicia en hogares)
- Educa al consumidor sobre signos de deterioro
- Empodera decisiones de consumo informadas |
| **Sesgo (Riesgo 1)** | El modelo puede funcionar mejor con frutas comunes (manzana roja) que con variedades menos representadas (manzana golden, plátano macho). **Mitigación:** Incluir variedades diversas en el dataset de entrenamiento |
| **Sobredependencia (Riesgo 2)** | Usuarios podrían dejar de usar su propio juicio visual. **Mitigación:** Mostrar disclaimer: *"Esto es una ayuda, no reemplaza tu criterio"* |
| **Falsos negativos (Riesgo 3)** | Clasificar fruta dañada como "buena" → riesgo de intoxicación. **Mitigación:** Optimizar F1 con énfasis en recall para clase "dañado". Priorizar seguridad sobre métrica bruta |
| **Exclusión (Riesgo 4)** | Personas mayores o sin acceso digital no se benefician. **Mitigación:** Interfaz simple, accesible, con imágenes grandes y tooltips |
| **Desplazamiento laboral** | No aplica directamente. No reemplaza empleos existentes; complementa la decisión del consumidor |
| **Transparencia** | La app muestra la confianza de cada predicción en %, permitiendo al usuario decidir cuándo confiar |

**Reflexión final:**
> *"La IA aplicada a la reducción del desperdicio alimentario tiene un impacto social netamente positivo, siempre que se implementen salvaguardas contra sesgos y se priorice la seguridad del consumidor por encima de la precisión estadística."*

---

## Escala de valoración

| Puntaje ponderado | Nivel de logro |
|---|---|
| 3.5 — 4.0 | Destacado |
| 2.6 — 3.4 | Competente |
| 1.6 — 2.5 | En desarrollo |
| 1.0 — 1.5 | Incipiente |
