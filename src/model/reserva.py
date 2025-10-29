from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Reserva:
    id: int
    socio_id: int
    libro_id: int
    fecha_reserva: datetime
    fecha_vencimiento: datetime
    devuelto: bool = False

    @classmethod
    def crear(cls, id: int, socio_id: int, libro_id: int, dias: int = 7) -> "Reserva":
        ahora = datetime.now()
        return cls(
            id=id,
            socio_id=socio_id,
            libro_id=libro_id,
            fecha_reserva=ahora,
            fecha_vencimiento=ahora + timedelta(days=dias),
        )

    def esta_vencida(self) -> bool:
        return not self.devuelto and datetime.now() > self.fecha_vencimiento


