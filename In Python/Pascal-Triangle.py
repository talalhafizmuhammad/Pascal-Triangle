def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def ncr(n, r):
    return fact(n) // (fact(r) * fact(n - r))

n = int(input("Enter number of rows: "))

for i in range(n):
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(ncr(i, j), end=" ")
    print()
