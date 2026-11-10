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