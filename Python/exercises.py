# #Crea una función calculadora que reciba dos números y una operación (+, -, *, /) y retorne el resultado.

# def calculadora():
#     a= float(input("Ingrese el primer numero: "))
#     b= float(input("Ingrese el segundo numero: "))
#     operacion = input("Ingrese la operacion: ")
    
    
#     if operacion == 'suma':
#         resultado = a+b
#     elif operacion == 'resta':
#         resultado = a-b
#     elif operacion == 'multiplicacion':
#         resultado = a*b
#     elif operacion == 'division':
#         resultado = a/b
#     else:
#         resultado = "Operación no valida"
    
#     print("El resultado es" ,resultado)
    
# calculadora()



# #Escribe una función que reciba una cadena de texto y retorne un diccionario con el conteo de cada palabra.

# def contar(cadena):
#     palabras = cadena.split()
#     diccionario = {}
      
#     for palabra in palabras:
#         if palabra in diccionario:
#             diccionario[palabra] +=1
#         else:
#             diccionario[palabra] = 1
#     return diccionario

# texto= "Hola mundo como estan"
# resultado= contar(texto)
# print (resultado)

#Crea una función que determine si una palabra o frase es un palíndromo (se lee igual al derecho que al revés).

# def palindromo():
#     texto = input("Ingrese una palabra: ").replace(" "," ").lower()
    
#     if texto == texto[::-1]:
#         print("Es un palindromo.")
#     else:
#         print("No es un palindromo")
        
# palindromo()



# # Implementar una función que genere una contraseña aleatoria de una longitud dada, combinando letras, números y símbolos. Permite que el usuario elija si desea incluir mayúsculas, números o caracteres especiales.
import random
import string

def generar_contraseña():
    longitud = input("Ingrese la longitud de la contra: ")
    
    incluir_mayusculas = input ("¿Incluir mayus?")
    incluir_numeros = input("¿Incluir numeros?")
    incluir_simbolos = input("¿Incluir caracteres especiales?")
    
    mayusculas = (string.ascii_uppercase)
    


# #Crea una función que convierta una temperatura de Celsius a Fahrenheit y viceversa.

# def convertir():
#     conversion = input("¿Convertir de C a F o de F a C?").lower()
    
#     if conversion == "c":
#         celsius = float(input("Ingrese la temp C: "))
#         fahrenheit = (celsius * 9/5) + 32
#         print(f"{celsius} grados C equivalen a {fahrenheit} grados f")
#     elif conversion == "f":
#         fahrenheit = float(input("Ingrese la temp F:"))
#         celsius = (fahrenheit - 32) * 5/9
#         print(f"{fahrenheit} grados C equivalen a {celsius} grados f")
        
# convertir()
    



#Crea una función que genere la secuencia de Fibonacci hasta el número n. Implementa la versión recursiva y la versión iterativa.

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    
def generar_fibonacci_recursivo(n):
    secuencia = []
    for i in range(n):
        secuencia.append(fibonacci_recursivo(i))
    return secuencia
    
n = int(input("Ingrese la cantidad de numero para secuencia de fibonacci recursivo: "))
print(generar_fibonacci_recursivo(n))

def fibonacci_iterativo(m):
    secuencia = []
    a,b=0,1
    for i in range(n):
        secuencia.append(a)
        a, b = b , a + b
    return secuencia

m = int(input("Ingrese la cantidad de numeros para secuencia de fibonacci iterativo: "))
print(fibonacci_iterativo(n))