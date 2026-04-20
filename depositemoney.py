import main
import time
def money_deposite():
    user_deposite= int(input("enter amount you want to deposite"))
    print("INSERT YOUR MONEY..")
    time.sleep(2)
    main.balance = main.balance + user_deposite
    main.transaction.append(user_deposite)
    print(f"now your balance is : Rs{main.balance}")
