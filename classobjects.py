#class - is blue print of an object
#Object - is an instance of a class

class Student:
     #Attributes/variables
     name = "John"
     gender = "Male"
     age =  23
     course = "Web development"

     #Behaviour/Method/functions

     def study(self):
          print("Student is studying")

#Creating an Object 
student1 = Student() 

print(student1.name,student1.gender,student1.course)
student1.study()

student2 = Student()  

print(student1.name)
Student3 = Student()      