
CANT_MP_XUNIDAD = 15 #En kg
TIEMP_XUNIDAD = 20 #En minutos -> Hacer conversión de horas a minutos en la entrada

def calcular_produccion(tiemp_disponible, TIEMP_XUNIDAD, lineas_disp, mp_disponible, CANT_MP_XUNIDAD):
    max_tiempo = (tiemp_disponible // TIEMP_XUNIDAD) * lineas_disp

    max_mp = mp_disponible // CANT_MP_XUNIDAD

    if max_tiempo < max_mp: #Faltó tiempo
        prod_obtenida = max_tiempo

    elif max_mp < max_tiempo: #Faltó materia prima
        prod_obtenida = max_mp

    else: #Son iguales
        prod_obtenida = max_tiempo
    #Materia prima
    mp_consumida = prod_obtenida * CANT_MP_XUNIDAD
    mp_restante = mp_disponible - mp_consumida
    #Tiempo -> Asi para q no haya errores por division entre 0
    if lineas_disp > 0:
        tiemp_usado = (prod_obtenida * TIEMP_XUNIDAD) / (lineas_disp * 60)
    else:
        tiemp_usado = 0.0

    return prod_obtenida, mp_consumida, mp_restante, tiemp_usado
