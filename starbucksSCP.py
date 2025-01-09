global expresso, latte, macchiato, redeye, undertoe
expresso = 1.50
latte = 1.50
macchiato = 1.25
redeye = 1.00
undertoe = 1.00

def display():
    print("Menu \n"
          "1. Expresso \n"
          "S = 0.99$ M = 1.99$ L = 2.99$  \n"
          "2. Latte \n"
          "S = 0.99$ M = 1.99$ L = 2.99$  \n"
          "3. Maccchiato \n"
          "S = 0.99$ M = 1.99$ L = 2.99$  \n"
          "4. Redeye \n"
          "S = 0.99$ M = 1.99$ L = 2.99$  \n"
          "5. UnderToe \n"
          "S = 0.99$ M = 1.99$ L = 2.99$  \n")

def payment():
    print("1. Cash \n"
          "2. Card \n")
    payment_type = int(input("What would you like to pay with: "))
    if payment_type == 1:
        print("You have to chose cash amount")
        print("Your total will be ", total,"$")
        payment = int(input("Enter the payment: "))
        change = payment - total
        print("Thank you for your payment. The change is", change, "$")
        print("Goodbye")
    elif payment_type == 2:
        print("You have chosen card payment type")
        print("Your total will be", total,"$")
        input("Please input your card number. (XXXX-XXXX-XXXX-XXXX): ")
        input("Please input the expiration date. (XX/XX): ")
        input("Please input the security code. (XXX): ")
        print("Thank you for your payment. Goodbye. ")

def size():
    global amount
    size2 = int(input("What size would you like?: "))
    if size2 == 1:
        return(0.99)
    elif size2 == 2:
        return(1.99)
    elif size2 == 3:
        return (2.99)
    else:
        print("You have made an invalid choice. Please try again.")
        return(0.99)
def choice():
    global total
    total = 0
    order = 1
    while order == 1:
        coff1 = int(input("Which coffee would you like:"))
        if coff1 == 1:
            print("You have chosen Expresso.")
            total = total + expresso + size()
        elif coff1 == 2:
            print("You have chosen Latte.")
            total = total + latte + size()
        elif coff1 == 3:
            print("You have chosen Macchiato.")
            total = total + macchiato + size()
        elif coff1 == 4:
            print("You have chosen Red Eye.")
            total = total + redeye + size()
        elif coff1 == 5:
            print("You have chosen Under Toe.")
            total = total + undertoe + size()
        else:
            print("You made an invalid choice. Try again.")
        order = int(input("Would you like anything else? (Press 1 to continue your order.): "))
        if order == 1:
            choice()
        elif order == 0:
            return total
        payment()
        break
display()
choice()
