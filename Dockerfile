# Usar imagen base de Python
FROM python:3.9-slim

# Directorio
WORKDIR /app

# requirements.txt
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código
COPY . .

# Exponer puerto 3000
EXPOSE 3000

# Ejecutar
CMD ["python", "aplicacion.py"]