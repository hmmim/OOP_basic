class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I don't what I say")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    def speak(self):
        print("MEOW")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I'm {self.color}")

class Dog(Pet):
    def __init__(self,name,age,nationality):
        super().__init__(name,age)
        self.nationality = nationality
    def speak(self):
        print("GAU")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I'm from {self.nationality}")

class Fish(Pet):
    pass
#it seem similarity so that we can write two times => it call #inheritance#
#We call it is generalization(su khai quat hoa)
p = Pet("Tim",27)
p.show()
c= Cat("james",22,"red")
c.show()
c.speak()
d =Dog("Jim",21,"Finland")
d.show()

