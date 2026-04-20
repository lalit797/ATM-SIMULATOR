import main
def withdrawl_money():
    user_withdrawl = int(input("enter money you want to wintdraw"))
    if user_withdrawl>main.balance:
        print("ISUFFICIENT BALANCE GREEEB😂😂😂")
    else:
     main.balance = main.balance - user_withdrawl
     main.transaction.append(user_withdrawl)
     print(f"\n now your remainig balance is : Rs{main.balance}")