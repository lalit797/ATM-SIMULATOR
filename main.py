import time
import main
from checkbalance import check_balance
from withdrawl import withdrawl_money
from depositemoney import money_deposite
from transactiondetails import details
from generatepin import generate
pin = 5623
transaction=[]
balance = 2000
set_otp = 9876
set_card_no= 123456
def main():
 print("WELCUM TO MY ATM SIMULATOR😘😘")
 time.sleep(2)
 attempts = 3
 max_attempts= 0
 while max_attempts <= attempts:
        user_pin= int(input("enter your valid atm pin:"))
        if user_pin == pin:
            while True:
                print("\npress 1. for check balance:")
                print("\npress 2. for check trancsaction details:")
                print("\npress 3. for deposite your money:")
                print("\npress 4. to withdraw your money")
                print("\nprees 5 to generate  new pin :")
                print("\n press 6. for exit | cancel process ")

                choose= int(input("enter"))

                if choose == 1:
                    check_balance()
                elif choose ==2:
                    details()
                elif choose == 3:
                    money_deposite()
                elif choose == 4:
                    withdrawl_money()
                elif choose ==5:
                    generate()
                elif choose == 6:
                    print("thanks for using my ATM SIMULATOR")
                    break 
                else:
                    print("WRONG NO ENTER , AUUKAT MEIN 😤😤😤")
        else: 
            print("wrong pin , YAAD KR KE AA 🫡🫡🫡🫡🫡")
            attempts -=1
        if attempts == 0:
            print("LIMIT EXCEEDED , card BLOCKED!!!")


main()