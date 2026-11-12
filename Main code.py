
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
    horas_perdidas = 0
    desperdicio = 0
    prod_defectuosa = 0

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
        print("\n------ Incidente -----")
        costo_acumulado, prod_planificada, horas_perdidas, desperdicio, prod_defectuosa = simular_incidencia_aleatoria(costo_acumulado, prod_planificada, horas_perdidas, desperdicio, prod_defectuosa)


        #Produccion:
        prod_obtenida, mp_consumida, mp_restante, tiemp_gastado = calcular_produccion(tiemp_disponible, TIEMP_XUNIDAD, lineas_disp, mp_actual, CANT_MP_XUNIDAD, prod_planificada)
        print("\n====================================================")
        print("                   Producción                       ")
        print("====================================================")
        print(f"\nLa producción obtenida durante esta jornada fue de: {prod_obtenida} unidades")
        print(f"La planta consumió un total de {mp_consumida}Kg de materia prima")
        print(f"Sobro un total de {mp_restante}Kg de materia prima")

        #Control de la mp
        mp_actual = mp_restante

        #Control de calidad:
        defectos_porc, prod_defectuosa, prod_real, porc_defectos, porc_buenos, calidad = control_calidad(prod_obtenida)
        print("\n------ Control de calidad -----")
        print(f"\nDurante esta jornada se presentó un margen de error del: {defectos_porc}%")
        print(f"Se obtuvo un total de {prod_real} und. de productos en optimas condiciones")
        print(f"Mientras que hubieron {prod_defectuosa} und. de productos defectuosos")
        print(f"Concluye en un {porc_buenos}% de productos buenos y {porc_defectos}% de productos defectuosos")

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
