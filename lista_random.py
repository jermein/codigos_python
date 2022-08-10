edades = []

from random import randint

x = randint(0,100)

print("El numero random de x es: ", x)

y = randint(0,100)

while x > y:
    y = randint(0,100)

print("El numero random de y es: ", y)

j = 0

for i in range(x,y):
    edades.append(j)
    z = randint(0,100)
    edades[j] = z
    print(edades[j])
    j += 1
    

