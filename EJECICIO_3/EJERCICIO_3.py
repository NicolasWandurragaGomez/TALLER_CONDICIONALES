" Ejercicio 3"


# input

Precio_costo=int(input("Digite el costo del producto: "))


# processing


if Precio_costo<=3000:
        ganancia=Precio_costo*0.15 

elif Precio_costo<=6000:
        ganancia=500

else: 
        ganancia= Precio_costo *0.25 
 

Precio_Venta= Precio_costo + ganancia

# ouput


print( " El producto tiene un Costo de $" + str( Precio_costo ) + " con una ganancia de $"  + str(ganancia) + " su precio de venta en $"  +   str (Precio_Venta) )

