# Program 6: Pattern Printing

n = int(input("Enter number of rows: "))

print("Pattern 1:")

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


print("Pattern 2:")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


print("Pattern 3:")

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()
