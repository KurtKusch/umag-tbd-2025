import random
import string

# Función de la calculadora
def calculadora():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = a + b
    elif operacion == '-':
        resultado = a - b
    elif operacion == '*':
        resultado = a * b
    elif operacion == '/':
        if b != 0:
            resultado = a / b
        else:
            resultado = "Error"
    else:
        resultado = "Operación no válida"
    
    print("El resultado es:", resultado)

# Función para contar palabras con numeración
def contar_palabras(texto):
    palabras = texto.split()
    conteo = {palabra: i+1 for i, palabra in enumerate(palabras)}
    return conteo

# Función para verificar si una palabra es un palíndromo
def palindromo():
    texto = input("Ingrese una palabra o frase: ").replace(" ", "").lower()
    if texto == texto[::-1]:
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

# Función para generar una contraseña aleatoria
def generar_contraseña(longitud, mayusculas, numeros, especiales):
    minúsculas = string.ascii_lowercase
    mayúsculas = string.ascii_uppercase if mayusculas else ''
    dígitos = string.digits if numeros else ''
    símbolos = string.punctuation if especiales else ''
    
    caracteres = minúsculas + mayúsculas + dígitos + símbolos

    if not caracteres:
        raise ValueError("Debe incluir al menos un tipo de carácter en la contraseña.")

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Función para generar la secuencia de Fibonacci (recursivo)
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

# Función para contar vocales y consonantes
def contar_vocales_consonantes(cadena):
    vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    num_vocales = sum(1 for letra in cadena if letra in vocales)
    num_consonantes = sum(1 for letra in cadena if letra in consonantes)

    return num_vocales, num_consonantes

# Función para adivinar el número
def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("He elegido un número entre 1 y 100.\n")

    while not adivinado:
        try:
            intento = int(input("Introduce tu número: "))
            intentos += 1

            if intento < numero_secreto:
                print("El numero es mayor.\n")
            elif intento > numero_secreto:
                print("El numero es menor.\n")
            else:
                adivinado = True
                print(f"Adivinaste el numero {numero_secreto} en {intentos} intentos.")

        except ValueError:
            print(" Ingresa un numero valido.\n")

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Calculadora")
        print("2. Contar palabras")
        print("3. Verificar palíndromo")
        print("4. Generar contraseña aleatoria")
        print("5. Generar secuencia de Fibonacci (recursivo)")
        print("6. Contar vocales y consonantes")
        print("7. Adivina el número")
        print("8. Salir")

        opcion = input("Elija una opción (1-8): ")

        if opcion == '1':
            calculadora()
        elif opcion == '2':
            texto = input("Ingrese un texto: ")
            resultado = contar_palabras(texto)
            print("\nNumeración de palabras:")
            for palabra, numero in resultado.items():
                print(f"{palabra}: {numero}")
        elif opcion == '3':
            palindromo()
        elif opcion == '4':
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            usar_mayusculas = input("¿Incluir mayúsculas? (s/n): ").strip().lower() == 's'
            usar_numeros = input("¿Incluir números? (s/n): ").strip().lower() == 's'
            usar_especiales = input("¿Incluir caracteres especiales? (s/n): ").strip().lower() == 's'
            contraseña_generada = generar_contraseña(longitud, usar_mayusculas, usar_numeros, usar_especiales)
            print(f"\n Contraseña generada: {contraseña_generada}")
        elif opcion == '5':
            n = int(input("Ingrese la cantidad de números para la secuencia de Fibonacci: "))
            print(generar_fibonacci_recursivo(n))
        elif opcion == '6':
            cadena = input("Ingrese una cadena: ")
            vocales, consonantes = contar_vocales_consonantes(cadena)
            print(f"\nVocales: {vocales}")
            print(f"Consonantes: {consonantes}")
        elif opcion == '7':
            adivina_el_numero()
        elif opcion == '8':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
menu()
