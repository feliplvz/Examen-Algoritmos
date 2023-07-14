import os

PRECIO_PLATINUM = 120000
PRECIO_GOLD = 80000
PRECIO_SILVER = 50000

ASIENTOS_DISPONIBLES = [True] * 100

COMPRADORES = []


def mostrar_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("╔═══════════════════════════════════════════════════╗")
    print("║             Venta de Entradas                     ║")
    print("╟───────────────────────────────────────────────────╢")
    print("║  Seleccione una de las siguientes opciones:       ║")
    print("║                                                   ║")
    print("║  1. Comprar entrada                               ║")
    print("║  2. Mostrar asientos disponibles                  ║")
    print("║  3. Ver listado de compradores                    ║")
    print("║  4. Mostrar ganancias totales                     ║")
    print("║  5. Salir del programa                            ║")
    print("╚═══════════════════════════════════════════════════╝")
    opcion = int(input("Ingrese una opción: "))
    return opcion


def comprar_entrada():
    os.system("cls" if os.name == "nt" else "clear")
    mostrar_asientos_disponibles()
    cantidad_entradas = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
    if not (1 <= cantidad_entradas <= 3):
        print("Cantidad inválida. Intente nuevamente.")
        return

    print("Precios de las entradas:")
    print(f"Platinum: ${PRECIO_PLATINUM} (Del 1 al 20)")
    print(f"Gold: ${PRECIO_GOLD}")
    print(f"Silver: ${PRECIO_SILVER}")

    asientos = []
    for i in range(cantidad_entradas):
        asiento = int(input(f"Ingrese el número de asiento #{i + 1} (1-100): "))
        if not (1 <= asiento <= 100):
            print("Asiento inválido. Intente nuevamente.")
            return
        if not ASIENTOS_DISPONIBLES[asiento - 1]:
            print("El asiento seleccionado no está disponible. Intente nuevamente.")
            return
        asientos.append(asiento)


    print("\n1. Comprar")
    print("2. Volver al menú anterior")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        rut = input("Ingrese el RUT del comprador (8 dígitos): ")
        if len(rut) != 8 or not rut.isdigit():
            print("RUT inválido. Debe tener exactamente 8 dígitos. Intente nuevamente.")
            return
        for asiento in asientos:
            tipo_entrada = determinar_tipo_entrada(asiento)
            precio_entrada = determinar_precio_entrada(tipo_entrada)
            COMPRADORES.append({'rut': rut, 'asiento': asiento, 'tipo_entrada': tipo_entrada,
                                'precio_entrada': precio_entrada})
            ASIENTOS_DISPONIBLES[asiento - 1] = False
        print("¡Compra realizada correctamente!")
    elif opcion == 2:
        return
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


def determinar_tipo_entrada(asiento):
    if 1 <= asiento <= 20:
        return "Platinum"
    elif 21 <= asiento <= 50:
        return "Gold"
    elif 51 <= asiento <= 100:
        return "Silver"


def determinar_precio_entrada(tipo_entrada):
    if tipo_entrada == "Platinum":
        return PRECIO_PLATINUM
    elif tipo_entrada == "Gold":
        return PRECIO_GOLD
    elif tipo_entrada == "Silver":
        return PRECIO_SILVER


def mostrar_asientos_disponibles():
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                       Asientos Disponibles                   ║")
    print("╟──────────────────────────────────────────────────────────────╢")

    for i, disponible in enumerate(ASIENTOS_DISPONIBLES, start=1):
        if i % 10 == 1:
            print("║ ", end="")
        if disponible:
            print(f" \033[1;32m{i:2d}  \033[0m", end=" ")
        else:
            print(f" \033[0;31m{i:2d}  \033[0m", end=" ")
        if i % 10 == 0:
            print(" ║")
    if (i + 1) % 10 != 0:
        print("║")

    print("╚══════════════════════════════════════════════════════════════╝")


def mostrar_listado_compradores():
    print("╔═══════════════════════════════════════════════════╗")
    print("║             Listado de Compradores                ║")
    print("╟───────────────────────────────────────────────────╢")
    compradores_ordenados = sorted(COMPRADORES, key=lambda x: x['rut'])
    for comprador in compradores_ordenados:
        print(f"║  RUT: {comprador['rut']}, Asiento: {comprador['asiento']}, "
              f"Tipo de entrada: {comprador['tipo_entrada']}, Precio de entrada: ${comprador['precio_entrada']}")
    print("╚═══════════════════════════════════════════════════╝")


""" def mostrar_ganancias_totales():
    print("╔═══════════════════════════════════════════════════╗")
    print("║               Ganancias Totales                   ║")
    print("╟───────────────────────────────────────────────────╢")

    total_ventas = len(COMPRADORES)
    ganancias_totales = 0
    tipo_entradas_vendidas = {'Platinum': 0, 'Gold': 0, 'Silver': 0}

    for comprador in COMPRADORES:
        ganancias_totales += comprador['precio_entrada']
        tipo_entradas_vendidas[comprador['tipo_entrada']] += 1

    for tipo_entrada, cantidad in tipo_entradas_vendidas.items():
        print(f"║  Tipo de entrada: {tipo_entrada}  |      Cantidad: {cantidad}, "
              f"Ganancias totales: ${cantidad * determinar_precio_entrada(tipo_entrada)}")

    print(f"║  Cantidad de entradas vendidas: {total_ventas}")
    print(f"║  Ganancias totales: ${ganancias_totales}")
    print("╚═══════════════════════════════════════════════════╝") """

def mostrar_ganancias_totales():
    print("╔════════════════════════════════════════════════════════════════════════╗")
    print("║                           Ganancias Totales                            ║")
    print("╟────────────────────────────────────────────────────────────────────────╢")

    total_ventas = len(COMPRADORES)
    ganancias_totales = 0
    tipo_entradas_vendidas = {'Platinum': 0, 'Gold': 0, 'Silver': 0}

    for comprador in COMPRADORES:
        ganancias_totales += comprador['precio_entrada']
        tipo_entradas_vendidas[comprador['tipo_entrada']] += 1

    for tipo_entrada, cantidad in tipo_entradas_vendidas.items():
        ganancias = cantidad * determinar_precio_entrada(tipo_entrada)
        print(f"║  Tipo de entrada: {tipo_entrada:<9} | Cantidad: {cantidad:<6} | "
              f"Ganancias: ${ganancias:<12}")

    print(f"║  Cantidad de entradas vendidas: {total_ventas:<13} | "
          f"Ganancias totales: ${ganancias_totales:<18}")
    print("╚════════════════════════════════════════════════════════════════════════╝")



def main():
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            comprar_entrada()
        elif opcion == 2:
            mostrar_asientos_disponibles()
            input("Presione enter para continuar: ")
        elif opcion == 3:
            mostrar_listado_compradores()
            input("Presione enter para continuar: ")
        elif opcion == 4:
            mostrar_ganancias_totales()
            input("Presione enter para continuar: ")
        elif opcion == 5:
            print("╔════════════════════════════════════════════════════╗")
            print("║                                                    ║")
            print("║        ¡Gracias por utilizar el sistema!           ║")
            print("║                                                    ║")
            print("║         Programa creado por Felipe Lopez           ║")
            print("║               13 de julio del 2023                 ║")
            print("║                                                    ║")
            print("╚════════════════════════════════════════════════════╝")
            break


if __name__ == "__main__":
    main()
