import math
from dataclasses import dataclass

numeric= int | float

class Animal:
    def __init__(self, especie, edad, color):
        self.especie = especie
        self.edad = edad
        self.color = color

    def hacer_sonido(self):
        return f"El animal de especie {self.especie} hace un sonido"

    def describir(self):
        return f"Este es un {self.especie} {self.color} de {self.edad} años"


animal_1 = Animal(especie="perro", edad=5, color="blanco")
animal_1.hacer_sonido()  # El animal de especie perro hace un sonido

animal_1 = Animal(especie="perro", edad=5, color="blanco")
animal_1.hacer_sonido()  # El animal de especie perro hace un sonido


class Perro(Animal):
    def __init__(self, edad, color):
        super().__init__(especie="perro", edad=edad, color=color)

    def hacer_sonido(self, sonido):
        print(f"EL animal de especie{self.especie} hace {sonido}")

    def __add__(self, other):
        print("Estas tratando de añadir un perro")


class AnimalEntrenado(Animal):
    def __init__(self, nivel_de_entrenamiento, especie, edad, color="negro"):
        super().__init__(especie, edad, color)
        self.nivel_de_entrenamiento = nivel_de_entrenamiento

    def hacer_truco(self):
        if self.nivel_de_entrenamiento == 1:
            print("Dar la pata")
        if self.nivel_de_entrenamiento == 2:
            print("Hacerse el muerto")
        if self.nivel_de_entrenamiento == 3:
            print("Ir a comprar pan")


perro_1 = Perro(color="gris", edad=7)
# print(perro_1.hacer_sonido())  # Salida: El perro ladra
print(perro_1.describir())  # Salida: Este es un perro gris de 7 años


class Mascota(Animal):
    def __init__(self, nombre, especie, edad, color="negro"):
        super().__init__(especie, edad, color)
        self.nombre = nombre

    def __repr__(self):
        return f"Mascota(nombre={self.nombre}, especie={self.especie}, edad={self.edad}, color={self.color})"

    def presentar(self):
        print(f"Hola, esta es mi mascota {self.nombre}")


class MascotaEntrenada(Mascota, AnimalEntrenado):
    def __init__(self, nombre, nivel_de_entrenamiento, especie, edad, color="negro"):
        Mascota.__init__(self, nombre, especie, edad, color)
        AnimalEntrenado.__init__(self, nivel_de_entrenamiento, especie, edad, color)

    def __repr__(self):
        # Aquí incluimos el nivel de entrenamiento en la representación
        return f"MascotaEntrenada(nombre={self.nombre}, especie={self.especie}, edad={self.edad}, color={self.color}, nivel_de_entrenamiento={self.nivel_de_entrenamiento})"


perro = Animal(especie="perro", edad=5, color="negro")
bobby = Mascota(nombre="Bobby", especie="perro", edad=1, color="blanco")
# print(bobby.hacer_sonido())
# bobby.presentar()

jack = MascotaEntrenada(
    nombre="Jack", nivel_de_entrenamiento=3, especie="perro", edad=8
)
# print(jack)
# jack.hacer_truco()


class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Coordenada(x={self.x}, y={self.y})"

    def __add__(self, other):
        return Coordenada(x=self.x + other.x, y=self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distancia(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


c1 = Coordenada(3, 5)
c2 = Coordenada(4, 5)

print(c1 + c2)

print(c1 == c2)

print(c1.distancia(c2))

def sumar_numero(numeros: list[int|float]) -> float:
    return sum(numeros)

def contar_ocurrencias(palabras: list[str]) -> dict[str, int]:
    resultado = {}
    for palabra in palabras:
        resultado[palabra] = resultado.get(palabra, 0) + 1
        
    return resultado

def buscar_elemento(lista: list[int], elemento: int) -> int| None:
    try:
        return lista.index(elemento)
    except ValueError:
        return None
    
    
@dataclass(eq= True, order=True, frozen=True)
class Punto:
    x: numeric
    y: numeric
    
    def __post_init__(self):
        if self.x < 0 or self.y < 0:
            raise ValueError("Las coordenadas no pueden ser negativas")

    def __add__(self, other):
        return Punto(x=self.x + other.x, y=self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distancia(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
p1= Punto(x=3, y=8)
p2= Punto(x=4, y=5)
print(p1)
print(p1 == p2)
print(p1.distancia(p2))
print(sorted([p2, p1]))