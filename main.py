class Vector:
    def __init__(self, x, y, z):
        if isinstance((x, y, z), (list, tuple)):
            self.x, self.y, self.z = x, y, z
        elif isinstance(x, int):
            self.x, self.y, self.z = x, x, x
        else:
            self.x, self.y, self.z = 0, 0, 0

    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __abs__(self):
        return self.length()

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    #Веторное произведение
    def __xor__(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    @staticmethod
    def triple_product(a, b, c):
        return a.dot_product(b ^ c)

    def __or__(self, other):
        return abs(self ^ other) < 1e-9

    @staticmethod
    def are_complanar(a, b, c):
        return abs(a ^ b) < 1e-9 and abs(a ^ c) < 1e-9


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = v1 + v2

print(v3.x, v3.y, v3.z)
print(abs(v1))
print(v1.dot_product(v2))
print(v1 ^ v2)
print(Vector.triple_product(v1, v2, v3))
print(v1 | v2)
print(Vector.are_complanar(v1, v2, v3))