# Etapa 1: capa base multicultural (Alpine)
FROM alpine:latest as base
RUN apk add --no-cache curl

# Etapa 2: Ubuntu para entorno completo
FROM ubuntu:20.04

# Evitar preguntas interactivas
ENV DEBIAN_FRONTEND=noninteractive

# Instalar Python y pip
RUN apt update && apt install -y python3 python3-pip

# Copiar la capa multicultural base
COPY --from=base / /multicultural-layer

# Crear directorio de la app
WORKDIR /app

# Copiar código
COPY . /app

# Instalar dependencias
RUN pip3 install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 5000

# Ejecutar app
CMD ["python3", "app.py"]
