import math

# Clase para representar la bola en caída libre
class BolaCaidaLibre:
    def __init__(self, masa, altura_inicial):
        # Masa de la bola (kg)
        self.masa = masa
        # Altura inicial desde la que se deja caer la bola (m)
        self.altura_inicial = altura_inicial
        # Aceleración debido a la gravedad (m/s^2)
        self.g = 9.81
    
    def calcular_velocidad(self, altura_actual):
        """
        Calcula la velocidad de la bola cuando está a una altura 'altura_actual'.
        
        Parametros:
        altura_actual: La altura a la que queremos conocer la velocidad de la bola (en metros).
        
        Retorna:
        velocidad: La velocidad de la bola en metros por segundo.
        """
        # Comprobamos que la altura actual esté dentro de un rango válido
        if altura_actual > self.altura_inicial or altura_actual < 0:
            raise ValueError("La altura debe estar entre 0 y la altura inicial.")
        
        # Usamos la fórmula v = sqrt(2g(h - y)) para calcular la velocidad sqrt= raiz cuadrada2
        velocidad = math.sqrt(2 * self.g * (self.altura_inicial - altura_actual))
        return velocidad

def obtener_datos_usuario():
    """
    Función que solicita al usuario la masa y la altura inicial de la bola.
    
    Retorna:
    masa (float): La masa de la bola en kg.
    altura_inicial (float): La altura inicial desde la que se deja caer la bola en metros.
    """
    # Solicitar al usuario la masa y la altura inicial
    masa = float(input("Ingresa la masa de la bola (en kg): "))
    altura_inicial = float(input("Ingresa la altura inicial desde la que se deja caer la bola (en metros): "))
    
    return masa, altura_inicial

# Función principal
def main():
    # Obtener los datos del usuario
    masa, altura_inicial = obtener_datos_usuario()
    
    # Crear el objeto de la clase BolaCaidaLibre
    bola = BolaCaidaLibre(masa, altura_inicial)
    
    # Solicitar al usuario la altura a la que desea calcular la velocidad
    altura = float(input("Ingresa la altura (en metros) a la que deseas conocer la velocidad: "))
    
    try:
        # Calcular la velocidad en la altura indicada
        velocidad = bola.calcular_velocidad(altura)
        print(f"La velocidad de la bola cuando está a {altura} metros sobre el suelo es {velocidad:.2f} m/s.")
    except ValueError as e:
        print(e)

# Ejecutar el programa
if __name__ == "__main__":
    main()

