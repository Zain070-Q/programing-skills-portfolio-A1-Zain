names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

def findName():
    find = input("Enter a name to find: ")

    if find in names:
        print(f"{find} was found in the list!")
    else:
        print(f"{find} is not in the list.")
        findName()

findName()