import math

# Clase para representar la bola en caída libre
class BolaCaidaLibre:
    def __init__(self, masa):
        # Masa de la bola (kg)
        self.masa = masa
        # Aceleración debido a la gravedad (m/s^2)
        self.g = 9.81
    
    def calcular_velocidad(self, altura_inicial, altura_actual):
        if altura_actual > altura_inicial or altura_actual < 0:
            raise ValueError("La altura actual debe estar entre 0 y la altura inicial.")
        
        # Fórmula v = sqrt(2g(h - y))
        velocidad = math.sqrt(2 * self.g * (altura_inicial - altura_actual))
        return velocidad


# Función para obtener los datos del usuario
def obtener_datos_usuario():
    masa = float(input("Ingresa la masa de la bola (en kg): "))
    
    # Solicitar alturas iniciales
    alturas_iniciales = list(
        map(float, input("Ingresa una lista de alturas iniciales (separadas por comas, en metros): ").split(","))
    )
    
    # Solicitar alturas a calcular
    alturas_actuales = list(
        map(float, input("Ingresa una lista de alturas actuales (separadas por comas, en metros): ").split(","))
    )
    
    return masa, alturas_iniciales, alturas_actuales


# Función principal
def main():
    # Obtener datos del usuario
    masa, alturas_iniciales, alturas_actuales = obtener_datos_usuario()
    
    # Crear el objeto de la clase
    bola = BolaCaidaLibre(masa)
    
    # Calcular velocidades usando ciclos anidados
    print("\nCálculo de velocidades:\n")
    for altura_inicial in alturas_iniciales:
        print(f"Para altura inicial = {altura_inicial} m:")
        for altura_actual in alturas_actuales:
            try:
                velocidad = bola.calcular_velocidad(altura_inicial, altura_actual)
                print(f"  - A {altura_actual} m: velocidad = {velocidad:.2f} m/s")
            except ValueError as e:
                print(f"  - A {altura_actual} m: {e}")
        print()  # Salto de línea entre experimentos


# Ejecutar el programa
if __name__ == "__main__":
    main()
