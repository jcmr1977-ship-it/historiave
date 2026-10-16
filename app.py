import streamlit as st

# Configuración básica de la página
st.set_page_config(
    page_title="Mi App Hola Mundo",
    page_icon="👋",
    layout="centered"
)

# Título principal
st.title("¡Hola, mundo!")
st.write("Esta es una aplicación básica de Streamlit.")

st.markdown("---")

# Sección para mostrar el script de Google en texto
st.subheader("Ejemplo de Script de Google (Texto)")
st.write("Aquí puedes ver el código de un script de Google (por ejemplo, Google Analytics) presentado en texto:")

# Script de ejemplo en texto plano
google_script_example = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=TU_ID_DE_SEGUIMIENTO"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'TU_ID_DE_SEGUIMIENTO');
</script>
"""

# Mostrar el script dentro de un bloque de código con sintaxis HTML
st.code(google_script_example, language="html")
