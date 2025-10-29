from typing import Callable
from src.controller.libro_controller import LibroController
from src.controller.socio_controller import SocioController
from src.controller.reserva_controller import ReservaController


class CLI:
    def __init__(self) -> None:
        self.libros = LibroController()
        self.socios = SocioController()
        self.reservas = ReservaController()

    def run(self) -> None:
        acciones: dict[str, tuple[str, Callable[[], None]]] = {
            "1": ("Alta socio", self._alta_socio),
            "2": ("Listar socios", self._listar_socios),
            "3": ("Alta libro", self._alta_libro),
            "4": ("Listar libros", self._listar_libros),
            "5": ("Reservar (prestar) libro", self._reservar_libro),
            "6": ("Listar reservas", self._listar_reservas),
            "7": ("Devolver libro", self._devolver_libro),
            "0": ("Salir", lambda: None),
        }

        while True:
            print("\n=== Biblioteca - Menú ===")
            for k, (texto, _) in acciones.items():
                print(f"{k}. {texto}")
            opcion = input("Elegí una opción: ").strip()
            if opcion == "0":
                print("Chau!")
                break
            accion = acciones.get(opcion)
            if not accion:
                print("Opción inválida")
                continue
            try:
                accion[1]()
            except Exception as e:
                print(f"Error: {e}")

    def _alta_socio(self) -> None:
        nombre = input("Nombre: ").strip()
        email = input("Email: ").strip()
        socio = self.socios.alta(nombre, email)
        print(f"Socio creado: id={socio.id}, nombre={socio.nombre}")

    def _listar_socios(self) -> None:
        for s in self.socios.listar():
            estado = "activo" if s.activo else "inactivo"
            print(f"[{s.id}] {s.nombre} <{s.email}> - {estado}")

    def _alta_libro(self) -> None:
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        anio = int(input("Año de publicación: ").strip())
        isbn = input("ISBN: ").strip()
        totales = int(input("Ejemplares totales: ").strip())
        libro = self.libros.crear(titulo, autor, anio, isbn, totales)
        print(f"Libro creado: id={libro.id}, '{libro.titulo}' ({libro.ejemplares_disponibles}/{libro.ejemplares_totales})")

    def _listar_libros(self) -> None:
        for l in self.libros.listar():
            print(f"[{l.id}] {l.titulo} - {l.autor} | disp: {l.ejemplares_disponibles}/{l.ejemplares_totales}")

    def _reservar_libro(self) -> None:
        socio_id = int(input("ID Socio: ").strip())
        libro_id = int(input("ID Libro: ").strip())
        dias = input("Días (enter=7): ").strip()
        dias_int = int(dias) if dias else 7
        reserva = self.reservas.reservar(socio_id, libro_id, dias_int)
        print(f"Reserva creada: id={reserva.id}, vence={reserva.fecha_vencimiento.date()}")

    def _listar_reservas(self) -> None:
        for r in self.reservas.listar():
            estado = "devuelto" if r.devuelto else "en curso"
            print(f"[{r.id}] socio={r.socio_id} libro={r.libro_id} - {estado}")

    def _devolver_libro(self) -> None:
        reserva_id = int(input("ID Reserva: ").strip())
        r = self.reservas.devolver(reserva_id)
        print(f"Reserva {r.id} marcada como devuelta")


if __name__ == "__main__":
    CLI().run()

