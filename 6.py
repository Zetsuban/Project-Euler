squareSum = 0
sumSquare = 0

for i in range(1,101):
    squareSum += i**2

for i in range(1,101):
    sumSquare += i

sumSquare = sumSquare**2

print(sumSquare - squareSum)