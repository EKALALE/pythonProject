class Dog:
   
   def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age

#creating objets
dog1 = Dog("Tito","Shepherd",3)
print(dog1.name,dog1.breed,dog1.age)

dog2 = Dog("PPLE","chihuahua",5)
print(dog2.name,dog2.breed,dog2.age)

dog3 = Dog("Jane","siberian husky",4)
print(dog3.name,dog3.breed,dog3.age)
