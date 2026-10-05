

password = "5000"
attempts = 3

while attempts > 0:
    user_Password = input("Enter Your Password =")

    if user_Password == password:
        print("Logging Successful")
        break

    else:
        print("wrong Password . Again ")
        attempts -= 1
        print(f"You have {attempts} attempts.")

if attempts == 0:
    print("Your Account has been locked")

