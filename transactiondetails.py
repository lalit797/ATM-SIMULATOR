import main
def details():
     if not main.transaction:
        print("No transactions yet")
     else:
        for t in main.transaction:
            print(f"transaction is : Rs{t}")
            
     print("Available balance:", main.balance)