def calcular_definitiva(n1, n2, n3):
    nota_final = (n1 * 0.3) + (n2 * 0.3) + (n3 * 0.4)

    if nota_final < 2.0:
        mostrar = "No puede habilitar."
    elif nota_final < 3.0:
        mostrar = "Reprobó."
    elif nota_final >= 4.5:
        mostrar = "¡Felicitaciones! Aprobó con excelencia."
    else:
        mostrar = "Aprobó."

    return nota_final, mostrar


# Inicializar lista para almacenar las mejores notas    
mejores_notas = []

# Leer las notas de 5 estudiantes
for estudiante in range(1, 6):
    print(f"Ingrese las notas del estudiante {estudiante}:")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))

    # Calcular nota definitiva y obtener mostrar
    nota_final, mostrar = calcular_definitiva(n1, n2, n3)

    # Imprimir mostrar
    print(f"Nota final del estudiante {estudiante}: {nota_final}. {mostrar}")

    # Agregar la nota final a la lista de mejores notas
    mejores_notas.append(nota_final)

# Encontrar la mejor nota 
mejor_nota = mejores_notas[0]
for nota in mejores_notas[1:]:
    if nota > mejor_nota:
        mejor_nota = nota

# Mostrar la mejor nota en pantalla
print(f"La mejor nota obtenida es: {mejor_nota}")


