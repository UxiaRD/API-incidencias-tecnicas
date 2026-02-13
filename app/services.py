from app.models import Incidencia, Estado, Prioridad

class IssueService:
    @staticmethod
    def open_high_priority(incidencias: list[Incidencia]) -> list[Incidencia]:
        """
        Lógica de negocio: Recuperar incidencias abiertas con prioridad alta.
        """
        return [
            inc for inc in incidencias 
            if inc.estado == Estado.ABIERTA and inc.prioridad == Prioridad.ALTA
        ]