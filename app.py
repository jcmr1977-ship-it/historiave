import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
    <script>
    (function() {
        var d = window.parent.document;
        var t = d.querySelector('title');
        if (!t) {
            t = d.createElement('title');
            d.head.appendChild(t);
        }
        t.textContent = "Historia Dominicana - IA";
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
