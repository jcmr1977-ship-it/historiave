import os
import base64
import streamlit as st
import google.generativeai as genai

# 1. Configuración de la Página de Streamlit
st.set_page_config(
    page_title="Historia y Cultura Venezolana - IA",
    page_icon="VE",
    layout="centered"
)

# Función para convertir la imagen local a Base64 y usarla en CSS
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# Reemplaza 'fondo_marca_agua.png' por el nombre exacto de tu archivo de imagen en el repositorio
img_base64 = get_base64_image("venezolaria.jpeg")

# 2. Inyección de CSS para la marca de agua y legibilidad
if img_base64:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.70), rgba(255, 255, 255, 0.40)), 
                              url("data:image/png;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .custom-box {{
            background-color: rgba(255, 255, 255, 0.60);
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
            border-left: 5px solid #1e3a8a;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
# 2. Configuración de la API Key de Gemini
# Intenta leer desde st.secrets (para Streamlit Cloud) o de variables de entorno locales
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except Exception:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

if not GOOGLE_API_KEY:
    st.error("⚠️ No se ha configurado la `GOOGLE_API_KEY`. Por favor, añádela en los Secrets de Streamlit o en tu entorno local.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# 3. Definición del Prompt del Sistema (Restricción temática estricta)
SYSTEM_PROMPT = """
Eres un asistente virtual experto e historiador especializado exclusivamente en Venezuela. 
Tu ámbito de conocimiento y respuesta se limita de forma estricta a los siguientes aspectos de Venezuela:
- Historia política, económica, cultural, popular, académica, sanitaria, deportiva, artística, tecnológica y urbanística.

Reglas obligatorias:
1. Si el usuario hace una pregunta que NO está relacionada con Venezuela o con las áreas temáticas mencionadas anteriormente, debes rechazar amablemente la consulta indicando que tu enfoque es exclusivamente la historia, cultura y desarrollo dominicano.
2. Mantén un tono académico, respetuoso, riguroso y amigable.
3. Proporciona contexto histórico y datos precisos cuando respondas.
"""

# 4. Inicialización del Modelo Gemini (Usando gemini-3.8-flash por velocidad y eficiencia)
@st.cache_resource
def load_gemini_model():
    # Configuramos el modelo con instrucciones de sistema incorporadas en el prompt inicial o rol
    model = genai.GenerativeModel(
        model_name="gemini-3.8-flash",
        system_instruction=SYSTEM_PROMPT
    )
    return model

model = load_gemini_model()

# 5. Interfaz Gráfica de Usuario (UI)
st.title("🇩🇴 Asistente Histórico y Cultural de Venezuela")
st.markdown("Pregúntame sobre la historia política, economía, cultura, deporte, urbanismo y más de Venezuela.")

# Inicializar historial de chat en el session_state de Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "model", 
            "content": "¡Saludos! Estoy a tu disposición para conversar sobre la historia, la cultura, la economía, el arte y los hitos de Venezuela. ¿Qué te gustaría explorar hoy?"
        }
    ]


# C. CAJA DE TEXTO DE LA PREGUNTA
user_input = st.text_input("Escribe tu pregunta sobre la República Dominicana:", value="", key="input_pregunta")

if st.button("Consultar", type="primary"):
    if user_input.strip():
        st.session_state.current_question = user_input
        with st.spinner("Consultando con Groq..."):
            try:
                client = Groq(api_key=GROQ_API_KEY)
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_input}
                    ],
                    model="openai/gpt-oss-20b",
                    temperature=0.3,
                    max_tokens=2048
                )
                st.session_state.current_response = chat_completion.choices[0].message.content
            except Exception as e:
                st.session_state.current_response = f"❌ Ocurrió un error al procesar tu solicitud con Groq: {e}"
    else:
        st.warning("Por favor, escribe una pregunta antes de consultar.")

# D. RESPUESTA ABAJO (Si ya fue consultada)
if st.session_state.current_response:
    st.markdown("---")
    st.subheader("📌 Pregunta realizada:")
    st.markdown(f'<div class="custom-box"><b>{st.session_state.current_question}</b></div>', unsafe_allow_html=True)
    
    st.subheader("🇩🇴 Respuesta:")
    st.markdown(f'<div class="custom-box">{st.session_state.current_response}</div>', unsafe_allow_html=True)
    st.caption("⚡ Estos es una IA y puede cometer errores. *Generado mediante Groq (openai/gpt-oss-20b)*")
   
    st.markdown("---")
    
    # E. BOTÓN DE PRÓXIMA PREGUNTA (Abajo de todo)
    if st.button("🔄 Próxima pregunta", type="secondary"):
        st.session_state.current_question = ""
        st.session_state.current_response = ""
    #    st.session_state.input_pregunta = ""
        st.rerun()
