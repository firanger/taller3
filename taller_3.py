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

"""2.  Un Zoólogo pretende determinar el porcentaje de animales que hay en las 
siguiente categorias de edades: 0 a 1 año, de mas de 1 año y menos de 3 y 
de  3  o  mas  años.  El  zoológico  todavía  no  está  seguro  del  animal  que  va 
estudiar. Si se decide por elefantes solo tomará una muestra de 20 de ellos; 
si se decide por jirafas, tomara 15 de muestras y si son chompancés tomará 
40. """
"""
animal=input("ingrese el nombre del animal para las muestras\nelefante\njirafa\nchompancés\n ")
ceroauno=0
masdeunañoymenosdetres=0
tresomasaños=0
if (animal=="elefante"):
    for i in range(20):
        e=random.uniform(0,4)
        if (e>=0 and e<=1):
            ceroauno+=1
        if (e>1 and e<3):
            masdeunañoymenosdetres+=1
        if (e>=3):
            tresomasaños+=1
    print("el porcentaje de especimenes de edades entre 0 y 1 años es del ", (ceroauno/20)*100,"%")
    print("el porcentaje de especimenes de edades entre mayor a 1 y menor que 3 años es del ", (masdeunañoymenosdetres/20)*100, "%")
    print("el porcentaje de especimenes de edades entre 3 y mas años es del ", (tresomasaños/20)*100, "%")

if (animal=="jirafa"):
    for i in range(20):
        e=random.uniform(0,4)
        if (e>=0 and e<=1):
            ceroauno+=1
        if (e>1 and e<3):
            masdeunañoymenosdetres+=1
        if (e>=3):
            tresomasaños+=1
    print("el porcentaje de especimenes de edades entre 0 y 1 años es del ", (ceroauno/15)*100,"%")
    print("el porcentaje de especimenes de edades entre mayor a 1 y menor que 3 años es del ", (masdeunañoymenosdetres/15)*100, "%")
    print("el porcentaje de especimenes de edades entre 3 y mas años es del ", (tresomasaños/15)*100, "%")
if (animal=="chompancés"):
    for i in range(20):
        e=random.uniform(0,4)
        if (e>=0 and e<=1):
            ceroauno+=1
        if (e>1 and e<3):
            masdeunañoymenosdetres+=1
        if (e>=3):
            tresomasaños+=1
    print("el porcentaje de especimenes de edades entre 0 y 1 años es del ", (ceroauno/40)*100,"%")
    print("el porcentaje de especimenes de edades entre mayor a 1 y menor que 3 años es del ", (masdeunañoymenosdetres/40)*100, "%")
    print("el porcentaje de especimenes de edades entre 3 y mas años es del ", (tresomasaños/40)*100, "%")  
"""


"""3. Una empresa se requiere calcular el salario semanal de cada uno de los n 
obreros que laboran en ella. El salario se obtiene de la siguiente forma: 
a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora 
b. Si  trabaja  mas  de  40  horas  se  le  paga  $20  por  cada  una  de 
lasprimeras 40 horas y $25 por cada hora extra.""" 
"""
num_trabajadores=int(input("ingrese el numero de trabajadores "))
trabajadores=[]
for i in range(num_trabajadores):
    print("ingrese el numero de horas trabajadas del obrero numero", (i+1))
    trabajadores.append(int(input()))

for f in range(len(trabajadores)):
    if (trabajadores[f]<=40):
        trabajadores[f]=(trabajadores[f]*20)
    if (trabajadores[f]>40):
         trabajadores[f]=(40*20)+((trabajadores[f]-40)*25)
for h in range(len(trabajadores)):
    print("la paga por las horas trabajadas del obrero numero ", h, " es: ", trabajadores[h])
    print("por alguna razon en el if donde hay horas menores a 40 no lo multiplica por 20 ")
"""
"""4. Calcular  el  promedio  de  edades  de  hombres,  mujeres  y  de  todo  un  grupo 
de alumnos. """
"""
hombres=int(input ("ingrese el numero de hombres "))
mujeres=int(input ("ingrese el numero de mujeres "))
promediohombres=0
promediomujeres=0
promedioalumnos=0
for i in range(hombres):
    print("ingrese la edad del hombre numero ", (i+1))
    a=int(input (""))
    promediohombres+=a
for i in range(mujeres):
    print("ingrese la edad de la mujer numero ", (i+1))
    a=int(input (""))
    promediomujeres+=a

print("el promedio de edad en los hombres es :", promediohombres/hombres)
print("el promedio de edad de las mujeres es :", promediomujeres/hombres)
print("el promedio de edad en el grupo de alumnos es :", (promediohombres+promediomujeres)/(hombres+mujeres))"""

"""5. Encontrar el menor valor de un conjunto de n números dados """
"""
numeros=int(input("ingrese el numero de numeros "))
lista=[]
for i in range(numeros):
    print("ingrese el numero en la posicion ",(i+1))
    lista.append(int(input("")))
print("el numero menor del conjunto es: ", min(lista))
"""