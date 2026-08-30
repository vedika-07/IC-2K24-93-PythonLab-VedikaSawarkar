# butterfly pattern

n = int(input("Enter the number of rows: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    for row in range(1, 2 * n):
        stars = row if row <= n else 2 * n - row
        middle_spaces = 2 * (n - stars)

        for _ in range(stars):
            print("*", end="")

        for _ in range(middle_spaces):
            print(" ", end="")

        for _ in range(stars):
            print("*", end="")

        print()

