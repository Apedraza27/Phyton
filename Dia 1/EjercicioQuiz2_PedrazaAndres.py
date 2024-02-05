inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 68, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

def calcular_precio(inmueble):
    if inmueble["zona"] == "A":
        precio = (inmueble["metros"] * 1000 + inmueble["habitaciones"] * 5000 + inmueble["garaje"] * 15000) * (1 - inmueble["antiguedad"] / 100)
    elif inmueble["zona"] == "B":
        precio = (inmueble["metros"] * 1000 + inmueble["habitaciones"] * 5000 + inmueble["garaje"] * 15000) * (1 - inmueble["antiguedad"] / 100) * 1.5
    else:
        ValueError("Zona no válida")
    
    return precio

def buscar_inmuebles(inmuebles, presupuesto):
    inmuebles_encontrados = []

    for inmueble in inmuebles:
        precio = calcular_precio(inmueble)
        if precio <= presupuesto:
            inmueble_encontrado = inmueble.copy()
            inmueble_encontrado["precio"] = precio
            inmuebles_encontrados.append(inmueble_encontrado)

    return inmuebles_encontrados


