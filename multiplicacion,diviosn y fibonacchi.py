n = 0
d = 0
f = 0
op = int(0)
def menu():
    print("----------------")
    print("1.Multiplicar")
    print("2.Dividir")
    print("3.Fibonacci")
    print("4.Salir")

def multiplicacion():
    c = 0
    n1 = int(input("Ingrese primer número a multiplicar: "))
    n2 = int(input("Ingrese segundo número a multiplicar: "))
    while (n2!=0):
        c=c+n1
        n2=n2-1
    print("El resultado de la multiplicacion es: ",c)

def division(n,d):
    co = 0
    re = 0
    n = int(input("Ingrese el numerador: "))
    d = int(input("Ingrese el divisor: "))
    while n>=d :
        n-= d
        re = n
        co+=1
    return("el resultado es", co, " y el sobrante es",re)
resultado = division(n, d)
print(resultado)

def fibonacci(f):
    a = 1
    b = 1
    f = int(input("Ingrese el numerador: "))
    if f == 1:
        print('0')
    elif f == 2:
        print('0','1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(f-3):
            total = a + b
            b = a
            a = total
            print("El resultado de la operacion es: ",total)
fibonacci(f)

menu()
op = int(input("Elija una opción: "))
while (op != 4):
    if (op == 1):
        multiplicacion()
    else:
        if (op == 2):
            division()
        else:
            if (op == 3):
                fibonacci()
            else:
                print("Opcion no válida")
    menu()
    op = int(input("Elija una opción: "))