def isPalindrom(n):
    pass

def palin():
    palindrom = 0
    for i in range(100,1000):
        for k in range(100,1000):
            if isPalindrom(i*k) and i*k > palindrom:
                palindrom = i*k if i*k > palindrom else palindrom
    return(palindrom)

print(palin())