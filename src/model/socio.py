from dataclasses import dataclass


@dataclass
class Socio:
    id: int
    nombre: str
    email: str
    activo: bool = True

    def __post_init__(self) -> None:
        if not self.nombre.strip():
            raise ValueError("El nombre no puede ser vacío")
        if "@" not in self.email or not self.email.strip():
            raise ValueError("Email inválido")


