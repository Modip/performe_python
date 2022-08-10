
def salut(name, age):
    print("Hello", name, "vous avez", age, "ans")

salut("Mor","12")

def somme(a, b):
    result = a-b
    print("la somme est", result)
nombre1 = 1
nombre2 = 14
somme(nombre1, nombre2)

def payment(solde):
    price = 800
    result = solde-price
    if result >= 0:
        print("Payment susccess your new solde is:",result)
    else:
        print("Solde insuffisant")
    return result
payment(5000)

class Somme:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def result(self):
        result = self.a-self.b
        return result
test=Somme(6, 2)
result = test.result()
print(result)