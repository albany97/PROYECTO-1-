#Mantenimiento

def mantenimiento(lineas_disp, tiemp_disponible):
  
    print("\n==================================================")
    print("                   Mantenimiento                    ")
    print("====================================================")
    
    #Estado de la maquina
    print(f"-> Estado actual: {lineas_disp} líneas operativas de 4 posibles")
    
    print("\nSeleccione la acción de mantenimiento para la jornada:")
    print("1. Mantenimiento Preventivo (Mantiene o mejora las líneas, consume poco tiempo)")
    print("2. Mantenimiento Correctivo (Repara urgente líneas caídas, consume más tiempo)")
    print("3. Omitir mantenimiento (Sin costo ni tiempo extra, riesgo de desgaste)")

    #Validacion de lo q se ingresa:
    opcion = 0
    while opcion < 1 or opcion > 3:
        try:
            opcion = int(input("Ingrese su opción (1-3): "))
            if opcion < 1 or opcion > 3:
                print("Opción inválida. Elija 1, 2 o 3.")
        except ValueError:
            print("Debe ingresar un número entero válido")
    #Iniciamos var.
    costo_mantenimiento = 0.0
    tiemp_gastado = 0.0

    #Las diferentes vertientes:
    if opcion == 1:
        #Preventivo: Cuesta dinero/tiempo controlado, asegura rendimiento
        tiemp_gastado = 30.0  #Todo en min.
        costo_mantenimiento = 150.0  
        print("\nMantenimiento Preventivo Aplicado")
        print("-> Se han ajustado los mecanismos. Tiempo invertido: 30 min.")
        if lineas_disp < 4:
            lineas_disp += 1
            print(f"-> ¡Línea recuperada! Líneas operativas ahora: {lineas_disp}")

    elif opcion == 2:
        # Correctivo: Más pesado, para emergencias o fallas
        tiemp_gastado = 60.0 
        costo_mantenimiento = 300.0
        print("\nMantenimiento Correctivo Aplicado")
        print("-> Reparación profunda ejecutada de emergencia. Tiempo invertido: 60 min.")
        if lineas_disp < 4:
            lineas_disp = min(4, lineas_disp + 2)  # Recupera hasta 2 líneas
            print(f"-> ¡Reparación exitosa! Líneas operativas ahora: {lineas_disp}")

    else:
        print("\nMantenimiento Omitido")
        print("-> La planta operará sin intervenciones técnicas en este turno.")

    # Afectamos las variables de producción (quitamos el tiempo del mantenimiento)
    #Uso el max por si resulta en num. negativo, entonces escogera el max. entre ambos (el 0.0)
    tiemp_disponible = max(0.0, tiemp_disponible - tiemp_gastado)

    return lineas_disp, tiemp_disponible, costo_mantenimiento, tiemp_gastado 