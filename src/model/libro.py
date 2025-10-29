from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Libro:
    id: int
    titulo: str
    autor: str
    anio_publicacion: int
    isbn: str
    ejemplares_totales: int
    ejemplares_disponibles: int = field(default=0)

    def __post_init__(self) -> None:
        if self.ejemplares_totales < 0:
            raise ValueError("Los ejemplares totales no pueden ser negativos")
        if self.ejemplares_disponibles < 0:
            raise ValueError("Los ejemplares disponibles no pueden ser negativos")
        if self.ejemplares_disponibles > self.ejemplares_totales:
            raise ValueError("Los disponibles no pueden superar a los totales")
        if not self.titulo.strip():
            raise ValueError("El título no puede ser vacío")
        if not self.autor.strip():
            raise ValueError("El autor no puede ser vacío")
        if not self.isbn.strip():
            raise ValueError("El ISBN no puede ser vacío")

    def hay_disponible(self) -> bool:
        return self.ejemplares_disponibles > 0

    def prestar(self) -> None:
        if not self.hay_disponible():
            raise ValueError("No hay ejemplares disponibles para prestar")
        self.ejemplares_disponibles -= 1

    def devolver(self) -> None:
        if self.ejemplares_disponibles >= self.ejemplares_totales:
            raise ValueError("No se puede devolver: ya están todos los ejemplares")
        self.ejemplares_disponibles += 1


