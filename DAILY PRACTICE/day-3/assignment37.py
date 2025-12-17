def fact(n):
    if(n==0): 
        return 1
    return n*fact(n-1)

def power(base,exponant):
    if(exponant==0):
        return 1
    return base*power(base,exponant-1)

print("power=",power(5,3))
print("factorial=",fact(5))
    
