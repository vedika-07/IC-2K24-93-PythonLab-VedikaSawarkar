# hollow_diamond

n = int(input("Enter an odd number: "))

if n <= 0 or n % 2 == 0:
    print("Please enter a positive odd number.")
else:
    middle = n // 2

    for row in range(n):
        distance = abs(middle - row)
        leading_spaces = distance
        width = n - 2 * distance

        for _ in range(leading_spaces):
            print(" ", end="")

        for col in range(width):
            if col == 0 or col == width - 1:
                print("*", end="")
            else:
                print(" ", end="")

        print()
