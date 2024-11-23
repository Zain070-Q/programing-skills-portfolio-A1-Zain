def isOddOrEven(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def getUserInput():
    return int(input("Enter a number: "))

def main():
    number = getUserInput()
    result = isOddOrEven(number)
    print(f"The number is {result}.")

main()