#Calificaciones por 4 años de carrera

calificaciones = 5
años = 4
calificacion_total_carrera = []

for i in range(años):
    print(f"Ingresa calificaciones del año {i + 1}:")
    Calificaciones_por_año = []
    for j in range(calificaciones):
        calificacion = float(input(f"calificacion {j + 1}: "))
        Calificaciones_por_año.append(calificacion)
        calificacion_total_carrera.append(Calificaciones_por_año)
        
        
print("Calificaciones_almacenadas")
for i, Calificaciones_por_año in enumerate(calificacion_total_carrera):
    print(f"calificacion: {i + 1}: {Calificaciones_por_año}")
    
promedios_por_año = []   
for Calificaciones_por_año in calificacion_total_carrera:
    promedio_por_año = sum(Calificaciones_por_año) / calificaciones
    promedios_por_año.append(promedio_por_año)
promedio_total = sum(map(sum, calificacion_total_carrera)) / (años * calificaciones)

print("\nEste es el promedio anual:")
for i, promedio_por_año in enumerate(promedios_por_año):
    print(f"año {i + 1}: {promedio_por_año:.2f}")
    
print(f"\nEste es el promedio total de la carrera: {promedio_total:.2f}")
