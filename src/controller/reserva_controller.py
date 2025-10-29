from typing import List, Optional
from src.model.reserva import Reserva
from src.service.prestamo_service import PrestamoService


class ReservaController:
    def __init__(self, service: Optional[PrestamoService] = None) -> None:
        self.service = service or PrestamoService()

    def reservar(self, socio_id: int, libro_id: int, dias: int = 7) -> Reserva:
        return self.service.reservar(socio_id=socio_id, libro_id=libro_id, dias=dias)

    def devolver(self, reserva_id: int) -> Reserva:
        return self.service.devolver(reserva_id)

    def listar(self) -> List[Reserva]:
        return self.service.listar_reservas()

    def listar_por_socio(self, socio_id: int) -> List[Reserva]:
        return self.service.reservas_por_socio(socio_id)

    def listar_por_libro(self, libro_id: int) -> List[Reserva]:
        return self.service.reservas_por_libro(libro_id)


