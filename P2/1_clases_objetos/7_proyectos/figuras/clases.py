class Figura:
    def calcularArea(self):
        pass


class Rectangulo(Figura):
    def _init_(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcularArea(self):
        return self.ancho * self.alto

    def getAncho(self):
        return self.ancho

    def setAncho(self, ancho):
        self.ancho = ancho

    def getAlto(self):
        return self.alto

    def setAlto(self, alto):
        self.alto = alto

    def getInfo(self):
        print(f"Figura con un ancho de: {self.getAncho()} y una altura de: {self.getAlto()}")


class Circulo(Figura):
    def _init_(self, radio):
        self.radio = radio

    def calcularArea(self):
        return 3.1416 * self.radio ** 2

    def getRadio(self):
        return self.radio

    def setRadio(self, radio):
        self.radio = radio

    def getInfo(self):
        print(f"Figura con un radio de: {self.getRadio()}")


class Triangulo(Figura):
    def _init_(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho

    def calcularArea(self):
        return (self.altura * self.ancho) / 2

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura

    def getAncho(self):
        return self.ancho

    def setAncho(self, ancho):
        self.ancho = ancho

    def getInfo(self):
        print(f"Figura con una altura de: {self.getAltura()} y un ancho de: {self.getAncho()}")