# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Afsha Sayyed
# Date: 30/01/2026

print("--- Factorial Finder ---\n")
number = int(input())

if number < 0:
    print(f"Factorial of {abs(number)} is Not Defined")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"Factorial of {number} is {factorial}")
  

