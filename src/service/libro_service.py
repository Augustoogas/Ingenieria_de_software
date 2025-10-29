from typing import List, Optional
from src.model.libro import Libro
from src.repository.libro_repository import LibroRepository


class LibroService:
    def __init__(self, repo: Optional[LibroRepository] = None) -> None:
        self.repo = repo or LibroRepository()

    def crear_libro(self, titulo: str, autor: str, anio_publicacion: int, isbn: str, ejemplares_totales: int, ejemplares_disponibles: int | None = None) -> Libro:
        return self.repo.create(
            titulo=titulo,
            autor=autor,
            anio_publicacion=anio_publicacion,
            isbn=isbn,
            ejemplares_totales=ejemplares_totales,
            ejemplares_disponibles=ejemplares_disponibles,
        )

    def listar_libros(self) -> List[Libro]:
        return self.repo.list()

    def buscar_por_id(self, id: int) -> Optional[Libro]:
        return self.repo.get(id)

    def buscar_por_isbn(self, isbn: str) -> Optional[Libro]:
        return self.repo.get_by_isbn(isbn)

    def prestar(self, libro_id: int) -> Libro:
        libro = self.repo.get(libro_id)
        if not libro:
            raise ValueError("Libro no encontrado")
        libro.prestar()
        self.repo.update(libro)
        return libro

    def devolver(self, libro_id: int) -> Libro:
        libro = self.repo.get(libro_id)
        if not libro:
            raise ValueError("Libro no encontrado")
        libro.devolver()
        self.repo.update(libro)
        return libro


