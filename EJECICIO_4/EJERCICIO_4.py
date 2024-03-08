import math

# input

peso=int(input("Digite su peso: "))

altura=float(input("Digite su altura: "))

# processing

imc= peso / altura**2


if imc< 16:
    print("Criterio de ingreso al hospital ")

elif imc> 16 and imc <17:
    print("Usted tiene infrapeso ")

elif imc > 17 and imc <18:
    print("Usted tiene bajo peso ")

elif imc > 18 and imc < 25:
    print("Usted tiene un peso normal (saludable)")

elif imc >25 and imc < 30:
    print("Usted tiene Sobrepeso (obesidad de grado I)")

elif imc > 30 and imc > 35:
    print("Usted tiene Sobrepeso Cronico (obesidad de grado II)")

elif imc > 30 and imc < 35:
    print("Usted tiene Obecidad Premorbida (obesidad de grado III)")

elif imc > 40:
    print("Usted tiene Obecidad Morbida (obesidad de grado IV)")