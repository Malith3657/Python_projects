username = "Malith"
password = "2006"
have_logged = input("Have you logged before ? (yes/no)") == "yes"

for i in range(3):
    if not have_logged:
        print("Please loggin frist.")

        user_name = input("Enter your user name :")
        user_password = input("Enter your password :")
        if user_name == "Malith" and user_password == "2006":
            have_logged = True
            print("Welcome")
        else:
            print("Try again")

    else:
        print("Welcome Back")
        break
else:
    print("Account locked")