## -----------------------------
## ---- Ejercicio 1 ----
## -----------------------------

# Impresión en consola
print ("Hola Mundo")

# ---- Datos primitivos ----
#1. String
texto = "Campus"
print (texto)
print (type(texto))
#2. Int
numeroEntero = 1
print (numeroEntero)
#3. Float
numeroDecimal = 3.1
print (numeroDecimal)
#4. Double
numeroDecimalLargo = 3.141625458
print (numeroDecimalLargo)
#5. Boolean
booleano = True
print (booleano)
# ---- Entradas por parte del usuario ----
entradaUsuario = input ("Ingresa tu nombre: ")
print ("Tu nombre es: ", entradaUsuario)
# ---- Entradas por parte del usuario con definición con tipo de dato primitivo ----
entradaUsuarioNumero = input("Ingresa tu edad: ")
numeroFinal = int(entradaUsuarioNumero)
print ("Tu edad es: ", numeroFinal)
# ---- Ciclos ----
#Ciclo for
for i in range (5,10,2): #for contador in range (desde,hasta,pasos):
    print (i)
#Ciclo while
booleanito = True
while booleanito == True: #while condición_a_cumplir :
    print ("sigo vivo")
    booleanito = False
# ---- Condicionales ----
texto1 = "Campus"
if texto1 == "Campus":
    print("Soy campus")
else:
    print("No soy campus")

#Terminar con funciones y arreglos
## Desarrollado por ANDRES PEDRAZA PEÑA - 1005331114