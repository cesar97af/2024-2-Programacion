class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, escalar):
        return Vector2D(self.x * escalar, self.y * escalar)

    def magnitud(self):
        return (self.x**2 + self.y**2)**0.5

    def normalizar(self):
        mag = self.magnitud()
        return Vector2D(self.x / mag, self.y / mag)

    def __repr__(self):
        return f"({self.x}, {self.y})"

class CuerpoOrbital:
    def __init__(self, masa, posicion, velocidad):
        self.masa = masa
        self.posicion = posicion  
        self.velocidad = velocidad  

    def actual_posicion(self, dt):
        self.posicion = self.posicion + self.velocidad * dt

    def aplicar_fuerza(self, fuerza, dt):
        aceleracion = fuerza * (1 / self.masa)
        self.velocidad = self.velocidad + aceleracion * dt
def calcular_la_fuerza_gravitacional(cuerpo1, cuerpo2, G):
    r_vector = cuerpo2.posicion - cuerpo1.posicion
    distancia = r_vector.magnitud()
    fuerza_magnitud = G * cuerpo1.masa * cuerpo2.masa / distancia**2
    fuerza_vector = r_vector.normalizar() * fuerza_magnitud
    return fuerza_vector

def orbita_simulada(cuerpo1, cuerpo2, G, dt, steps):
    for _ in range(steps):
        fuerza = calcular_la_fuerza_gravitacional(cuerpo1, cuerpo2, G)
        cuerpo1.aplicar_fuerza(fuerza, dt)
        cuerpo2.aplicar_fuerza(fuerza, dt)
        cuerpo1.actual_posicion(dt)
        cuerpo2.actual_posicion(dt)
        print(f"Posición del cuerpo 1: {cuerpo1.posicion}, Posición del cuerpo 2: {cuerpo2.posicion}")

# Constantes físicas y parámetros iniciales
G = 6.67430e-11  # Constante gravitacional
masa1 = 5.972e24  # Masa de la Tierra
masa2 = 7.348e22  # Masa de la Luna
posición_inicial1 = Vector2D(0, 0)
posición_inicial2 = Vector2D(384400000, 0)  # Distancia Tierra-Luna en unidades mts
velocidad_inicial1 = Vector2D(0, 0)
velocidad_inicial2 = Vector2D(0, 1022)  # Velocidad orbital de la Luna en m/s

Tierra = CuerpoOrbital(masa1, posición_inicial1, velocidad_inicial1)
Luna = CuerpoOrbital(masa2, posición_inicial2, velocidad_inicial2)

orbita_simulada(Tierra, Luna, G, dt=60, steps=10)