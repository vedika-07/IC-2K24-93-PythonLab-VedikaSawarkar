# Python Lab 2

## Program 1: Armstrong Number

### Aim
To check whether a number is an Armstrong number and display Armstrong numbers within a given range.

### Logic
The number of digits is calculated first. Each digit is raised to the power of the number of digits and all the values are added. If the sum is equal to the original number, it is an Armstrong number.

### Sample Input
153

### Sample Output
153 is an Armstrong number.

---

## Program 2: Prime Number

### Aim
To check whether a number is prime and display prime numbers up to a given limit.

### Logic
A number is prime if it has no divisor other than 1 and itself. Divisors are checked only up to the square root of the number.

### Sample Input
29

### Sample Output
29 is a prime number.

---

## Program 3: Perfect Number

### Aim
To check whether a number is a perfect number and display perfect numbers up to a given limit.

### Logic
The proper divisors of the number are added. If their sum is equal to the original number, the number is perfect.

### Sample Input
6

### Sample Output
6 is a perfect number.

---

## Program 4: Palindrome

### Aim
To check whether a number or string is a palindrome using arithmetic and string methods.

### Logic
In the arithmetic method, the number is reversed using remainder and integer division. In the string method, the string is compared with its reverse.

### Sample Input
121

### Sample Output
Arithmetic method: Palindrome

---

## Program 5: Fibonacci

### Aim
To generate the Fibonacci series using iteration and recursion.

### Logic
The iterative method uses a loop to generate the series. The recursive method calls itself to calculate Fibonacci numbers.

### Sample Input
10

### Sample Output
0 1 1 2 3 5 8 13 21 34

---

## Program 6: Pattern Printing

### Aim
To print different patterns using nested loops.

### Logic
Nested loops are used to control the number of rows, spaces and characters printed in each row.

### Sample Input
4

### Sample Output
Patterns are printed for 4 rows.

---

## Program 7: Menu-Driven Application

### Aim
To combine programs 1 to 6 into a single menu-driven application.

### Logic
A menu is displayed using a loop. The user's choice determines which program is executed. The menu continues until the user selects Exit.

### Sample Input
1

### Sample Output
The selected program is executed.

---

## Program 8: Number Guessing Game

### Aim
To create a number guessing game where the user guesses a randomly generated number between 1 and 100.

### Logic
The computer generates a random number. The user gets a maximum of 7 attempts. After every guess, the program indicates whether the guess is too high or too low.

### Sample Input
50

### Sample Output
Too high! / Too low! / Correct!

---

# Analysis

## 1. For loop vs While loop

A `for` loop is generally more suitable when the number of iterations is known, such as printing a fixed number of Fibonacci terms or checking a range.

A `while` loop is useful when the number of iterations depends on a condition, such as reversing the digits of a number.

## 2. Fibonacci: Iteration vs Recursion

The iterative approach is more efficient because it calculates the Fibonacci series using a single loop.

The recursive approach makes many repeated function calls because the same Fibonacci values may be calculated multiple times. Therefore, recursion requires more function calls and computational work for larger values of `n`.

## 3. Why is checking up to √n enough for Prime Number?

If a number `n` has a factor greater than √n, it must have another factor smaller than √n.

For example, if:

n = a × b

then at least one of `a` or `b` must be less than or equal to √n.

Therefore, checking divisors only up to √n is sufficient to determine whether a number is prime.

## 4. Strategy for minimum guesses in the guessing game

Binary search is an efficient strategy when the possible numbers are ordered. After every guess, approximately half of the remaining range can be eliminated.

For a range from 1 to 100, this strategy can find the number in at most about 7 guesses.
