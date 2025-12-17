prices = [105, 110, 108, 112, 115, 116, 114]
avg=[]
for i in range (0,5,2):
    
    avg.append((sum(prices[i:i+3]))//3)

print("the average prices are :",avg)
    