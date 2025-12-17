def binary():
    num=int(input("enter the number="))
    binary=""
    while(num>0):
        binary=str(num%2)+binary
        num=num//2
    print(binary)

binary()