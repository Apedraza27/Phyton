def contar_pares_divisibles_por_k(numeros, k):
    contador = 0
    # Recorre la lista chequeando los pares posibles
    for i in range(1, len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] < numeros[j] and (numeros[i] + numeros[j]) % k == 0:
                contador += 1
    return contador

def main():
    T = int(input("Introduce el número de casos de prueba: "))

    for _ in range(T):
        n, k = map(int, input("Introduce n y k separados por espacio: ").split())
        numeros = list(map(int, input("Introduce los números enteros separados por espacio: ").split()))

        # Valida que la longitud de la lista de numeros corresponde con el valor de n
        if len(numeros) != n:
            raise ValueError("La cantidad de números no coincide con el valor n proporcionado.")
        
        resultado = contar_pares_divisibles_por_k(numeros, k)
        print(f"El número de pares donde ai < aj, ambos distintos de n, y (ai + aj) divisibles por {k} es: {resultado}")

if __name__ == "__main__":
    main()
