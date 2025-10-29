from typing import List, Optional
from src.model.reserva import Reserva


class ReservaRepository:
    _instance: Optional["ReservaRepository"] = None

    def __new__(cls) -> "ReservaRepository":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._data = {}
            cls._instance._next_id = 1
        return cls._instance

    def create(self, socio_id: int, libro_id: int, dias: int = 7) -> Reserva:
        reserva = Reserva.crear(id=self._next_id, socio_id=socio_id, libro_id=libro_id, dias=dias)
        self._data[self._next_id] = reserva
        self._next_id += 1
        return reserva

    def get(self, id: int) -> Optional[Reserva]:
        return self._data.get(id)

    def list(self) -> List[Reserva]:
        return list(self._data.values())

    def list_by_socio(self, socio_id: int) -> List[Reserva]:
        return [r for r in self._data.values() if r.socio_id == socio_id]

    def list_by_libro(self, libro_id: int) -> List[Reserva]:
        return [r for r in self._data.values() if r.libro_id == libro_id]

    def update(self, reserva: Reserva) -> None:
        if reserva.id not in self._data:
            raise KeyError("Reserva no encontrada")
        self._data[reserva.id] = reserva

    def delete(self, id: int) -> None:
        self._data.pop(id, None)


