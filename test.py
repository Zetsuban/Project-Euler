sumo = 0
summ = 0

for i in range(20):
    if i%2 == 0:
        sumo += i

for i in range(20):
    summ += i if i%2 == 0 else 0

print(sumo)
print(summ)