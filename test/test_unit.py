import pytest
from app.models import Incidencia, Estado, Prioridad
from app.services import IssueService

def test_open_high_priority_filter():
    # Preparamos datos de prueba
    incidencias = [
        Incidencia(descripcion="Error A", prioridad=Prioridad.ALTA, estado=Estado.ABIERTA),
        Incidencia(descripcion="Error B", prioridad=Prioridad.BAJA, estado=Estado.ABIERTA),
        Incidencia(descripcion="Error C", prioridad=Prioridad.ALTA, estado=Estado.CERRADA),
    ]
    
    # Ejecutamos la lógica de negocio
    resultado = IssueService.open_high_priority(incidencias)
    
    # Verificaciones
    assert len(resultado) == 1
    assert resultado[0].descripcion == "Error A"
    assert resultado[0].prioridad == Prioridad.ALTA
    assert resultado[0].estado == Estado.ABIERTA

def test_open_high_priority_empty():
    # Verificamos que maneje listas vacías
    assert IssueService.open_high_priority([]) == []