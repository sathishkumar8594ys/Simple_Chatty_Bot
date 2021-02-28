N = int(input())
n = 0
while n < N:
    n = n + 1
    remain = n % 2
    if remain == 0 and n != N:
        print(n)