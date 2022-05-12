#Bucle while

import math

num=int(input("Digite un numero:"))

while num<0:
    print("Error -> Deberia ser un numero positivo")
    num=int(input("Digite un numero:"))

print(f"\nSu raiz cuadrada es:{(math.sqrt(num)):.2f}")


#ejemplo 2

i=0
while i<10:
    print("Hola mundo")
    i+=1