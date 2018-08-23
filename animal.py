class Animal:
    def __init__(self,name,health):
        self.name=name
        self.health=health

    def walk(self):
        self.health=self.health-1

    def run(self):
        self.health=self.health-5

    def displayHealth(self):
        print(str(self.health))
        print(str(self.name))

""" pet=Animal("malu",100)
pet.walk()
pet.walk()
pet.walk()
pet.run()
pet.run()
pet.display_health() """

class Dog(Animal):
    def __init__(self,name,health=150):
        super().__init__(name,health)

    def pet(self):
        self.health=self.health+5

""" doge=Dog("Doge")
doge.walk()
doge.walk()
doge.walk()
doge.run()
doge.run()
doge.pet()
doge.display_health() """

class Dragon(Animal):
    def __init__(self,name,health=170):
        super().__init__(name,health)

    def fly(self):
        self.health=self.health-10

    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon")

""" drogon=Dragon("meow")
drogon.fly()
drogon.display_health()

anotherPet=Animal("neighbor",10)
#anotherPet.pet()
#anotherPet.fly()
anotherPet.display_health() """


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def addDog(self, name):
        self.animals.append( Dog(name) )
    def addDragon(self, name):
        self.animals.append( Dragon(name) )
    def printAllHealth(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.displayHealth()
            
zoo1 = Zoo("John's Zoo")
zoo1.addDog("Tracy")
zoo1.addDog("Doggeh")
zoo1.addDragon("Draggeh")
zoo1.addDragon("Dragoon")
zoo1.printAllHealth()
