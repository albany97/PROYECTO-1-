#11. Evaluacion de la jornada

def estado_jornada(prod_planificada, prod_obtenida, calidad, eficiencia, prod_defectuosa, prod_real):
  print("========================================")
  print("        EVALUACIÓN DE LA JORNADA        ")
  print("========================================")
  
  #Cumplimiento / produccion
  if prod_planificada > 0:
    porc_cumplimiento = round((prod_obtenida / prod_planificada) * 100, 2)
  else:
    porc_cumplimiento = 0.0

  if porc_cumplimiento >= 95:
    print("Producción: Cumplida exitosamente.")
  elif porc_cumplimiento >= 75:
    print("Producción: Estándar.")
  else:
    print("Producción: No cumplida.")
    
  #Calidad
  if calidad == "Nivel aceptable":
    print("Calidad: Excelente / Alta")
  elif calidad == "Nivel de atención":
    print("Calidad: Aceptable")
  else:
    print("Calidad: Deficiente")
    
  # Desperdicio evaluando si es menor al 5% de la producción real
  if prod_real > 0 and (prod_defectuosa / prod_real) <= 0.05:
    print("Desperdicio: Controlado eficientemente")
  else:
    print("Desperdicio: Por encima del margen ideal")
    
  # Eficiencia
  if eficiencia >= 80:
    print("Eficiencia: Alta.")
  elif eficiencia >= 60:
    print("Eficiencia: Moderada.")
  else:
    print("Eficiencia: Baja")
  print("========================================\n")




#Resultado final de la simulacion 
def informe_final(nombre_planta, nombre_supervisor, prod_planificada_total, prod_real_total, prod_defectuosa_total, costo_acumulado_total, calidad_prom):
  
  if prod_planificada_total > 0:
    cumplimiento_total = (prod_real_total / prod_planificada_total) * 100
  else:
    cumplimiento_total = 100

  print("\n=========================================")
  print("              INFORME FINAL              ")
  print("=========================================")
  print(f"\nPlanta: {nombre_planta}")
  print(f"Supervisor: {nombre_supervisor}")
  print(f"Producción planificada : {round(prod_planificada_total, 1)}")
  print(f"Producción realizada   : {round(prod_real_total, 1)}")
  print(f"Total Defectuosos      : {round(prod_defectuosa_total, 1)}")
  print(f"Costo Total Acumulado  : {round(costo_acumulado_total, 2)}$")
  print("-----------------------------------------")

  if calidad_prom >= 90:
    resultado = "Plan de calidad cumplido exitosamente!"
  elif calidad_prom >= 75:
    resultado = "Cumplimiento parcial por calidad estandar!"
  else:
    resultado = "Critico por defectos de calidad!"

  print(f"RESULTADO DE LA SIMULACION: {resultado}")
  print("=========================================\n")
