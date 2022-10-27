# Instalación de python
FROM python:3.8

# instalación de las librerías necesarias
RUN pip install fastapi uvicorn[standard]

# ejecutamos el puerto donde corre la aplicación
EXPOSE 80

# añado las dependencias de la app en una carpeta app de docker
COPY ./app /app

# comando de ejecución
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]