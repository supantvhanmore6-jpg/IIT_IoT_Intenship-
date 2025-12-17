def addition(n1,n2):
    sum=n1+n2
    print("result=",sum)

def substraction(n1,n2):
    sub=n1-n2
    print("result=",sub)

def multiplication(n1,n2):
    mul=n1*n2
    print("result=",mul)

def division(n1,n2):
    div=n1/n2
    print("result=",div)

while(True):
    num1=int(input("enter first number = "))
    num2=int(input("enter second number = "))
    print("1.addition\n2.substraction\n3.multiplication\n4.division")
    choice=int(input("enter operation = "))

    match choice:
        case 1:addition(num1,num2)
        case 2:substraction(num1,num2)
        case 3:multiplication(num1,num2)
        case 4:division(num1,num2)
        
