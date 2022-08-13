class celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.prendido = False
    
    def prender(self):
        self.prendido = True
        print("El", self.marca, self.modelo, "se ha arrancado")
    
    def apagado(self):
        self.prendido = False
        print("El", self.marca, self.modelo, "se ha apagado")

samsung= celular("samsug", "model s10")
iphone = celular("iphone", "model 13")

print(type(samsung))
print(type(iphone))
print(samsung.marca, samsung.modelo)
print(iphone.marca, iphone.modelo)

samsung.prender()
iphone.prender()

print(samsung.prender)
print(iphone.prender)

samsung.apagado()
iphone.apagado()
print(samsung.apagado)
print(iphone.apagado)
