def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    nombre= input("Ingrese su nombre completo:")
    email = input("ingrese su mail:")
    nota1= int(input("ingrese una nota:"))
    nota2= int(input("ingrese una nota:"))
    nota3= int(input("ingrese una nota:"))


    multilinea = """========================
    FICHA DEL ALUMNO
========================"""
    
    print(multilinea)
    nombre_mayuscula= nombre.strip().title()

    print(f"Nombre:",nombre_mayuscula)
    print(f"Email:",email.lower())
    print(f"Caracteres en nombre:", len(nombre_mayuscula))

    espacio = nombre_mayuscula.find(" ")
    iniciales = nombre_mayuscula[0] + nombre_mayuscula[espacio + 1]
    print(f"Iniciales: {iniciales}")

    nombre= nombre_mayuscula[:espacio].lower()
    apellido=nombre_mayuscula[espacio + 1:].lower()
    print(f"Usuario:", apellido + "." + nombre)

    email_valido = "@" in email
    print(f"Email valido:", email_valido)

    arroba= email.find("@")
    dominio= email[arroba + 1:].lower()
    print(f"Dominio:", dominio)

    archivo= nombre_mayuscula.replace(" ", "_")
    print(f"Nombre para archivo:", archivo)

    cantidad= nombre_mayuscula.lower().count("a")
    print(f"Cantidad de a:", cantidad)

    codigo= nombre_mayuscula[::-1].upper()
    print(f"Codigo secreto:", codigo)

    print(f"Nota 1:", nota1)
    print(f"Nota 2:", nota2)
    print(f"Nota 3:", nota3)

    suma= nota1 + nota2 + nota3
    promedio=suma/3
    entero= suma//3
    print(f"Suma:", suma)
    print(f"Promedio:", promedio)
    print(f"Promedio entero:", entero)
    
    print("=" * 24)
    
ficha()
