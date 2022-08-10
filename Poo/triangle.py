class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetre(self):
        perimetre = self.a + self.b + self.c
        return perimetre

triangle = Triangle(3, 7, 9)

perimetre=triangle.perimetre()
print(perimetre)