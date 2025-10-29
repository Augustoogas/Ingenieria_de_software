from typing import List, Optional
from src.model.socio import Socio
from src.repository.socio_repository import SocioRepository


class SocioService:
    def __init__(self, repo: Optional[SocioRepository] = None) -> None:
        self.repo = repo or SocioRepository()

    def alta(self, nombre: str, email: str) -> Socio:
        return self.repo.create(nombre=nombre, email=email, activo=True)

    def listar(self) -> List[Socio]:
        return self.repo.list()

    def buscar_por_id(self, id: int) -> Optional[Socio]:
        return self.repo.get(id)

    def activar(self, id: int) -> Socio:
        socio = self._require(id)
        socio.activo = True
        self.repo.update(socio)
        return socio

    def desactivar(self, id: int) -> Socio:
        socio = self._require(id)
        socio.activo = False
        self.repo.update(socio)
        return socio

    def _require(self, id: int) -> Socio:
        socio = self.repo.get(id)
        if not socio:
            raise ValueError("Socio no encontrado")
        return socio


