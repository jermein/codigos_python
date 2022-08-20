opcion = 0

while (opcion <= 4):
    print("elija una opcion 1.mostrar el factorial de un numero, 2.multiplicacion a base de sumas, 3.division a bas de restas, 4.fibonashi, 5,salir")
    opcion = int(input())
    if opcion == 1:
        print("digite numero a sacar facotrial")
        factorial = int(input())
        if factorial < 0:
            print("no existe este facotrial")
        else:
            c = factorial
            fact = 1
            while (factorial > 1 ):
                fact *= factorial
                factorial -= 1
            print("el factorial de", c,"es" ,fact)
    if opcion == 2:
        c = 0
        num1 = int(input("digite numero a multiplicar: "))
        num2 = int(input("digite 2 numero a multiplcar: "))
        while (num2 != 0):
            c = c + num1
            num2 = num2 - 1
        print("El resultado de la multiplicacion es: ",c)
    if opcion == 3:
        print("ingrese numerador")
        n = (int(input()))
        print("ingrese divisor")
        c = (int(input()))
        num = n
        con = 0
        while num > 0:
         con += 1
         num = num-c
        print("el numero es:",con)
    if opcion == 4:
        num3 = int(input("ingrese el numero "))
        n1, n2 = 0, 1
        count = 0     
        print("Fibonacci secuencia:")
        while count < num3:
            print(n1)
            num4 = n1 + n2
            n1 = n2
            n2 = num4
            count += 1
    if opcion == 5:
        print("saliendo......")