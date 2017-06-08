class Animal(object):
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health

    def displayHealth(self):
        print self.name
        print self.health
        return self

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

animal1 = Animal('Cat', 100)
animal1.walk().walk().walk().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self). __init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

dog1 = Dog("Rover")
dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self). __init__(name)
        self.health = 170
        print "I am a Dragon!"
    def fly(self):
        self.health -= 10
        return self

dragon = Dragon('Flying Dragon')
dragon.displayHealth            
