# PROYECTO-1-

# Simulador de Gestión y Control de una Planta Industrial

## Descripción del Proyecto
La simulación coloca al usuario en el rol de *Supervisor de Producción*, permitiéndole tomar decisiones estratégicas a lo largo de un ciclo operativo de 5 jornadas de trabajo.

Durante la ejecución, el sistema modela un proceso industrial real administrando variables de tiempo, materia prima, líneas de producción, mantenimientos, costos acumulados y control de calidad, evaluando el impacto directo de cada decisión sobre los indicadores finales de la planta.

---

## Integrantes del Equipo
* Albany Farías (Ingeniería de Sistemas)
* Melissa Girandola (Ingeniería de Sistemas)
* Paula Páez (Ingeniería de Sistemas)
* Sebastian Mota (Ingeniería de Sistemas)
* Paola Gonzalez (Ingeniería Industrial)

---

## Estructura Modular y Responsabilidades
El proyecto fue construido bajo los principios de programación estructurada y modularidad en Python, dividido en módulos con responsabilidades claramente definidas:

1. **main.py**: Coordinador principal del programa. Controla el flujo general, el bucle iterativo de las 5 jornadas y la opción de reinicio completo de la simulación.
2. **datos_2.py**: Maneja la interfaz inicial de bienvenida, la captura del nombre de la planta y del supervisor, y el selector de escenarios iniciales.
3. **planificacion.py**: Contiene la lógica de planificación de cada jornada, validando la factibilidad del plan segú*n demanda, horas y materia prima disponible.
4. **calculo_produccion.py**: Ejecuta el núcleo matemático del proceso productivo, calculando unidades obtenidas, consumos de insumos, desperdicios y tiempos de reloj utilizados.
5. **mantenimiento.py**: Controla el desgaste acumulado de la maquinaria, permitiendo al usuario ejecutar mantenimientos preventivos que afectan costos y disponibilidad horaria.
6. **costos.py**: Realiza los cálculos financieros acumulados de la planta (materia prima, mantenimientos, horas perdidas y penalizaciones por defectos).
7. **cosas.py**: Encargado de la presentación gráfica (Panel de Estado de la Planta, Evaluación de la Jornada e Informe Final del proyecto).
8. **def incidencia_falta_de_materia_prima (m.py**: Genera y resuelve eventos imprevistos de forma aleatoria (falta de materia prima, falla de maquinaria, problemas de calidad y pérdida de tiempo), procesando las decisiones tomadas y sus repercusiones en costos, horas y calidad.

---

## Reglas de la Simulación e Indicadores

### 1. Parámetros Estándar de Producción
* **Tiempo por unidad:** 20 minutos por producto.
* **Materia prima por unidad:** 15 kg de material.
* **Capacidad Máxima (Líneas):** Hasta 4 líneas de producción operativas simultáneamente.

### 2. Estructura de Costos
* **Materia Prima:** $5 por cada kg consumido.
* **Penalización por Defectos:** $10 por cada producto defectuoso.
* **Horas Perdidas:** $25 por cada hora de producción no aprovechada.
* **Mantenimiento Preventivo:** $150 de costo fijo (reduce 2 horas disponibles de la jornada).

### 3. Escenarios Iniciales
* **Escenario 1 (Producción Estable):** 50,000 kg de materia prima inicial.
* **Escenario 2 (Alta Demanda):** 60,000 kg de materia prima inicial.
* **Escenario 3 (Producción Crítica):** 20,000 kg de materia prima inicial.

### 4. Evaluación de Calidad y Eficiencia
* **Calidad:** Porcentaje de unidades aceptadas sobre la producción real obtenida.
  * `>= 95%`: Nivel aceptable.
  * `90% a 94%`: Nivel de atención.
  * `< 90%`: Nivel crítico.
* **Cumplimiento:** Relación porcentual entre la producción realizada y la planificada.
* **Eficiencia:** Porcentaje de tiempo de producción utilizado respecto al tiempo total disponible.

### 5. Sistema de Incidencias y Toma de Decisiones
Durante cada jornada de trabajo, el sistema puede activar una incidencia aleatoria que obliga al supervisor a tomar una decisión estratégica entre 3 alternativas reales:

- **Falta de Materia Prima:** Permite comprar insumos de emergencia (+$150 en costos), ajustar a la baja la meta de producción o cancelar el lote actual.
- **Falla de Maquinaria:** Permite realizar una reparación de emergencia (+$200 en costos), continuar la producción asumiendo un incremento de 5 productos defectuosos, o suspender la producción registrando 2 horas perdidas.
- **Problema de Calidad en Insumos:** Permite rechazar la materia prima buscando un proveedor alternativo (+$100 en costos), aceptar los insumos asumiendo un 10% de desperdicio y +$50 en costos, o cancelar el lote por control de calidad.
- **Pérdida de Tiempo de Producción:** Permite contratar personal de apoyo (+$100 en costos), extender la jornada pagando horas extras (+$50 en costos y recuperando tiempo), o declarar el resto del día como tiempo perdido (+2 horas perdidas).
---
