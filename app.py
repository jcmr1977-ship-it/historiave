import streamlit as st
import streamlit.components.v1 as components

# Inyección directa de un elemento <script> en el <head> padre
components.html(
    """
    <script>
    (function() {
        var head = window.parent.document.head;
        
        // Creamos la etiqueta <script> real
        var script = window.parent.document.createElement('script');
        script.type = 'text/javascript';
        script.text = 'console.log("¡Script ejecutado en el head del padre!");';
        
        // La añadimos al <head>
        head.appendChild(script);
    })();
    </script>
    """,
    height=0,
    width=0,
)

# Configuración de la página (Importante: debe ir idealmente al inicio del archivo)
st.set_page_config(
    page_title="Mi App Hola Mundo",
    page_icon="👋",
    layout="centered"
)

st.title("¡Hola, mundo!")
st.write("Esta es una aplicación básica de Streamlit.")
