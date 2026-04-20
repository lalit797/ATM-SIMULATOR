import main
import time
def generate():
    u_c =int(input(''' 
press 1. to generate your pin by OTP
press 2. to generate your pin by atm card no.
'''))
    
    if u_c==1:
        otp = int(input("enter 4 digit otp:"))
        time.sleep(1)
        if otp==main.set_otp:
            print("enter the new pin(4-digit) .you want to generate")
            new_pin= int(input("enter"))
            if new_pin !=main.pin :
                main.pin = new_pin

        print(f"new pin is : {new_pin}") 
    elif u_c==2: 
        card_no= int(input("enter last 6 digit of your card:"))
        if card_no == main.set_card_no:
            print("enter new pin you want to generate:")
            new_pin_card_no= int(input("enter"))
            main.pin = new_pin_card_no
        print(f"new pin is :{new_pin_card_no}")
    else:
        print("wrong no. entered...")        


