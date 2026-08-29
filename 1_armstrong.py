# Program 1: Armstrong Number

num = int(input("Enter a number: "))

temp = num
sum = 0
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Armstrong numbers are:")

for n in range(start, end + 1):
    temp = n
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** len(str(n))
        temp = temp // 10

    if sum == n:
        print(n, end=" ")