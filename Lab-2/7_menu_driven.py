# Program 7: Menu Driven Program

while True:

    print("\n----- MENU -----")
    print("1. Armstrong Number")
    print("2. Prime Number")
    print("3. Perfect Number")
    print("4. Palindrome")
    print("5. Fibonacci")
    print("6. Pattern")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        temp = num
        sum = 0

        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** len(str(num))
            temp = temp // 10

        if sum == num:
            print("Armstrong number")
        else:
            print("Not an Armstrong number")

    elif choice == 2:
        num = int(input("Enter a number: "))
        prime = True

        if num < 2:
            prime = False

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print("Prime number")
        else:
            print("Not a prime number")

    elif choice == 3:
        num = int(input("Enter a number: "))
        sum = 0

        for i in range(1, num):
            if num % i == 0:
                sum = sum + i

        if sum == num:
            print("Perfect number")
        else:
            print("Not a perfect number")

    elif choice == 4:
        text = input("Enter a string: ")

        if text == text[::-1]:
            print("Palindrome")
        else:
            print("Not a palindrome")

    elif choice == 5:
        n = int(input("Enter number of terms: "))
        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b

    elif choice == 6:
        n = int(input("Enter number of rows: "))

        for i in range(1, n + 1):
            for j in range(i):
                print("*", end="")
            print()

    elif choice == 7:
        print("Program ended")
        break

    else:
        print("Invalid choice")
