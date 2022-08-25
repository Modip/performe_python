import random


class Personne:
    def __init__(self, name: str, mark: int = 50, flask=3):
        self.name = name
        self.mark = mark
        self.flask = flask

    @property
    def damage(self):
        return random.randint(1, 10)

    def attack(self, enemi: "Personne") -> int:
        damage_inflict = self.damage

        enemi.mark -= damage_inflict
        print(self.name, "à infligé un domage de", damage_inflict, "points à", enemi.name, "il lui reste", enemi.mark, "points")
        return damage_inflict
    def take_flask(self):
        if not self.flask:
            print("Vous avez plus que potion")
            return False

        flask_mark = random.randint(5, 50)
        self.mark += flask_mark
        print("Vous avez recuperer une potion, vous avez ", self.mark)
        return True


def _derouler(actor: Personne, enemi:Personne):
    while actor.mark > 0 and enemi.mark > 0:
        choix = int(input("Veiller choisir entre \n 1: pour attack \n 2: pour potion \n"))
        print("-" * 70)
        if choix == 1:
            actor.attack(enemi)
            enemi.attack(actor)

        elif choix == 2:
            actor.take_flask()
            enemi.attack(actor)
        print("-" * 70)
        if enemi.mark <= 0:
            print("You win")
            print("-" * 70)
            break
        elif actor.mark <= 0:
            print("You lose")
            print("-" * 70)
def _star():
    actor = Personne("Modip")
    enemi = Personne("Adversaire", 50, 0)
    _derouler(actor, enemi)


if __name__ == "__main__":
    _star()


