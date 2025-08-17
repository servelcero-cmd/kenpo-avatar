# 1. Usar una imagen oficial de Python como sistema operativo base
FROM python:3.10-slim

# 2. Establecer variables de entorno para que Python corra limpiamente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Copiar el futuro archivo de dependencias y luego instalarlas
# (Crearemos el archivo requirements.txt en el siguiente paso)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar todo el código de la carpeta 'backend' al contenedor
COPY . /app/

# 6. Exponer el puerto que la aplicación usará para comunicarse
EXPOSE 8000

# 7. (Conceptual) El comando para iniciar el servidor de Django
# Este comando se ejecutará cuando el contenedor se inicie
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
