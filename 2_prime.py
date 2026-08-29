# Program 2: Prime Number

num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

limit = int(input("Enter the limit: "))

print("Prime numbers are:")

for n in range(2, limit + 1):
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")