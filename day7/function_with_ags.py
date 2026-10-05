def print_full_name(first_name,last_name ):

    print(f"Full name is :- {first_name} \n last name is :- {last_name}")

print_full_name("Malith","Madushan") #positional argument passing

print("=====================")

print_full_name(first_name="Malith",last_name="Madushan")#keyword argument passing

print("====================")

def multiply(a,b):
    print(f"Multiplying - {a} and {b} ")
    return a * b

result = multiply(10,22)

print(result)