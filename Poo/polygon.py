class Polygon:
    def __init__(self, slices):
        self.slices = slices

    def info(self):
        print("Le polygon a plusieurs cotes")

    def perimetre(self):
        perimetre = sum(self.slices)
        return perimetre

class Triangle(Polygon):
    def info(self):
        print("Triangle a trois cotes")

class Carre(Polygon):
    def info(self):
        print("Le carre a quatre cotes")

triangle = Triangle([3, 4, 5])
perimetre = triangle.perimetre()
carre = Carre([2, 2, 2, 2])
perimetrecarre = carre.perimetre()
info = triangle.info()
print("Le perimetre du carré est de :", perimetre)
print("Le perimetre du carré est de :", perimetrecarre)