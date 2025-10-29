from typing import List, Optional
from src.model.libro import Libro
from src.service.libro_service import LibroService


class LibroController:
    def __init__(self, service: Optional[LibroService] = None) -> None:
        self.service = service or LibroService()

    def crear(self, titulo: str, autor: str, anio_publicacion: int, isbn: str, ejemplares_totales: int, ejemplares_disponibles: int | None = None) -> Libro:
        return self.service.crear_libro(
            titulo=titulo,
            autor=autor,
            anio_publicacion=anio_publicacion,
            isbn=isbn,
            ejemplares_totales=ejemplares_totales,
            ejemplares_disponibles=ejemplares_disponibles,
        )

    def listar(self) -> List[Libro]:
        return self.service.listar_libros()

    def prestar(self, libro_id: int) -> Libro:
        return self.service.prestar(libro_id)

    def devolver(self, libro_id: int) -> Libro:
        return self.service.devolver(libro_id)


