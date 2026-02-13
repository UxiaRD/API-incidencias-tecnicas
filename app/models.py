from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Uso de enums para estado y prioridad según el anexo
class Prioridad(str, Enum):
    ALTA = "alta"
    MEDIA = "media"
    BAJA = "baja"

class Estado(str, Enum):
    ABIERTA = "abierta"
    CERRADA = "cerrada"

class Incidencia(BaseModel):
    # El ID es opcional al crear (POST), pero lo asignaremos en el servidor
    id: Optional[int] = None
    descripcion: str
    prioridad: Prioridad
    estado: Estado
    fecha_creacion: datetime = Field(default_factory=datetime.now)