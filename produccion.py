
CANT_MP_XUNIDAD = 15 #En kg
TIEMP_XUNIDAD = 20 #En minutos -> Hacer conversión de horas a minutos en la entrada

def calcular_produccion(tiemp_disponible, TIEMP_XUNIDAD, lineas_disp, mp_actual, CANT_MP_XUNIDAD, prod_planificada):
    max_tiempo = (tiemp_disponible // TIEMP_XUNIDAD) * lineas_disp

    max_mp = mp_actual // CANT_MP_XUNIDAD

    #Evalua lo q falto para a produccion
    if max_tiempo < max_mp: #Faltó tiempo
        capacidad_tecnica = max_tiempo

    elif max_mp < max_tiempo: #Faltó materia prima
        capacidad_tecnica = max_mp

    else: #Son iguales
        capacidad_tecnica = max_tiempo

    #Para que no se pase de lo pedido por el usuario
    prod_obtenida = min(capacidad_tecnica, prod_planificada)

    #Materia prima
    mp_consumida = prod_obtenida * CANT_MP_XUNIDAD
    mp_restante = mp_actual - mp_consumida

    #Tiempo -> Asi para q no haya errores por division entre 0
    if lineas_disp > 0:
        tiemp_gastado = (prod_obtenida * TIEMP_XUNIDAD) / (lineas_disp * 60)
    else:
        tiemp_gastado = 0.0

    return prod_obtenida, mp_consumida, mp_restante, tiemp_gastado
