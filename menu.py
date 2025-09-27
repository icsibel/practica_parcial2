from funcional import Supermercado

supermercado=Supermercado()

while True:
    print("  \n AKIRA TORIYAMA  ")
    print("1. HU00001 - tomar turno")
    print("2. HU00001 - ver turnos pendientes")
    print("3. HU00002 - atender siguiente")
    print("4. HU00003 - ver estado colita o turnitos")
    print("5. HU00004 - ver inventario")
    print("6. HU00004 - agregar artículo a inventario")
    print("7. HU00004 - dar de baja el artículo")
    print("8. Salir")
    opcion = input("Seleccione opción: ")

    match opcion:
        case "1":
            supermercado.tomar_turno()
        case "2":
            supermercado.ver_turno()
        case "3":
            supermercado.atencion_cliente()
        case "4":
            supermercado.ver_cola_pila()
        case "5":
            supermercado.mostrar_inventario()
        case "6":
            supermercado.agregar_articulo()
        case "7":
            supermercado.dar_baja()
        case "8":
            print("Saliendo...")
            break
        case _:
            print("opción inválida")

