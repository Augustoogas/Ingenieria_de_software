from typing import List, Optional
from src.model.socio import Socio


class SocioRepository:
    _instance: Optional["SocioRepository"] = None

    def __new__(cls) -> "SocioRepository":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._data = {}
            cls._instance._next_id = 1
        return cls._instance

    def create(self, nombre: str, email: str, activo: bool = True) -> Socio:
        socio = Socio(id=self._next_id, nombre=nombre, email=email, activo=activo)
        self._data[self._next_id] = socio
        self._next_id += 1
        return socio

    def get(self, id: int) -> Optional[Socio]:
        return self._data.get(id)

    def get_by_email(self, email: str) -> Optional[Socio]:
        return next((s for s in self._data.values() if s.email == email), None)

    def list(self) -> List[Socio]:
        return list(self._data.values())

    def update(self, socio: Socio) -> None:
        if socio.id not in self._data:
            raise KeyError("Socio no encontrado")
        self._data[socio.id] = socio

    def delete(self, id: int) -> None:
        self._data.pop(id, None)


