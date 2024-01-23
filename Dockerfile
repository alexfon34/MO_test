#Usar la imagen de python
FROM python:3.13.0a3-bookworm

#Configura el directorio de la aplicación
WORKDIR /app

#Copia el archivo de requerimientos de la aplicación
COPY requirements.txt .

#Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Copia el contenido del directorio al contendor en la carpeta raiz
COPY ./ ./

#Habilita el puerto 8000
EXPOSE 8000

#Ejecuta la apliación en el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]