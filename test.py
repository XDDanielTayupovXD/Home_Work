class meat:

     def __init__(self, name, amount):
        self.name = name
        print("Создано мясо ", name)
        self.amount = amount
    
     def info(self):
        print(f"{self.name} лежит, пищевая ценность: {self.amount}")

    
class dog:

    def __init__(self, n, h, l):
        self.name = n
        self.health = h
        self.live = l
        print("Появилась новая собока с именем", self.name)

    def eating(self, eat_meat):
        print(f"{self.name} кушает")
        self.health += eat_meat.amount
        if (self.health > 35):
            print(f"{self.name} наелся. Количество жизней увеличилось.")
            self.live += 1
            self.health = 20
        if (self.health < 0):
            print("Отравился или голод")
            self.live -= 1
        print(f"Здоровье стало ({self.health})")

    def info(self):
        print(f"Здоровье: {self.health}")
        print(f"Жизней: {self.live}")

    

Bob = dog("Боб", 35, 1)
EAT1 = meat("Мясо", 20)
EAT2 = meat("Замороженное мясо", 10)
EAT3 = meat("Стейк", 50)
EAT4 = meat("ТУЛОЕ МЯСО", -20)

Bob.info()
Bob.eating(EAT3)
Bob.info()