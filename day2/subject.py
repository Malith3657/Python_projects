sub_input = int(input("Enter your marks - "))

if sub_input >= 75:
    print(f"{sub_input} = A")
elif sub_input >= 65:
    print(f"{sub_input} = B ")
elif sub_input >= 55:
    print(f"{sub_input} = C")
elif sub_input >= 35:
    print(f"{sub_input} = S")
elif sub_input < 35:
    print(f"{sub_input} fail")
