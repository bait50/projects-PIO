#Este es un proyecto para la clase de introduccion a l logica de programacion
#Este proyecto consiste en la venta y compra de un joyeria

stock = [
    {"nombre":"anillo de plata","precio":500,"stock":20}
    ,{"nombre":"anillo de oro","precio":1000,"stock":5}
    ,{"nombre":"anillo de diamante","precio":1500,"stock":10}
    ,{"nombre":"relog rolex","precio":5000,"stock":5}
    ,{"nombre":"relog sol","precio":10000,"stock":3}
]

carrito =[] #Esta lista se almacenaran todos los productos que el usuario compre en el stock, lo podrimos llamar el historial de compras

def mostrar_stock():
    print("---Stock disponible---")
    for i,producto in enumerate(stock, start=1):# esto no solo recorretre el stock, si no que tambien el indice de cada producto
        print("-----------------------------------------------------------------------------------")
        print(f"{i}.nombre: {producto['nombre']} || precio: {producto['precio']} || stock: {producto['stock']}")
        print("-----------------------------------------------------------------------------------")

def mostrar_carrito():
    if not carrito:
        print("--- El carrito está vacío ---")
        return

    print("---Historial de compras---")
    for i,producto in enumerate(carrito, start=1):
        print("-----------------------------------------------------------------------------------")
        print(f"{i}.nombre: {producto['nombre']} ||precio unitario: {producto['precio']} || cantidad comprada: {producto['cantidad comprada']} || precio total {calcular_total()} ")
        print("-----------------------------------------------------------------------------------")

def calcular_total():
    total = sum(producto["precio"]*producto["cantidad comprada"] for producto in carrito)
    return total

def agregar_carrito():
    mostrar_stock()
    try:
        print("-----------------------------------------------------------------------------------")
        print("---Seleciona el producto que deseas comprar ---")
        print("-----------------------------------------------------------------------------------")
        seleccion = int(input("Selecione el numero del producto que deseas comprar: "))-1 # se resta 1 para que sea el mismo numero que el indice de la lista
        cantidad = int(input("Cuantos deseas comprar: "))
        if seleccion >= 0 and seleccion < len(stock):
            if stock[seleccion]["stock"] >= cantidad:
                stock[seleccion]["stock"] -= cantidad
                producto_comprado = {
                    "nombre":stock[seleccion]["nombre"]
                    ,"precio":stock[seleccion]["precio"]
                    ,"cantidad comprada":cantidad
                }
                carrito.append(producto_comprado)
               # print(f"total a pagar: {calcular_total()}")
                print("-----------------------------------------------------------------------------------")
                print("se agrego el producto al carrito")
                print("-----------------------------------------------------------------------------------")
            else:
                print("-----------------------------------------------------------------------------------")
                print("No hay suficiente stock")
                print("-----------------------------------------------------------------------------------")
        else:
            print("la opcion selecionadv no es valida")
    except ValueError:
        print("no se pudo agregar el producto")

def finalizar_compra():
    if not carrito:
        print("--- El carrito está vacío ---")
        return
    
    mostrar_carrito()
    try:
        total = calcular_total()
        print(f"---el precio total a pagar es: {total}---")

        print("""1.efectivo
        2.Debito
        3.Credito""")
        pago = int(input("selecione el metodo de pago: "))
        if pago == 1 or pago == 2 or pago == 3:
            print("-----------------------------------------------------------------------------------")
            print("gracias por tu compra")
            print("-----------------------------------------------------------------------------------")
        else:
            print("-----------------------------------------------------------------------------------")
            print("no se pudo realizar el pago")
            print("-----------------------------------------------------------------------------------")
    except ValueError:
        print("no se pudo realizar el pago")


def menu_principal():
    while True:
        print("""Menu Principal:
        1. Mostrar productos
        2. Agregar producto al carrito
        3. Mostrar carrito
        4. Finalizar compra
        5. Salir""")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            mostrar_stock()
        elif opcion == '2':
            agregar_carrito()
        elif opcion == '3':
            mostrar_carrito()
        elif opcion == '4':
            finalizar_compra()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta nuevamente.")


menu_principal()