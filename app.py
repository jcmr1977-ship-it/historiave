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
    f"""
    <script>
    (function() {{
        var d = window.parent.document;
        if (d.getElementById('ga-gtag')) return;

        var s1 = d.createElement('script');
        s1.id = 'ga-gtag';
        s1.async = true;
        s1.src = 'https://www.googletagmanager.com/gtag/js?id={GOOGLE_ANALYTICS_ID}';
        d.head.appendChild(s1);

        var s2 = d.createElement('script');
        s2.innerHTML = "window.dataLayer=window.dataLayer||[];"
                     + "function gtag(){{dataLayer.push(arguments);}}"
                     + "gtag('js', new Date());"
                     + "gtag('config', '{GOOGLE_ANALYTICS_ID}');";
        d.head.appendChild(s2);
    }})();
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


