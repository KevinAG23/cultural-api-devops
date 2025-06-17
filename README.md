# 🌍 Cultural API - Proyecto DevOps Distribuido

Este proyecto es una API REST construida con **Python (Flask)** que responde con saludos culturales desde distintos países. Fue desarrollada por un equipo distribuido de 4 personas aplicando prácticas modernas de **DevOps colaborativo**, incluyendo:

- Versionamiento colaborativo con Git/GitHub
- Integración y entrega continua (CI/CD) con GitHub Actions
- Gestión de dependencias multiculturales mediante Docker multietapa
- Monitoreo de colaboración con GitHub Insights

---

## ✅ Funcionalidad de la API

| Método | Endpoint               | Descripción                                       |
|--------|------------------------|---------------------------------------------------|
| GET    | `/cultural-greeting`   | Devuelve un objeto JSON con saludos culturales   |

📌 Ejemplo de respuesta:
```json
{
  "greetings": {
    "Ecuador": "¡Hola!",
    "India": "नमस्ते",
    "Germany": "Hallo",
    "Japan": "こんにちは",
    "Brazil": "Olá"
  }
}
