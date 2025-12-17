data = ((10, 10, 10, 12),
        (30, 45, 56, 45),
        (81, 80, 39, 32),
        (1, 2, 3, 4))

average = []

cols = len(data[0])

for i in range(cols):          
    total = 0
    for j in data:             
        total = total + j[i]
    avg = total / len(data)
    average.append(avg)

print(average)
