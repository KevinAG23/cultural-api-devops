# 🤝 COLLABORATION.md

Este documento resume la experiencia de trabajo colaborativo dentro del proyecto **Cultural API - DevOps distribuido**. Cada integrante del equipo asumió un rol específico en un entorno simulado de desarrollo distribuido, utilizando herramientas de integración continua, contenerización y monitoreo colaborativo.

---

## 🌎 Distribución de roles y ramas

| País       | Rama          | Rol Principal         | Actividades realizadas                         |
|------------|---------------|------------------------|-------------------------------------------------|
| Ecuador    | `dev-ecuador` | Backend Developer      | Implementación del endpoint `/cultural-greeting` |
| India      | `dev-india`   | DevOps Engineer        | Creación de `Dockerfile` multicultural, pruebas locales |
| Alemania   | `dev-germany` | Líder de integración   | Gestión de ramas, merges, convenciones de commits |
| Japón      | `dev-japan`   | QA + CI/CD             | Pruebas automatizadas con `pytest`, configuración de GitHub Actions |

---

## ⏰ Conflictos por zona horaria

Uno de los mayores retos fue la coordinación entre miembros en distintas zonas horarias. Para mitigar esto:

- Se establecieron ventanas comunes para reuniones (por ejemplo, 14h00 UTC).
- Se utilizaron *issues* en GitHub y comentarios en *pull requests* como comunicación asíncrona.
- Los merges se programaron para que ningún miembro tenga cambios inesperados durante su noche local.

---

## 🐳 ¿Qué pasaría si India no tuviera acceso a Docker Hub?

Durante el proyecto, simulamos que el miembro de India no tenía acceso a Docker Hub. Como respuesta:

- Se evaluó el uso de **GitHub Container Registry (GHCR)** como alternativa para compartir imágenes.
- También se diseñó un mecanismo de fallback para construir las imágenes localmente usando `Dockerfile` y compartir por archivo `.tar`.

Esto permitió demostrar resiliencia ante limitaciones externas y garantizar la continuidad del flujo DevOps.

---

## 📈 Análisis de colaboración (GitHub Insights)

Se revisó la pestaña `Insights > Contributors` para evaluar:

- **Commits por miembro:** todos los miembros realizaron al menos 5 commits significativos.
- **Pull requests:** se utilizaron ramas `dev-[país]` con PRs bien documentadas.
- **Tiempo de revisión:** el tiempo medio de respuesta a los PRs fue de 2 a 4 horas.

Este enfoque promovió una colaboración equilibrada, sin sobrecargar a ningún integrante.

---

## 💡 Reflexión final

> “Trabajar como un equipo distribuido con un flujo DevOps fue una experiencia enriquecedora. Logramos integrar tecnologías clave como GitHub Actions, Docker y testing automatizado, manteniendo una comunicación clara y eficiente.”

Algunos aprendizajes importantes:
- La división de roles facilita la responsabilidad individual sin perder la visión global.
- GitHub Actions automatiza el control de calidad y evita errores humanos.
- La planificación anticipada ante limitaciones (como acceso a recursos) mejora la resiliencia del equipo.

---

## 📌 Conclusión

Este ejercicio permitió poner en práctica no solo habilidades técnicas (CI/CD, contenerización, pruebas), sino también habilidades de **colaboración remota**, gestión de tiempo y resolución de conflictos, fundamentales en entornos DevOps reales.
