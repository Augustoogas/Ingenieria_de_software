from typing import List, Optional
from src.model.socio import Socio
from src.service.socio_service import SocioService


class SocioController:
    def __init__(self, service: Optional[SocioService] = None) -> None:
        self.service = service or SocioService()

    def alta(self, nombre: str, email: str) -> Socio:
        return self.service.alta(nombre=nombre, email=email)

    def listar(self) -> List[Socio]:
        return self.service.listar()

    def activar(self, socio_id: int) -> Socio:
        return self.service.activar(socio_id)

    def desactivar(self, socio_id: int) -> Socio:
        return self.service.desactivar(socio_id)


