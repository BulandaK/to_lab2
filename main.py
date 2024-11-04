import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getComponents(self):
        return [self.x, self.y]

    def abs(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def cdot(self, vector):
        return self.x * vector.x + self.y * vector.y

class PolarInheritance2D(Vector2D):
    def getAngle(self):
        return math.atan2(self.y, self.x)

class Vector3DInheritance(Vector2D):
    def __init__(self, x, y, z=0):
        super().__init__(x, y)
        self.z = z

    def getComponents(self):
        return [self.x, self.y, self.z]

    def abs(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def cdot(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def cross(self, vector):
        x = self.y * vector.z - self.z * vector.y
        y = self.z * vector.x - self.x * vector.z
        z = self.x * vector.y - self.y * vector.x
        return [x, y, z]
    def getSrcV(self):
        return self

def Vector3DDecorator(vector, z=0):
    vector.z = z

    def getComponents():
        return [vector.x, vector.y, vector.z]

    def abs():
        return math.sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 2)

    def cdot(other_vector):
        return vector.x * other_vector.x + vector.y * other_vector.y + vector.z * other_vector.z

    def cross(other_vector):
        x = vector.y * other_vector.z - vector.z * other_vector.y
        y = vector.z * other_vector.x - vector.x * other_vector.z
        z = vector.x * other_vector.y - vector.y * other_vector.x
        return [x, y, z]
    def getSrcV():
        return vector

    vector.getComponents = getComponents
    vector.abs = abs
    vector.cdot = cdot
    vector.cross = cross

    return vector

# Utworzenie trzech przykładowych wektorów
vector1 = PolarInheritance2D(3, 4)  # Wektor 2D
vector2 = Vector3DInheritance(1, 2, 3)  # Wektor 3D
vector3 = Vector3DInheritance(4, 5, 6)  # Kolejny wektor 3D

# Wyświetlenie współrzędnych kartezjańskich
print("Współrzędne kartezjańskie:")
print("Vector1:", vector1.getComponents())
print("Vector2:", vector2.getComponents())
print("Vector3:", vector3.getComponents())

# Wyświetlenie współrzędnych biegunowych (kąt i długość) dla wektora 2D
print("\nWspółrzędne biegunowe:")
print("Długość Vector1:", vector1.abs())
print("Kąt Vector1:", vector1.getAngle())

# Obliczenie iloczynów skalarnych
print("\nIloczyny skalarne:")
print("Vector1 · Vector2:", vector1.cdot(vector2))
print("Vector1 · Vector3:", vector1.cdot(vector3))
print("Vector2 · Vector3:", vector2.cdot(vector3))

# Obliczenie iloczynów wektorowych
print("\nIloczyny wektorowe (współrzędne kartezjańskie):")
# Uwaga: Iloczyn wektorowy jest zdefiniowany tylko dla wektorów 3D
print("Vector2 x Vector3:", vector2.cross(vector3))
# Dla iloczynu wektorowego z Vector1 (2D) zakładamy, że z = 0 dla Vector1
vector1_3d = Vector3DInheritance(vector1.x, vector1.y, 0)
print("Vector1 x Vector2:", vector1_3d.cross(vector2))
print("Vector1 x Vector3:", vector1_3d.cross(vector3))

