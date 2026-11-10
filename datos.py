#Datos iniciales

def mostrar_bienvenida():
  print("=========================================================")
  print("          SISTEMA DE CONTROL Y GESTION DE PLANTA         ")
  print("=========================================================")
  print("Bienvenido. Asumiras el control operativo de la planta durante 5  jornadas.\n")


def datos_iniciales():
  nombre_planta = input("Ingrese el nombre de la planta de produccion: ")
  while nombre_planta == "":
    print("El nombre no puede estar vacio.")
    nombre_planta = input("Ingrese el nombre de la planta de produccion: ")

  nombre_supervisor = input("Ingrese su nombre (Supervisor): ")
  while nombre_supervisor == "":
    print("El nombre del supervisor no puede estar vacio.")
    nombre_supervisor = input("Ingrese su nombre (Supervisor): ")

  return nombre_planta, nombre_supervisor


def seleccionar_escenario():
  print("\n--- SELECCION DE ESCENARIO DE PRODUCCION ---")
  print("1. Produccion Estable (Normal)")
  print("2. Alta Demanda (Exigente)")
  print("3. Produccion Critica (Restricciones fuertes)")

  opcion = 0

  while opcion < 1 or opcion > 3:
    try:
      opcion = int(input("Seleccione una opcion (1-3): "))
      if opcion < 1 or opcion > 3:
        print("Opcion invalida. Elija 1, 2 o 3.")
    except ValueError:
      print("Debe ingresar un numero entero valido.")

  match opcion:
    case 1:
      mp_inicial = 50000
     
    case 2:
      mp_inicial = 60000

    case 3:
      mp_inicial = 20000
 
  return mp_inicial
