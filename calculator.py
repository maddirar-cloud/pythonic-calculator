import math


def arithmetic():
    x=0
    y=0
    func = input("Add or Subtract? ")
    if func.lower() == "add":
        x = int(input("what's the first number you want to add? "))
        y = int(input("what's the second number you want to add? "))
        result = x + y
        print(result)
    else:
        x = input("what's the first number you want to subtract? ")
        y = input("what's the second number you want to subtract? ")
        result = x - y
        print(result)

def main():
    arithmetic()

if __name__ == "__main__":
    main()