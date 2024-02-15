# Definir la función que genera la secuencia de Fibonacci
def fibonacci(n):
    # Inicializar los primeros dos términos de la secuencia
    a, b = 0, 1
    # Iterar hasta el término n
    for i in range(n):
        # Imprimir el término actual
        print(a)
        # Actualizar los términos a y b
        a, b = b, a + b

print("¡Bienvenido al generador de la Secuencia de Fibonacci!")

# Ejecutar el programa repetidamente hasta que el usuario ingrese cero
while True:
    # Solicitar al usuario ingresar un valor entero "n"
    n = input("Ingrese un valor entero para n (o 0 para salir): ")
    try:
        n = int(n)
        if n < 0:
            print("El valor de n debe ser un número entero positivo.")
            continue
    except ValueError:
        print("El valor de n debe ser un número entero positivo.")
        continue
    # Mostrar la secuencia de Fibonacci hasta el enésimo término ingresado por el usuario
    fibonacci(n)
    # Preguntar si el usuario desea continuar o salir
    choice = input("¿Desea continuar? (S/N): ")
    if choice.lower() == "n":
        break

print("¡Gracias por usar el generador de la Secuencia de Fibonacci!")

