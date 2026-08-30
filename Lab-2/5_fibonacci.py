# Program 5: Fibonacci Series

n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci using loop:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("\nFibonacci using recursion:")

for i in range(n):
    print(fibonacci(i), end=" ")
