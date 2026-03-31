def rectangle():

    base = int(input("ingrese la base: "))
    altura = int(input("Ingrese la altura: "))

    area = base*altura
    perimetro = (2*base) + (2*altura)

    print(f"Base:", base)
    print(f"Altura:", altura)
    print(f"Area:", area)
    print(f"Perimetro:", perimetro)
