
import random

def control_calidad(prod_obtenida):
    defectos_porc = round(random.uniform(0.01, 0.05), 2) #Es el % de falla por jornada, aleatorio entre los numeros que elegi (0.01 = 1% y 0.05 = 5%)

    prod_defectuosa = round(prod_obtenida * defectos_porc)

    prod_real = prod_obtenida - prod_defectuosa

    porc_defectos = round((prod_defectuosa / prod_obtenida) * 100, 2)

    porc_buenos = round(100 - porc_defectos, 2)

    #La conclusión:
    if porc_buenos >= 95:
        calidad = "Nivel aceptable"
    elif porc_buenos >= 90 and porc_buenos <= 94: 
        calidad = "Nivel de atención"
    else:
        calidad = "Nivel critico"

    return defectos_porc, prod_defectuosa, prod_real, porc_defectos, porc_buenos, calidad
