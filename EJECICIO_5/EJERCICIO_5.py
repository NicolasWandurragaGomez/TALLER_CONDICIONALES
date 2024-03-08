# input

metros_gastados=int(input("Digite los metros de agua: "))

# processing

if metros_gastados <=50:
    Algo=0
elif metros_gastados >50 and metros_gastados <=200:
    Algo=2000 * (metros_gastados - 50)
else:
    metros_gastados >200
    Algo=3000 * (metros_gastados - 50)

costo_agua=10000 + Algo

# ouput

print("El costo del agua es", costo_agua)