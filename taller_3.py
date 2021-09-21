import random
""" 
UNIVERSIDAD DE LA COSTA CUC 
FUNDAMENTOS ALGORÍTMICOS 
TALLER DE CICLOS PARA 
PROFESOR: ING.  ROBERTO MORALES  
  
"""
 
 
"""
Realice los procedimientos que den solución a los siguientes ejercicios. 
1. El departamento de Seguridad de Transito de Barranquilla, desea saber de 
los n autos que entrar a la ciudad, cuantos entran con calcomanía de cada 
color.  Conociendo  el  último  placa  de  la  placa  de  cada  automóvil  se  puede 
determinar el color de la calcomanía utilizando la siguiente relación:"""
"""
autos = int(input("ingrese el numero de autos "))
amarillo=0
rosa=0
verde=0
azul=0
roja=0
for i in range (autos):
    print("ingrese el ultimo digito de la placa del auto numero: ",(i+1))
    placa = int(input(""))
    if (placa == 1 or placa == 2):
        amarillo+=1
    if (placa == 3 or placa == 4):
        rosa+=1
    if (placa == 5 or placa == 6):
        roja+=1
    if (placa == 7 or placa == 8):
        verde+=1
    if (placa == 9 or placa == 0):
        azul+=1
print("el numero de autos amarillos que entraron es: ", amarillo)
print("el numero de autos rosa que entraron es: ", rosa)
print("el numero de autos roja que entraron es: ", roja)
print("el numero de autos verde que entraron es: ", verde)
print("el numero de autos azul que entraron es: ", azul)"""