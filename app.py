import streamlit as st
import streamlit.components.v1 as components

# Configuración básica de la página
st.set_page_config(
    page_title="Mi App Hola Mundo",
    page_icon="👋",
    layout="centered"
)

# --- GOOGLE ANALYTICS (INYECCIÓN EN EL HEAD REAL) ---
GOOGLE_ANALYTICS_ID = "G-YCZN022HR5"

components.html(
    """
    <script>
        document.head.appendChild(
            document.createTextNode("<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YCZN022HR5"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-YCZN022HR5');
</script>")
        );
    </script>
    """,
    height=0, width=0,
)

#------------------------------------------------------------------
# Función para convertir la imagen local a Base64 y usarla en CSS
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# Título principal
st.title("¡Hola, mundo!")
st.write("Esta es una aplicación básica de Streamlit.")

st.markdown("---")


