import streamlit as st

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
        var parentDoc = window.parent.document;
        if (!parentDoc.getElementById('ga-gtag')) {{
            var script1 = parentDoc.createElement('script');
            script1.id = 'ga-gtag';
            script1.async = true;
            script1.src = 'https://www.googletagmanager.com/gtag/js?id={GOOGLE_ANALYTICS_ID}';
            parentDoc.head.appendChild(script1);

            var script2 = parentDoc.createElement('script');
            script2.innerHTML = `
                window.dataLayer = window.dataLayer || [];
                function gtag(){{dataLayer.push(arguments);}}
                gtag('js', new Date());
                gtag('config', '{GOOGLE_ANALYTICS_ID}');
            `;
            parentDoc.head.appendChild(script2);
        }}
    }})();
    </script>
    """,
    height=0,
    width=0,
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


