
import random

def incidencia_falta_de_materia_prima(costo_acumulado, produccion_pendiente, horas_perdidas):
    print("AVISO DE INCIDENCIA: Hay falta de materia prima en el proceso de produccion. No hay suficiente inventario para terminar.")
    print("1. Comprar materia prima (150$ en costos extras).")
    print("2. Bajar la meta de produccion.")
    print("3. Cancelar la produccion.")

    while True:
        opcion = input("Seleccione una opcion (1, 2 o 3): ")
        if opcion == "1" or opcion == "2" or opcion == "3":
            break
        print("Opcion invalida. Por favor seleccione una opcion valida (1, 2 o 3).")

    if opcion == "1":
        costo_acumulado += 150
        horas_perdidas += 0
        print("Has comprado la materia prima, el costo acumulado ahora es de:", costo_acumulado)
    elif opcion == "2":
        produccion_pendiente -= 1
        horas_perdidas += 0
        print("Has bajado la meta de produccion, la produccion pendiente ahora es de:", produccion_pendiente)
    else:
        print("Has cancelado la produccion.")
        horas_perdidas += 0

    return costo_acumulado, produccion_pendiente, horas_perdidas


def incidencia_falla_de_maquinaria(costo_acumulado, horas_perdidas, prod_defectuosa):
    print("AVISO DE INCIDENCIA: Hay una falla en la maquinaria. Se han perdido horas de producción.")
    print("1. Reparar la maquinaria (200$ en costos extras).")
    print("2. Continuar con la producción, pero habrá productos defectuosos.")
    print("3. Cancelar la producción. Se registrarán las horas perdidas.")

    while True:
        opcion = input("Seleccione una opcion (1, 2 o 3): ")
        if opcion == "1" or opcion == "2" or opcion == "3":
            break
        print("Opcion invalida. Por favor seleccione una opcion valida (1, 2 o 3).")

    if opcion == "1":
        costo_acumulado += 200
        horas_perdidas += 0
        print("Has reparado la maquinaria, el costo acumulado ahora es de:", costo_acumulado)
    elif opcion == "2":
        prod_defectuosa += 5
        horas_perdidas += 0
        print("Has decidido continuar con la producción, pero habrá productos defectuosos. Productos defectuosos: ", prod_defectuosa)
    elif opcion == "3":
        horas_perdidas += 2
        print("Has cancelado la producción. Se registrarán las horas perdidas. Horas perdidas: ", horas_perdidas)

    return costo_acumulado, horas_perdidas, prod_defectuosa


def problema_de_calidad(costo_acumulado, produccion_pendiente, desperdicio, horas_perdidas):
    print("AVISO DE INCIDENCIA: Hay un problema de calidad en la materia prima.")
    print("1. Rechazar la materia prima y buscar un proveedor alternativo (100$ en costos extras).")
    print("2. Aceptar la materia prima y asumir el desperdicio (50$ en costos extras).")
    print("3. Cancelar el lote actual por control de calidad.")

    while True:
        opcion = input("Seleccione una opcion (1, 2 o 3): ")
        if opcion == "1" or opcion == "2" or opcion == "3":
            break
        print("Opcion invalida. Por favor seleccione una opcion valida (1, 2 o 3).")

    if opcion == "1":
        costo_acumulado += 100
        print("Has rechazado la materia prima y buscado un proveedor alternativo. El costo acumulado ahora es de:", costo_acumulado)
    elif opcion == "2":
        desperdicio = produccion_pendiente * 0.1  
        produccion_pendiente -= desperdicio
        costo_acumulado += 50
        print("Has aceptado la materia prima y asumido el desperdicio. El costo acumulado ahora es de:", costo_acumulado)
    elif opcion == "3":
        produccion_pendiente -= 1
        print("Has cancelado el lote actual por control de calidad. La produccion pendiente ahora es de:", produccion_pendiente)

    horas_perdidas += 0

    return costo_acumulado, produccion_pendiente, desperdicio, horas_perdidas


def incidencia_perdida_de_tiempo(horas_utilizadas, horas_perdidas, costo_acumulado):
    print("AVISO DE INCIDENCIA: Se produjo un retraso imprevisto en el proceso de producción.")
    print("1. Buscar personal de apoyo para acelerar el proceso.")
    print("2. Extender el turno de trabajo para recuperar el tiempo perdido y pagar horas extras (50$ en costos extras).")
    print("3. Declarar el resto del día como tiempo perdido y asumir la pérdida de horas.")

    while True:
        opcion = input("Seleccione una opcion (1, 2 o 3): ")
        if opcion == "1" or opcion == "2" or opcion == "3":
            break
        print("Opcion invalida. Por favor seleccione una opcion valida (1, 2 o 3).")

    if opcion == "1":
        costo_acumulado += 100
        horas_perdidas += 0
        print("Has buscado personal de apoyo para acelerar el proceso. El costo acumulado ahora es de:", costo_acumulado)
    elif opcion == "2":
        horas_perdidas -= 2
        costo_acumulado += 50
        print("Has extendido el turno de trabajo para recuperar el tiempo perdido. El costo acumulado ahora es de:", costo_acumulado)
    elif opcion == "3":
        horas_perdidas += 2
        print("Has declarado el resto del día como tiempo perdido y asumido la pérdida de horas. Horas perdidas:", horas_perdidas)

    return horas_utilizadas, horas_perdidas, costo_acumulado


def simular_incidencia_aleatoria(costo_acumulado, produccion_pendiente, horas_utilizadas, horas_perdidas, calidad, desperdicio, prod_defectuosa):
    selector = random.randint(1, 4)
    if selector == 1:
        print("Se ha producido una incidencia de falta de materia prima.")
        costo_acumulado, produccion_pendiente, horas_perdidas = incidencia_falta_de_materia_prima(costo_acumulado, produccion_pendiente, horas_perdidas)
    elif selector == 2:
        print("Se ha producido una incidencia de falla de maquinaria.")
        costo_acumulado, horas_perdidas, prod_defectuosa = incidencia_falla_de_maquinaria(costo_acumulado, horas_perdidas, prod_defectuosa)
    elif selector == 3:
        print("Se ha producido un problema de calidad en la materia prima.")
        costo_acumulado, produccion_pendiente, desperdicio, horas_perdidas = problema_de_calidad(costo_acumulado, produccion_pendiente, desperdicio, horas_perdidas)
    elif selector == 4:
        print("Se ha producido una incidencia de pérdida de tiempo.")
        horas_utilizadas, horas_perdidas, calidad, costo_acumulado = incidencia_perdida_de_tiempo(horas_utilizadas, horas_perdidas, calidad, costo_acumulado)
    return costo_acumulado, produccion_pendiente, horas_utilizadas, horas_perdidas, calidad, desperdicio, prod_defectuosa
