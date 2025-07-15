productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
             }


stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], 
         '123FHD': [290890,32], 
         '342FHD': [444990,7],
         'GF75HD': [749990,2], 
         'UWU131HD': [349990,1], 
         'FS1230HD': [249990,0]
        }

def valida_texto(msg_input):
    while True:
        texto = input(msg_input)
        if len (texto.strip()) == 0:
            print("El texto no puede estar vacío")
            continue
        else:
            return texto
        

def buscar_por_codigo(codigo:str):
    for i in stock:
        if stock[i][0].lower() == codigo.lower():
            print("Encontrado")
            marca_encontrada = stock[i]
            marca_encontrada.insert(0,1)
            return marca_encontrada
            
def valida_numero_entero_positivo(msg_input):
    while True:
        try:
            numero = int(input(msg_input))
            if numero <= 0:
                print("Solo se permiten numeros positivos mayores a 0")
                continue
            else:
                return numero
        except ValueError:
            print("Debe ingresar valores numericos.")
            continue

def stock_marca(marca:str):
    for i in productos:
        if productos[i][0].lower() == marca.lower():
            print("Encontrada")
            marca_encontrada = productos[i]
            marca_encontrada.insert(0,i)
            return marca_encontrada


def busqueda_precio(p_min:int, p_max:int):
    for i in stock:
        if stock[i][0] >= p_min and stock[i][0] <= p_max:
            print (productos[i])


def actualizar_precio(modelo:str, p:int):
    marca_encontrada = stock_marca(buscar_por_codigo)
    if marca_encontrada != None:
        print(marca_encontrada)
        for i in stock:
            if i.upper() == marca_encontrada[0].upper():
                stock[i][0] = actualizar_precio
            else:
                print("No se encontró")

            
def menu():
    while True:
        print("**** MENÚ PRINCIPAL ****")
        print("[1] - Stock marca.")
        print("[2] - Busqueda por precio.")
        print("[3] - Actualizar precio.")
        print("[4] - Salir.")
        opcion = valida_numero_entero_positivo("Ingrese una opción: ")

        if opcion == 1:
            nombre_marca = valida_texto("Ingrese maraca a consultar: ")
            marca_encontrada = stock_marca(nombre_marca)
            if marca_encontrada == None:
                print("No se encontró la marca")
            else:
                print(f"El stock es de: {marca_encontrada["nombre_marca"]}")

        elif opcion == 2:
            p_min = valida_numero_entero_positivo("Ingrese el rango minimo de precio: ")
            p_max = valida_numero_entero_positivo("Ingrese el rango maximo de precio: ")
            busqueda_precio(p_min,p_max)

        elif opcion == 3:
            codigo_marca = valida_texto("Ingrese modelo a actualizar: ")
            nuevo_precio = valida_numero_entero_positivo("Ingrese el nuevo precio: ")
            actualizar_precio(codigo_marca,nuevo_precio)

        elif opcion == 4:
            print("PROGRAMA FINALIZADO...")
            break

        else:
            print("Debe seleccionar una opción valida [1 - 4]")
            continue

menu()

