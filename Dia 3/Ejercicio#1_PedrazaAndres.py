def coins(sum): 
    i = 0
    coins_10 = sum // 10 
    sum %= 10 
    coins_5 = sum // 5
    sum %= 5 
    coins_1 = sum
    print("coins =", coins_1 + coins_5 + coins_10)
    counter = []
            
    for i in range(coins_10):
        counter.append("10")
    for i in range(coins_5):
        counter.append("5")
    for i in range(coins_1):
        counter.append("1")

    print(counter)

while True:
    try:
        sum = int(input("--> "))
        if sum > 0 and sum<=1000 :
            break  
        else:
            print("Introduzca un número mayor que 0 y menor que 1001.")
    except ValueError:
        print("Por favor ingrese un número entero válido.")
coins(sum)