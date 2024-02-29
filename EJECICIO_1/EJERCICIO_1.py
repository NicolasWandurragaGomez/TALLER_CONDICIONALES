import math

# input

X= int(input("digite una cordenada X: "))
Y= int(input("digite una cordenada Y: "))

#  processing and output

if X == 0:
    if Y == 0:
        print("La cordenada (" + str(X) + ", " + str(Y) + ") esta en el origen")
    else:
        print("La cordenada (" + str(X) + ", " + str(Y) + ") esta en el eje Y")
elif Y == 0:
    print("La cordenada (" + str(X) + ", " + str(Y) + ") esta en el eje X")
elif X > 0:
    if Y > 0:
        print("La cordenada (" + str(X) + ", " + str(Y) + ") esta en el cuadrante 1")
    else:
        print("La cordenada (" + str(X) + ", " + str(Y) + ") esta en el cuadrante 4")
elif Y < 0:
    print("La cordenada (" + str(X) + ", " + str(Y) + ") esta en el cuadrante 3")
else:
    print("La cordenada (" + str(X) + ", " + str(Y) + ") esta en el cuadrante 2")
