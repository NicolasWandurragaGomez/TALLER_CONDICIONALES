"ejercicio 2"





# input




ingresos=int(input("Digite sus ingresos: "))


# processing 

if ingresos<945200:
    print("No puede hacer el prestamo ya que sus ingresos son menores a $945200")


if ingresos>=945200:
    deudas=int(input("Tiene alguna deuda:SI TIENE Digite (1),SI NO TIENE Digite (2): "))
    SN=deudas
   
if SN == (1):
    print("No puede hacer el prestamo ya que tiene deudas ")
else:
     SN== (2)
     print("Puede hacer el presamo ya que no tiene deudas y sus ingresos son mayores a $945200")
 