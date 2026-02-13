# API REST de Gestión de Incidencias Técnicas
![CI Status](https://github.com/TU_USUARIO/TU_REPOSITORIO/actions/workflows/ci.yml/badge.svg)

Este proyecto consiste en una API REST desarrollada con FastAPI para la gestión de incidencias técnicas en un entorno de soporte. El sistema permite registrar nuevas incidencias y filtrar aquellas que requieren atención inmediata basándose en su estado y prioridad.

## 	:open_file_folder: Estructura del Proyecto
El repositorio sigue una organización modular para facilitar el mantenimiento y la ejecución de tests:
```
mi-proyecto-api/
├── .github/workflows/ci.yml  # Configuración del pipeline de Integración Continua
├── app/                      # Contiene el código fuente de la app
│   ├── main.py               # Punto de entrada de FastAPI y definición de endpoints
│   ├── models.py             # Modelos Pydantic y Enums
│   └── services.py           # Lógica de negocio (IssueService)
├── tests/                    # Directorio de pruebas automatizadas
│   ├── test_unit.py          # Tests unitarios (pytest)
│   └── test_e2e.py           # Tests end-to-end (peticiones HTTP)
├── requirements.txt          # FastAPI, uvicorn, pytest, httpx, ruff
└── README.md                 # Documentación técnica
```

## :round_pushpin: Endpoints
- ``POST /incidencias``: Crear nueva incidencia.

- ``GET /incidencias/urgentes``: Filtrado de abiertas y alta prioridad.

- ``GET /incidencias/{id}``: Detalle de una incidencia.

- ``PATCH /incidencias/{id}/cerrar``: Cambio de estado rápido.

- ``GET /incidencias/stats/resumen``: Métricas generales.

## 	:arrows_counterclockwise: Pipeline de GitHub Actions
El flujo de integración continua se activa automáticamente con cada ``push`` o ``pull request``.

Realiza los siguientes pasos:
1. **Análisis Estático**: Uso de ``ruff`` para asegurar la calidad y estilo del código.
2. **Tests Unitarios**: Ejecución de pruebas con ``pytest`` para validar la lógica de ``IssueService`` de forma aislada.
3. **Despliegue Temporal y Tests E2E**:
    - **Arranque de la API**: Se inicia el servidor mediante ``uvicorn app.main:app &``. El uso de ``&`` es crucial, ya que permite que la API corra en segundo plano mientras el pipeline continúa con los tests.
    - **Ejecución de Tests E2E**: Se lanzan peticiones HTTP reales contra ``http://localhost:8000`` para validar los códigos de estado y las respuestas de la API en un entorno real.

## :pencil: Decisiones Técnicas y Mejoras
- **Persistencia**: Se ha optado por almacenamiento en memoria (listas) para cumplir con el requisito de simplicidad.

- **Validación**: Se utilizan modelos Pydantic para garantizar que ninguna incidencia se cree sin los campos obligatorios (descripción, prioridad, estado y fecha).

- **Lógica de Negocio**: Se implementó el método ``open_high_priority`` para filtrar eficientemente incidencias abiertas con prioridad alta.

- **Posibles Mejoras**: En una versión productiva, se recomienda sustituir la lista en memoria por una base de datos persistente (como PostgreSQL) y añadir autenticación para proteger los endpoints.

## :woman: Autor
**Uxía RD** - [GitHub](https://github.com/UxiaRD)