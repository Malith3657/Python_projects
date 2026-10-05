def addition(num_1, num_2):
    return (num_1 + num_2)


def substaction(num_1, num_2):
    return (num_1 - num_2)


def multiplication(num_1, num_2):
    return (num_1 * num_2)


def division(num_1, num_2):
    if num_2 == 0:
        return 'cannot br division by zero'

    return num_1 / num_2


def take_user_input():
    first_num = int(input("Enter first number - : "))
    second_num = int(input("Enter second number - : "))
    return first_num, second_num


while True:
    operation = input("Enter operation to continue (+,-,/,*) : ")

    if operation == "+":
        val1, val2 = take_user_input()
        print(f"Result is {addition(val1, val2)}")
    elif operation == "-":
        val1, val2 = take_user_input()
        print(f"Result is {substaction(val1, val2)}")
    elif operation == "*":
        val1, val2 = take_user_input()
        print(f"Result is {multiplication(val1, val2)}")
    else:
        val1, val2 = take_user_input()
        print(f"Result is {division(val1, val2)}")