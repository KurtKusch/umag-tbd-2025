print("Hola mundo!")

x = 11 # No preocuparse del tamaño
print(x)

if x < 10: #and, or & not
    print("x es menor a 10") #Este queda dentro del IF
elif x < 10:
    print("x es mayor o igual a 10")
else:
    print("X es mayor o igual") #Este no

my_float = 3.5
my_bool = False # or True
my_str = "Hola" # String
my_none = None

my_str = 3.5

print(type(my_str))

##Ciclo WHILE###

i = 0
while i < 5:
   print (i)
   i += 1


##Ciclo FOR###

for x in range(5):
  if x < 3:
      continue
  print(x)

mi_lista = [1, "2", 4.5 ,3 ,5, 5, [1, 2, 3]]

mi_lista.append("A") # append inserta al final de la lista
mi_lista.insert(1, "B") #agrega en una posicion especificada
mi_lista.remove("B") # eliminar un elemento
mi_lista.pop(4) # ELimina un elemento en la posicion indicata
mi_lista.extend([10, 20, 30])
print(mi_lista)

print(mi_lista[::-1]) # Invierte la lista
for e in mi_lista:
    print(e)

mi_tupla = (1,2,3,4,5) #Las tuplas no se pueden modificar
print(mi_tupla[:-2])
for e in mi_tupla:
    print(e)

mi_conjunto = {1, 2, 3, 4, 5}
mi_conjunto.add((1,2))
mi_conjunto.add(9)
mi_conjunto = mi_conjunto - ({1,20,30,4})
print(mi_conjunto)
print(10 in mi_conjunto)

mi_diccionario = {"nombre": "Ariel", "edad": 21}
mi_diccionario["edad"] = 25
print(mi_diccionario.get("apellido", "desconocido")) #se puede dejar un default en caso de que no exista el get
print (mi_diccionario["edad"])
print(mi_diccionario.keys())
print(mi_diccionario.items())

for k, v in mi_diccionario.items():
    print(k, v)

for i, e in enumerate(mi_lista):
    print(i, e)

mis_numeros = [1, 4, 5, 10, 12, 15]
mis_cuadrados = [n*n for n in mis_numeros if n % 2 == 0] 
print(mis_cuadrados)

letras = ["A", "B", "C"]
conteo = {l: 0 for l in letras}
print(conteo)

mi_texto = "Hol a mundo"
palabras = mi_texto.split()
print("*".join(palabras))
nombre = "diego"

mi_fstring = f"Ariel dijo {mi_texto}.\n{2**8}"
print(mi_fstring)

def suma_numeros(n1, n2=5):
    print(n1 + n2)
suma_numeros(n1=20, n2=20)

def aplica_fn(valores, fn):
    return fn(valores)
def promedio(x):
    return sum(x) / len(x)

print(aplica_fn([1, 2, 3, 4, 5], promedio ))

def test(a, b, **kwargs):
    """
    Esta es la funcion test
    xD!
    lolazo
    :param a: Primer argumento
    :param return: nada
    """
    print(a, b, kwargs)
mi_a = {"a":1, "b":2, "c": 3, "d": 5}
test(**mi_a)