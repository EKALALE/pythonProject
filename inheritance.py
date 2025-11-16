#THe process of acquiring the members(Attributes and Behaviours) of a parent class

#parent class/super class /base class
class Animal:
    isMammal = True
    def sound(self):
        print("Animal is making a sound")

#Child class/sub class/Derived class
class Duck(Animal):
    hasFeather = True
    def swim(self):
        print("Duck is swimming")

class Horse(Duck):
    iswild = True
    def movement(self):
        print("Horse is galloping")


#Creating objects

a= Animal()

print(a.sound)

d = Duck()
d.sound()

h = Horse()
h.hasFeather