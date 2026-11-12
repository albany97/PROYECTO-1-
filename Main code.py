
#Aqui todas las importaciones:
from datos import mostrar_bienvenida, datos_iniciales, seleccionar_escenario 
#Mostrar bienvenida: Menu de entrada. Datos inciales: nombre planta/ususario. Seleccion escenario: mp_inicial y horas disp inicial

from planificacion import planificar_jornada 
#Planificar jornada: prod_planificada, prod_demanda, lineas_disp, tiemp_disponible, continuar

from produccion import calcular_produccion
#Calculo produccion: prod_obtenida, mp_consumida, mp_restante, tiemp_usado

from control_de_calidad import control_calidad 
#Control calidad: defectos_porc, prod_defectuosa, prod_real, porc_defectos, porc_buenos, calidad

from mantenimiento import mantenimiento

from evaluacion_jornada import estado_jornada

from incidencias import simular_incidencia_aleatoria

from sistema_de_costos import calcular_costo_jornada

#Constantes
CANT_MP_XUNIDAD = 15 #En kg
TIEMP_XUNIDAD = 20 #En minutos

#Iniciamos variable para el ciclo de la simulacion
iniciar = True
#Aca inicia ya la simulacion:
while iniciar == True:
    #Bienvenida
    mostrar_bienvenida()
    nombre_planta, nombre_supervisor = datos_iniciales()
    mp_actual = seleccionar_escenario()
    mp_consumida = 0
    costo_mantenimiento = 0
    costo_acumulado = 0

    for jornada in range(0, 5):

        #Planificacion
        prod_planificada, prod_demanda, lineas_disp, tiemp_disponible, continuar = planificar_jornada(mp_actual) 

        if not continuar:
            print("Fin de la simulacion! La planta se ha detenido por falta de recursos")
            break

        #Luego mantenimiento:
        lineas_disp, tiemp_disponible, costo_mantenimiento, tiemp_gastado = mantenimiento(lineas_disp, tiemp_disponible)
        #Asi va acumulando de una
        costo_acumulado += costo_mantenimiento

        #La parte de incidencias:
        costo_acumulado, prod_planificada, tiemp_disponible, horas_perdidas, calidad_jornada, desperdicio, productos_defectuosos = simular_incidencia_aleatoria(
        costo_acumulado, prod_planificada, tiemp_disponible, horas_perdidas, desperdicio, productos_defectuosos)

        #Produccion:
        prod_obtenida, mp_consumida, mp_restante, tiemp_usado = calcular_produccion(tiemp_disponible, TIEMP_XUNIDAD, lineas_disp, mp_actual, CANT_MP_XUNIDAD)

        #Control de la mp
        mp_actual = mp_restante

        #Control de calidad:
        defectos_porc, prod_defectuosa, prod_real, porc_defectos, porc_buenos, calidad = control_calidad(prod_obtenida)

        #costos
        costo_acumulado = calcular_costo_jornada(mp_consumida, tiemp_gastado, prod_defectuosa, costo_acumulado)

        #panel de estado
        #indicadores de procesos
        #evaluacion de cada jornada
        






    #Reinicio de simulacion con var. bandera 
    print("Deseas reiniciar la simulacion?")
    iniciar_choice = input("Tu respuesta aca (Si/No): ")

    if iniciar_choice.lower() == "si":
        iniciar = True
    else:
        iniciar = False
