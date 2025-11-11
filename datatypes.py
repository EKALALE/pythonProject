number=60 #integer
weight=58.78 #Float
greeting ="hello" #string
isPythonFun = True #boolean
print(number)
print(weight)
print(greeting)
print("is python fun",isPythonFun)

#data structures-multiple values stored in one variable
#list
cars = ["Mercedes","Audi","Nissan","Toyota"] #list - ordered and changeable

#tupple-ordered and unchangeable
fruits = ("Apple","mango","banana")
countries={ "kenya","Uganda","France"}#set-unordered &unchangable
student = {
    "name":"Felix",
    "course":"web development",
    "age":23,
    "gender":"female"

} #Dictionary - key,value pair


print(cars)
print(fruits)
print(countries)
print(student.get("age"))
print(student["gender"])
# Typecasting - converting one datatype to another
print(int(68.78))
print(int(weight))
print(float(58))