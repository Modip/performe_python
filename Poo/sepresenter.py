class Personne:
    def __init__(self, nom, age: int, genre: bool):
        self.nom = nom
        self.age = age
        self.genre = genre

    def sepresenter(self):
        nom = self.nom
        age = self.age
        genre = self.genre
        print("Hello my name is", nom, "i am", age)
        if genre == True:
            print("I am major")

personne=Personne("Modip", 30, True)
result= personne.sepresenter()
