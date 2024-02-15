# Función para calcular las longitudes posibles con un conjunto dado de monedas
def calculate_possible_leg_lengths(coins, target_height):
    # Ordenar las monedas de menor a mayor espesor
    coins.sort()
    # Inicializar las variables para almacenar las longitudes más cercanas
    closest_under = None
    closest_over = None
    # Inicializar variables para el mejor caso de cada situación
    best_under_diff = float('inf')
    best_over_diff = float('-inf')
    
    # Función recursiva para encontrar la combinación de monedas
    def find_combinations(height, index):
        nonlocal closest_under, closest_over, best_under_diff, best_over_diff
        
        # Si ya procesamos la última moneda, comparamos con los objetivos
        if index >= len(coins):
            if height <= target_height and target_height - height < best_under_diff:
                closest_under = height
                best_under_diff = target_height - height
            elif height >= target_height and height - target_height > best_over_diff:
                closest_over = height
                best_over_diff = height - target_height
            return
        
        # Llamada recursiva sin incluir la moneda actual
        find_combinations(height, index + 1)
        
        # Llamada recursiva incluyendo la moneda actual
        find_combinations(height + coins[index], index + 1)
    
    # Llamamos a la función recursiva inicialmente con altura 0 y en el índice 0
    find_combinations(0, 0)
    
    return closest_under, closest_over

# Leer y procesar la entrada
while True:
    # Leer la línea que contiene el número de tipos de monedas y mesas a diseñar
    n, t = map(int, input().split())
    if n == 0 and t == 0:
        break  # Fin de la entrada
    # Leer las siguientes n líneas para las monedas disponibles
    coins = [int(input()) for _ in range(n)]
    # Procesar cada altura de mesa t
    for _ in range(t):
        target_height = int(input())
        under, over = calculate_possible_leg_lengths(coins, target_height)
        print(f"{under} {over}")

# No es necesario ejecutar una 'main function' ya que el código está pensado para ejecutarse directamente
