from typing import Dict, List, Optional
from src.model.libro import Libro


class LibroRepository:
    _instance: Optional["LibroRepository"] = None

    def __new__(cls) -> "LibroRepository":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._data = {}
            cls._instance._next_id = 1
        return cls._instance

    def create(self, titulo: str, autor: str, anio_publicacion: int, isbn: str, ejemplares_totales: int, ejemplares_disponibles: int | None = None) -> Libro:
        if ejemplares_disponibles is None:
            ejemplares_disponibles = ejemplares_totales
        libro = Libro(
            id=self._next_id,
            titulo=titulo,
            autor=autor,
            anio_publicacion=anio_publicacion,
            isbn=isbn,
            ejemplares_totales=ejemplares_totales,
            ejemplares_disponibles=ejemplares_disponibles,
        )
        self._data[self._next_id] = libro
        self._next_id += 1
        return libro

    def get(self, id: int) -> Optional[Libro]:
        return self._data.get(id)

    def get_by_isbn(self, isbn: str) -> Optional[Libro]:
        return next((l for l in self._data.values() if l.isbn == isbn), None)

    def list(self) -> List[Libro]:
        return list(self._data.values())

    def update(self, libro: Libro) -> None:
        if libro.id not in self._data:
            raise KeyError("Libro no encontrado")
        self._data[libro.id] = libro

    def delete(self, id: int) -> None:
        self._data.pop(id, None)


