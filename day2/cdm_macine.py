
# languages = 10 , 20 , 30
#
# user_input = int(input("Enter your pin  number - "))
# select = (input(" select language = "))
# user_withdraw = int(input("withdraw or deposit"))

pin_number = 3657
account_balance = 50000


menu = input("1.check balance"
             "\n2.Withdraw"
             "\n3.deposit"
             "\n4.select menu number")
if menu == "1":
    print(f"Your account balance is {account_balance}")


if menu == "2":
    withdraw_amount = float(input("Enter Withdraw Amount"))
    if withdraw_amount + 5 < account_balance :
            print("please take your money.")
            print(f"your new balance is {account_balance - withdraw_amount - 5}")
    else:
        print("Insufficient Amount.")

if menu == "3":
    deposit_amount = float(input("Enter Deposit Amount"))

    print(f"your new balance is {account_balance + deposit_amount}")






