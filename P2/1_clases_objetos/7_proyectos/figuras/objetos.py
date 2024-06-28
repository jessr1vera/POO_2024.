from figuras import Figura, Rectangulo, Circulo, Triangulo

print("Figura base (abstracta)")
figura_base = Figura()

print("Rectangulo")
rectangulo = Rectangulo(20, 10)
rectangulo.getInfo()
print(f"Área del rectángulo: {rectangulo.calcularArea()}")

print("Circulo")
circulo = Circulo(33)
circulo.getInfo()
print(f"Área del círculo: {circulo.calcularArea()}")

print("Triangulo")
triangulo = Triangulo(70, 12)
triangulo.getInfo()
print(f"Área del triángulo: {triangulo.calcularArea()}")