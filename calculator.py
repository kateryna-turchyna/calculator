
def add (x,y):
    return x+y
def subtract (x, y):
    return x-y
def multiply (x, y):
    return x*y
def divide (x,y):
    return x/y

while True:
    question=input("do you want to use a calculator: yes/no ")
    if question == 'yes':
    
        choice_op=input("select operation: add, sub, mul, div ")
        num1=int(input("first number "))
        num2=int(input("second number "))

        if choice_op == 'add':
            print(add(num1,num2))
        elif choice_op == 'sub':
            print(subtract(num1,num2))
        elif choice_op == 'mul':
            print(multiply(num1,num2))
        elif choice_op == 'div':
            print(divide(num1,num2))
        else:
            print("invalid input")
    else:
        break
    


    
                
