# Usa una imagen oficial ligera de Python
FROM python:3.11-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Instala las dependencias del proyecto (incluyendo Streamlit)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación y el script de parcheo
COPY . .

# EJECUTA EL SCRIPT: Esto modifica el index.html instalado en el entorno de Python
RUN python patch_streamlit.py

# Expone el puerto por defecto de Streamlit
EXPOSE 8501

# Comando para iniciar la aplicación
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
