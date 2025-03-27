# f = open("mi_archivo.txt", "w")

# f.write("Este es el nuevo contenido")



# for line in f.readlines():
#     print(f"Linea: {line}".replace("\n",""))

with open("mi_archivo.txt", "w") as f:
    f.write("Este es el nuevo contenidos")

