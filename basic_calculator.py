# Design a basic calulator with the Basic Functionality: Add, Subtract, Multiply, Divide
from secrets import choice

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))


def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))


def mult(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))


def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))


print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

choice = input("input your choice: ")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("input first number :"))
    b = int(input("input second number :"))
    add(a, b)
elif choice == "b" or choice == "B":
    print("Subtraction")
    a = int(input("input first number :"))
    b = int(input("input second number :"))
    sub(a, b)
elif choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("input first number :"))
    b = int(input("input second number :"))
    mult(a, b)
elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("input first number :"))
    b = int(input("input second number :"))
    div(a, b)
elif choice == "e" or choice == "E":
    print("Program Ended")
    quit()