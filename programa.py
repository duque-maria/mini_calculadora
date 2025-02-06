import math 

# input
print("······························")
print("Minicalculadora Guanentina")
print("······························")

print("1-- sumar (x+y)")
print("2-- restar (x-y)")
print("3-- multiplicar (x*y)")
print("4-- división (x/y)")
print("5-- potencia (x**y)")
print("6-- logaritmo (math.log(x,y))")


x = int(input("Introducir el primer numero: "))
y = int(input("Introducir el segundo numero: "))
opc = int(input("Selecciona una operación: "))

# processing
if opc == 1:
    r= (x+y)
else:
    if opc== 2:
        r= (x-y) # output
    else:
        if opc == 3:
            r= (x*y) # ouput
        else:
            if opc == 4:
                r= (x/y) # output
            else: 
                if opc == 5:
                    r= (x**y) # output
                else:
                    if opc== 6:
                        r= (math.log(x,y)) # output
                    else:
                        r= "Opción no válida" # output

# output
print("Resultado: " + str(r))