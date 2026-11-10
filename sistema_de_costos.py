def calcular_costo_jornada(mp_consumida, tiemp_gastado, prod_defectuosa, costo_acumulado):

    #establecer valores de costos unitarios
    valor_mp = 200.0
    valor_tiemp_gastado = 350.0
    valor_prod_defectuosos = 80.0

    #gastos de la jornada
    gasto_materia_prima = mp_consumida * valor_mp
    gasto_tiempo_perdido = tiemp_gastado * valor_tiemp_gastado
    gasto_penalizaciones = prod_defectuosa * valor_prod_defectuosos

    total_gastos_jornada = gasto_materia_prima + valor_tiemp_gastado + gasto_penalizaciones

    costo_acumulado = costo_acumulado + total_gastos_jornada
    return costo_acumulado

