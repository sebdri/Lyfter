def ordenar_canciones(archivo_entrada, archivo_salida):
    with open(archivo_entrada, "r", encoding="utf-8") as file:
        canciones = file.readlines()

    canciones.sort()

    with open(archivo_salida, "w", encoding="utf-8") as file:
        file.writelines(canciones)

    print("Canciones ordenadas correctamente.")


ordenar_canciones("canciones.txt", "canciones_ordenadas.txt")