import math

# Guarde este archivo en la ruta C:/users/usuario/AppData/Local/Programs/Python/Python<número_versión>/Lib
# Guarde con el mismo nombre con el que lo descargó: formas.py
# Importe como: import formas as fm, recomendado
# Creado por github.com/kev402

def perimetro_cuadrado(lado):
    return lado * 4

def area_cuadrado(lado):
    return lado ** 2

def perimetro_rectangulo(base, altura):
    return 2 * base + 2 * altura

def area_rectangulo(base, altura):
    return base * altura

def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def area_triangulo(base, altura):
    return (base * altura) / 2

def perimetro_circulo(radio):
    return 2 * math.pi * radio

def area_circulo(radio):
    return math.pi * (radio ** 2)

def perimetro_poligono_regular(lado, cantidad_lados):
    return lado * cantidad_lados

def area_poligono_regular(perimetro, apotema):
    return (perimetro * apotema) / 2

def volumen_cubo(lado):
    return lado ** 3

def volumen_prisma_rectangular(lado, altura):
    área_base = lado ** 2
    return área_base * altura

def volumen_prisma_triangular(base_triángulo, altura_triángulo, altura):
    base_prisma = (base_triángulo * altura_triángulo) / 2
    return base_prisma * altura

def volumen_cilindro(radio, altura):
    base = math.pi * (radio ** 2)
    return base * altura

def volumen_prismas_regulares(perímetro_base, apotema, altura):
    área_base = (perímetro_base * apotema) / 2
    return área_base * altura

def pirámide_triángulo(base_triángulo, altura_triángulo, altura):
    área_base = (base_triángulo * altura_triángulo) / 2
    return 1/3 * (área_base * altura)

def pirámide_cuadrado(lado, altura):
    área_base = lado ** 2
    return 1/3 (área_base * altura)

def pirámide_regular(perímetro_base, apotema, altura):
    área_base = (perímetro_base * apotema) / 2
    return 1/3 (área_base * altura)

def volumen_cono(radio, altura):
    área_base = math.pi * (radio **2)
    return 1/3 (área_base * altura)

def volumen_esfera(radio):
    return 4/3 * math.pi * (radio ** 3)