age = int(input("Enter age "))
if age >= 18:
    print("You are qualified to vote")
else:
    print("You are not qualified")   

#program to return for the largest number among 3 numbers 

first = int(input("Enter first number:"))
second = int(input("Enter second number:"))
third = int(input("Enter third number:"))
if first > second and first > third:
    print(first,"is the largest number")

elif second > first and second > third :
    print(second,"is the largest nuber")
else:
    print(third,"is the largest number")

    #Assignment 
    number = int(input("Enter the number"))
    if number % 2 = 0 :
      print (number,"is even")
    else:
        print(number,"is odd")