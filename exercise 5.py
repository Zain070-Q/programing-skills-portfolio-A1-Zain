Months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 }

M=int(input("choose a month "))
if M in Months:

    print(f"{Months[M]}")
else:
    print("error")