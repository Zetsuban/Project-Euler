# Starts with 2520 because it's the smalest divisible by 1 to 10
nb = 2520

def divisible(n):
    for i in range(2,21):
        if n%i != 0:
            return False
    return True

while not divisible(nb):
    # Add 20 because it needs to be divisible by 20 anyway
    nb += 20

print(nb)