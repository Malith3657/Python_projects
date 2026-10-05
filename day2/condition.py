

password = "test@1996"
username = "test"

username_input = input("Enter your username :")


print(password == username_input)


if username == username_input:
    print("congrats your username matches !")
    password_input = input("Enter your password :")
    if password == password_input:
        print("congracts your password matches as well!")
        print("""
        Wellcome to our secret game
        1) press 1 to start the game 
        """)
        user_input = input("choice :")
        if user_input == "1":
            print("sanke game is loading........")
        else:
            print("Error")
    else:
        print("Entered  password is incorrect")

else:
    print("Entered username is incorrect")



