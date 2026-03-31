def change():
    gasto= float(input("ingrese su gasto: "))
    dinero_recibido = int(input("ingrese el dinero recibido: "))

    vuelto = (dinero_recibido - gasto)

    pesos= int(vuelto)
    centavos= int(round((vuelto - pesos)*100))
    print(f"Ingresar gasto:")
    print(gasto)
    print(f"Dinero recibido")
    print(dinero_recibido)
    print(f"\nVuelto\n")
    
    print(f"Pesos:")
    print(int(vuelto))
    print(f"Centavos:")
    print(centavos)
