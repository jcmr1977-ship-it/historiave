import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
    <script>
    (function() {
        var head = window.parent.document.head;
        var node = window.parent.document.createTextNode("Hello from Streamlit");
        head.appendChild(node);
    })();
    </script>
    """,
    height=0, width=0,
)

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
