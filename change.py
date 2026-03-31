def change():
    gasto= float(input("ingrese su gasto: "))
    dinero_recibido = int(input("ingrese el dinero recibido: "))

    vuelto = (dinero_recibido - gasto)

    pesos= round(vuelto)
    centavos= int((vuelto - pesos)*100)
    print(f"Ingresar gasto:")
    print(gasto)
    print(f"Dinero recibido:")
    print(dinero_recibido)
    print(f"\n Vuelto")
    
    print(f"Pesos:")
    print(pesos)
    print(f"Centavos:")
    print(centavos)
