def fabonacci():
    num=int(input("enter the no upto which you want to print fabonacci series = "))
    a=0
    b=1
    for i in range(num):
        print(a,end="  ")
        a,b=b,a+b

fabonacci()
