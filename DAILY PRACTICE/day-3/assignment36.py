def addition(n1,n2):
    sum=n1+n2
    return sum

def substraction(n1,n2):
    sub=n1-n2
    return sub

def multiplication(n1,n2):
    mul=n1*n2
    return mul

def division(n1,n2):
    div=n1/n2
    return div

def calculate(num1,num2,func):
    result=func(num1,num2)
    return result

while(True):
    num1=int(input("enter first number = "))
    num2=int(input("enter second number = "))
    print("1.addition\n2.substraction\n3.multiplication\n4.division")
    choice=int(input("enter operation = "))

    match choice:
        case 1:print("result=",calculate(num1,num2,addition))
        case 2:print("result=",calculate(num1,num2,substraction))
        case 3:print("result=",calculate(num1,num2,multiplication))
        case 4:print("result=",calculate(num1,num2,division))
        
