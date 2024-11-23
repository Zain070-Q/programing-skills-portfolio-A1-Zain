def verifypassword():
    maxTries = 5
    correctPassword = "12345" 

    for tries in range(maxTries):
        password = input("Enter password: ")

        if password == correctPassword:
            print("Correct! Access granted.")
            return
        else:
            print(f"Invalid password. You have {maxTries - tries - 1} tries left.")

    print("Too many failed tries. Try again later.")

verifypassword()