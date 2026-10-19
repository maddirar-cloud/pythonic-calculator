
def complexArithmetic():
    func = input("multiply  or divide? ")
    if func.lower() == "multiply":
        x = int(input("what's the first number you want to multiply? "))
        y = int(input("what's the second number you want to multiply? "))
        result = x * y
        print(result)
    else:
        x = input("what's the first number you want to divide? ")
        y = input("what's the second number you want to divide? ")
        result = x/y
        print(result)
            
    def main():
        complexArithmetic()
    
    if __name__ == "__main__":
        main()
