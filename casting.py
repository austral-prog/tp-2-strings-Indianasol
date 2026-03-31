def casting():
    precio = int(input("Ingrese un precio: "))
    descuento = float(input("Ingrese el descuento: "))
    cantidad = int(input("Ingrese una cantidad: "))

    precio_descuento= (precio - descuento)
    total = (cantidad*(precio_descuento))
    print(f"Precio:",precio)
    print(f"Descuento:",descuento)
    print (f"Precio con descuento:",precio_descuento)
    print (f"Total:",total)

