def calcular_promedio(numeros):
    
    if len(numeros) == 0:
        return "La lista está vacía, no se puede calcular el promedio."
    
    # Calcula el promedio
    promedio = sum(numeros) / len(numeros)
    return promedio

# Prueba la función con algunos valores
numeros = [10, 20, 30, 40]
resultado = calcular_promedio(numeros)
print(f"El promedio es: {resultado}")
