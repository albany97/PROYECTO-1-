
#2. Planificacion:

#Constantes globales del modulo:
CANT_MP_XUNIDAD = 15 #En kg
TIEMP_XUNIDAD = 20 #En minutos

def planificar_jornada(mp_actual):
    print("\n------ Planificacion de la jornada ------")
    prod_planificada = int(input("Ingrese la cantidad de unidades a producir: "))
    prod_demanda = int(input("Ingrese la demanda establecida para esta jornada: "))

    tiemp_disponible = (float(input("Ingrese las horas de produccion disponibles: "))) * 60 #En minutos ya

    lineas_disp = int(input("Ingrese la cantidad de lineas de producción actualmente operativas (max. 4): "))
    while lineas_disp < 0 or lineas_disp > 4:
        lineas_disp = int(input("El numero ingresado es invalido. Ingrese la cantidad de lineas de produccion operativas: "))

    capacidad_maxima = (tiemp_disponible // TIEMP_XUNIDAD) * lineas_disp

    if lineas_disp == 0:
        print("ALERTA: No hay lineas de producción funcionales!")
        prod_planificada = 0
        continuar = False #Una especie de var. bandera para saber cuando parar o seguir

    else:
        if mp_actual < (prod_planificada * CANT_MP_XUNIDAD): 
            print("ALERTA: Materia prima insficiente para alcanzar la meta planificada!")
            print("Se aborta la operacion!")
            continuar = False

        elif tiemp_disponible < ((prod_planificada / lineas_disp) * TIEMP_XUNIDAD):
            print("ALERTA: Horas insuficientes para alcanzar la meta planificada!")
            prod_planificada = (tiemp_disponible // TIEMP_XUNIDAD) * lineas_disp
            print(f"MODIFICACION: Plan ajustado a: {prod_planificada} unidades por razones de tiempo")
            continuar = True

        elif prod_planificada > capacidad_maxima:
            print(f"ALERTA: La meta supera la capacidad física de las líneas (Máx: {capacidad_maxima} u)")
            prod_planificada = capacidad_maxima
            print(f"MODIFICACION: Plan ajustado a la capacidad máxima: {prod_planificada} unidades")
            continuar = True

        else:
            print("El plan es totalmente viable")
            continuar = True

    return prod_planificada, prod_demanda, lineas_disp, tiemp_disponible, continuar

