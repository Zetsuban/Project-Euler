def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
    

def lagestPrimeFactor(n):
    for i in range(n,1,-1):
        if n%i == 0 and isPrime(i):
            return i

print(lagestPrimeFactor(600851475143))

#TODO Optimize