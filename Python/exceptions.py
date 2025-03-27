# try:
#     # Código que podría generar una excepción
#     x = int("texto")
# except ValueError:
#     print("Ocurrió un error de valor.")

valor_texto = "7"
try:
    x = int(valor_texto) / 0
except ValueError:
    print("Ocurrió un error de valor.")
except ZeroDivisionError as e:
    print(f"Ocurrió una división por cero.{repr(e)}")
except (ValueError, ZeroDivisionError) as e:
    print(f"Ocurrió una división por cero.{repr(e)}")

print("Hola!")
