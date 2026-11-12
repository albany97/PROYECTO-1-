def panel_estado(
    prod_planificada,
    prod_obtenida,
    prod_pend,
    mp_actual,
    tiemp_disponible,
    tiemp_gastado,
    horas_perdidas,
    prod_defectuosa,
    porc_buenos,
    costo_acumulado,
    eficiencia_jornada,
):
    print("\n=========================================")
    print("           ESTADO DE LA PLANTA           ")
    print("=========================================")
    print(f"Producción planificada: {prod_planificada}")
    print(f"Producción realizada:   {prod_obtenida}")
    print(f"Producción pendiente:   {prod_pend}")
    print(f"Materia prima:          {mp_actual} kg")
    print(f"Horas disponibles:      {round((tiemp_disponible / 60), 2)}")
    print(f"Horas utilizadas:       {round(tiemp_gastado, 2)}")
    print(f"Horas perdidas:         {round(horas_perdidas, 2)}")
    print(f"Productos defectuosos:  {prod_defectuosa}")
    print(f"Calidad:                {round(porc_buenos, 1)}%")
    print(f"Costo acumulado:        {round(costo_acumulado, 2)}$")
    print(f"Eficiencia:             {round(eficiencia_jornada, 2)}%")
    print("=========================================\n")



def informe_final(
    nombre_planta, 
    nombre_supervisor,
    prod_tot_plan, 
    prod_tot_real,
    defectos_tot, 
    desperdicio_tot,
    costo_total_acumulado, 
    calidad_promedio,
    eficiencia_promedio
):
  if prod_tot_plan > 0:
    cumplimiento_total = (prod_tot_real / prod_tot_plan) * 100
  else:
    cumplimiento_total = 100

  print("\n=========================================")
  print("               INFORME FINAL             ")
  print("=========================================")
  print(f"Planta: {nombre_planta}")
  print(f"Supervisor: {nombre_supervisor}")
  print(f"Producción planificada : {round(prod_tot_plan, 1)}")
  print(f"Producción realizada   : {round(prod_tot_real, 1)}")
  print(f"Total Defectuosos      : {round(defectos_tot, 1)}")
  print(f"Desperdicio Acumulado  : {round(desperdicio_tot, 1)}")
  print(f"Costo Total Acumulado  : ${round(costo_total_acumulado, 2)}")
  print(f"Eficiencia Promedio    : {round(eficiencia_promedio, 1)}%")
  print("-----------------------------------------")

  if cumplimiento_total >= 95 and calidad_promedio >= 90:
    resultado = "PLAN DE PRODUCCIÓN CUMPLIDO EXITOSAMENTE"
  elif cumplimiento_total >= 75:
    resultado = "CUMPLIMIENTO PARCIAL DEL PLAN"
  elif calidad_promedio < 80:
    resultado = "CRÍTICO POR PROBLEMAS DE CALIDAD"
  else:
    resultado = "CRÍTICO POR NO CULMINAR"

  print(f"RESULTADO: {resultado}")
  print("=========================================\n")