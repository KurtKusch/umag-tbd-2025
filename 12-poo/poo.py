from typing import List, Optional

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool):
        self.titulo: str = titulo
        self.autor: str = autor
        self.isbn: str = isbn
        self.disponible: bool =True
    
    def mostrar_info(self) -> None:
        disponibilidad = "disponible" if self.disponible else "no disponible"
        print(f"Libro: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}\nEstado: {disponibilidad}")
    
    def prestar(self) -> None:
        self.disponible = False
        
    def devolver(self) -> None:
        self.disponible = True

        
class Usuario:
    def __init__(self, nombre : str, id_usuario: str, prestamos: List[Libro]):
        self.nombre: str = nombre
        self.id_usuario: str = id_usuario
        self.prestamos: List[Libro] = []
    
    def tomar_libro(self, libro: Libro) -> bool:
        if libro.disponible:
            libro.prestar()
            self.prestamos.append(libro)
            print(f"{self.nombre} ha tomado el libro '{libro.titulo}'.")
            return True
        print(f"El libro '{libro.titulo}' no está disponible.")
        return False
    
    def devolver_libro(self, libro: Libro) -> None:
        if libro in self.prestamos:
            self.prestamos.remove(libro)
            libro.devolver()
            print(f"{self.nombre} ha devuelto el libro '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}'.")
    
class Biblioteca:
    def __init__(self, nombre: str, libros: List[Libro], usuarios: List[Usuario]):
        self.nombre: str = nombre
        self.libros: List[Libro] = []
        self.usuarios: List[Usuario] = []
        
    def agregar_libro(self, libro: Libro) -> None:
        self.libros.append(libro)
        print(f"El libro '{libro.titulo}' ha sido agregado a la biblioteca.")
    
    def registrar_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)
        print(f"El usuario '{usuario.nombre}' ha sido registrado.")
        
    def mostrar_libros_disponibles(self) -> None:
        print("Libros disponibles:")
        for libro in self.libros:
            if libro.disponible:
                print(f"- {libro.titulo}")
    
    def buscar_libro_por_titulo(self, titulo: str) -> Optional[Libro]:
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

libro1 = Libro("ola", "Kurt Kusch", "123-321", True)
libro2 = Libro("k pasa", "Los k", "321-123", True)

usuario1 = Usuario("Jose", "1", [])
usuario2 = Usuario("Mario", "2", [])

biblioteca1 = Biblioteca("Biblioteca Municipal", [], [])

biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)

biblioteca1.registrar_usuario(usuario1)
biblioteca1.registrar_usuario(usuario2)

biblioteca1.mostrar_libros_disponibles()

usuario1.tomar_libro(libro1)

biblioteca1.mostrar_libros_disponibles()

usuario2.tomar_libro(libro1)
usuario2.tomar_libro(libro2)

biblioteca1.mostrar_libros_disponibles()

usuario1.devolver_libro(libro1)

biblioteca1.mostrar_libros_disponibles()

libro_encontrado = biblioteca1.buscar_libro_por_titulo("Cien años de soledad")
if libro_encontrado:
    libro_encontrado.mostrar_info()
else:
    print("Libro no encontrado.")
