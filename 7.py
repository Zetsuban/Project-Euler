def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = 2
primes = 0

while primes < 10001:
    
    if isPrime(n):
        primes += 1

    n += 1

print(n-1)