from fastapi import FastAPI, HTTPException
from app.models import Estado, Incidencia, Prioridad
from app.services import IssueService

app = FastAPI(title="API de Incidencias Técnicas")

# Almacenamiento en memoria (lista)
db_incidencias: list[Incidencia] = [
    Incidencia(
        id=1, 
        descripcion="Fallo crítico en el servidor de base de datos", 
        prioridad=Prioridad.ALTA, 
        estado=Estado.ABIERTA
    ),
    Incidencia(
        id=2, 
        descripcion="Actualizar software de los terminales", 
        prioridad=Prioridad.BAJA, 
        estado=Estado.ABIERTA
    ),
    Incidencia(
        id=3, 
        descripcion="Error de conexión en el router principal", 
        prioridad=Prioridad.ALTA, 
        estado=Estado.CERRADA
    ),
    Incidencia(
        id=4, 
        descripcion="Revisión de cables en oficina 4", 
        prioridad=Prioridad.MEDIA, 
        estado=Estado.ABIERTA
    ),
    Incidencia(
        id=5, 
        descripcion="Pantalla azul en puesto de recepción", 
        prioridad=Prioridad.ALTA, 
        estado=Estado.ABIERTA
    )
]

@app.post("/incidencias", response_model=Incidencia, status_code=201)
def crear_incidencia(incidencia: Incidencia):
    # Genera un ID sumando 1 al ID más alto actual o usa 1 si está vacía
    nuevo_id = max([i.id for i in db_incidencias], default=0) + 1
    incidencia.id = nuevo_id
    db_incidencias.append(incidencia)
    return incidencia

@app.get("/incidencias/urgentes", response_model=list[Incidencia])
def obtener_incidencias_urgentes():
    # Usamos la clase de servicio para la lógica de filtrado
    return IssueService.open_high_priority(db_incidencias)

@app.get("/incidencias", response_model=list[Incidencia])
def listar_todas():
    return db_incidencias

@app.get("/incidencias/{incidencia_id}", response_model=Incidencia)
def obtener_incidencia_por_id(incidencia_id: int):
    """Recupera una incidencia específica por su ID."""
    for inc in db_incidencias:
        if inc.id == incidencia_id:
            return inc
    raise HTTPException(status_code=404, detail="Incidencia no encontrada")

@app.patch("/incidencias/{incidencia_id}/cerrar", response_model=Incidencia)
def cerrar_incidencia(incidencia_id: int):
    """Endpoint para cerrar una incidencia rápidamente."""
    for inc in db_incidencias:
        if inc.id == incidencia_id:
            inc.estado = Estado.CERRADA
            return inc
    raise HTTPException(status_code=404, detail="Incidencia no encontrada")

@app.get("/incidencias/stats/resumen")
def obtener_estadisticas():
    """Devuelve un conteo básico de incidencias por estado."""
    abiertas = len([i for i in db_incidencias if i.estado == Estado.ABIERTA])
    cerradas = len([i for i in db_incidencias if i.estado == Estado.CERRADA])
    return {
        "total": len(db_incidencias),
        "abiertas": abiertas,
        "cerradas": cerradas,
        "porcentaje_completado": (cerradas / len(db_incidencias) * 100) if db_incidencias else 0
    }