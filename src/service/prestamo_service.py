from typing import List, Optional
from src.model.reserva import Reserva
from src.repository.reserva_repository import ReservaRepository
from src.repository.libro_repository import LibroRepository
from src.repository.socio_repository import SocioRepository


class PrestamoService:
    def __init__(
        self,
        reserva_repo: Optional[ReservaRepository] = None,
        libro_repo: Optional[LibroRepository] = None,
        socio_repo: Optional[SocioRepository] = None,
    ) -> None:
        self.reserva_repo = reserva_repo or ReservaRepository()
        self.libro_repo = libro_repo or LibroRepository()
        self.socio_repo = socio_repo or SocioRepository()

    def reservar(self, socio_id: int, libro_id: int, dias: int = 7) -> Reserva:
        socio = self.socio_repo.get(socio_id)
        if not socio or not socio.activo:
            raise ValueError("Socio inexistente o inactivo")

        libro = self.libro_repo.get(libro_id)
        if not libro:
            raise ValueError("Libro no encontrado")
        if not libro.hay_disponible():
            raise ValueError("No hay ejemplares disponibles")

        libro.prestar()
        self.libro_repo.update(libro)

        reserva = self.reserva_repo.create(socio_id=socio_id, libro_id=libro_id, dias=dias)
        return reserva

    def devolver(self, reserva_id: int) -> Reserva:
        reserva = self.reserva_repo.get(reserva_id)
        if not reserva:
            raise ValueError("Reserva no encontrada")
        if reserva.devuelto:
            return reserva

        libro = self.libro_repo.get(reserva.libro_id)
        if not libro:
            raise ValueError("Libro no encontrado para la reserva")

        libro.devolver()
        self.libro_repo.update(libro)

        reserva.devuelto = True
        self.reserva_repo.update(reserva)
        return reserva

    def listar_reservas(self) -> List[Reserva]:
        return self.reserva_repo.list()

    def reservas_por_socio(self, socio_id: int) -> List[Reserva]:
        return self.reserva_repo.list_by_socio(socio_id)

    def reservas_por_libro(self, libro_id: int) -> List[Reserva]:
        return self.reserva_repo.list_by_libro(libro_id)


