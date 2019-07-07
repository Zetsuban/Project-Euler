def fibio(n):
    sum = 0
    first, second = 1, 2
    while second <= n:
        first, second = second, first+second
        if second%2 == 0:
            sum += second
    return sum

print(fibio(4000000))