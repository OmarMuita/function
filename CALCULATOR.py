def add(num1,num2):
    addition=num1+num2
    return addition
def subtract(num3,num4):
    subtract=num3-num4
    return subtract
def multiply(num5,num6):
    multiply=num5*num6
    return multiply
def divide(num6,num7):
    divide=num6/num7
    return divide
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
choice=int(input("Enter your choice:"))
if choice==1:
    print(add(num1,num2))
if choice==2:
    print(subtract(num1,num2))
if choice==3:
    print(multiply(num1,num2))
if choice==4:
    print(divide(num1,num2))









      
