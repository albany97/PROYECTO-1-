def calcular_costo_jornada(mp_consumida, horas_perdidas, prod_defectuosos, accion_mantenimiento, costo_acumulado_previo):

    #establecer valores de costos unitarios
    valor_mp = 200.0
    valor_horas_perdidas = 350.0
    valor_prod_defectuosos = 80.0
    valor_mantenimiento_prev = 800.0
    valor_mantenimiento_corr = 1500.0

    #gastos de la jornada
    gasto_materia_prima = mp_consumida * valor_mp
    gasto_tiempo_perdido = horas_perdidas * valor_horas_perdidas
    gasto_penalizaciones = prod_defectuosos * valor_prod_defectuosos
    
    #gasto de mantenimiento segun la accion tomada
    gasto_mantenimiento = 0.0
    if accion_mantenimiento == 1:
        gasto_mantenimiento = valor_mantenimiento_prev
    elif accion_mantenimiento == 2:
        gasto_mantenimiento = valor_mantenimiento_corr

    total_gastos_jornada = gasto_materia_prima + gasto_tiempo_perdido + gasto_penalizaciones + gasto_mantenimiento

    nuevo_costo_total = costo_acumulado_previo + total_gastos_jornada
    return nuevo_costo_total

