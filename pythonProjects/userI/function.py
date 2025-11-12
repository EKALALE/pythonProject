#Function/Method - Ablock of code that performs tasks

# 1. Starndad Librabry Functons/Inbuilt Fuctions - Already exists

number = max(34 , 56,76,21,79,9)
print("The maximum value is:",number)

print()
x = min(50,70,21,34,88,55)
print("The minimum number is:",x)

# 2. User-Defined fuctions -its created and defined by the user

def greeting ():
    print("Hello there!")

greeting() #fn call

#Parameters/variables and Arguments/values 
def add():
    num1=7
    num2=5
    print(num1+num2)

add()

print()

def add(num1 ,num2):
   
    print(num1+num2)

add(3,8)
add(70,80)