
from typing_extensions import Self


class animal:
    especie = str
    pelaje = str
    color = str
    altura = str
    def __init__(self,especie):
        self.especie = especie
        self.pelaje()
        self.altura()
        self.color()

    def pelaje(self):
        self.pelaje = "bastante"

    def altura(self):
        self.altura= "23 cm"
    
    def color(self):
        self.color = "negro"

class felino(animal):
    tipo = str
    def __init__(self, tipo):
        self.tipo = tipo
        super().__init__(felino)
    pass
f = felino("leon")
print(f.altura)

#hacer un algoritmo para calcular la factorial
#hacer una multiplicacion a base de sumas
#divisiones con restas
#hacer la serie de fibonachi