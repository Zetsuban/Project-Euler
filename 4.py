def isPalindrom(n):
    nb = str(n)
    if len(nb)%2 == 0:
        first, second = nb[:len(nb)//2], nb[len(nb)//2:]
        if first == second[::-1]:
            return True
        else:
            return False

def palin():
    palindrom = 0
    for i in range(100,1000):
        for k in range(100,1000):
            if isPalindrom(i*k) and i*k > palindrom:
                palindrom = i*k
    return(palindrom)

print(palin())