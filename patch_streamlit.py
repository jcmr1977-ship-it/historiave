import os
import streamlit as st

def patch_index_html():
    # Obtiene la ruta del paquete estático de streamlit
    streamlit_dir = os.path.dirname(st.__file__)
    index_path = os.path.join(streamlit_dir, "static", "index.html")

    if not os.path.exists(index_path):
        print(f"No se encontró el index.html en: {index_path}")
        return

    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Script o etiquetas meta que deseas inyectar en el <head>
    injection_code = """
        <!-- Script inyectado mediante Docker -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=TU-ID-DE-ANALYTICS"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', 'TU-ID-DE-ANALYTICS');
        </script>
    </head>
    """

    if "TU-ID-DE-ANALYTICS" not in html_content:
        # Reemplazamos la etiqueta de cierre del head con nuestro script + el head cerrado
        new_html_content = html_content.replace("</head>", injection_code)

        with open(index_path, "w", encoding="utf-8") as f:
            f.write(new_html_content)
        print("¡El index.html de Streamlit ha sido parcheado con éxito!")
    else:
        print("El archivo ya contenía el parche.")

if __name__ == "__main__":
    patch_index_html()
