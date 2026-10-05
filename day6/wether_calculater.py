temp_per_day_for_week = [[0.0 for j in range(3)] for i in range(7)]

for temp in temp_per_day_for_week:
    print(temp)

average_temp = 0.0
hottest_day = 0

while 1:
    user_input = int(input("""\n1. Enter(update) the temperature 
    \n2.Check temperature of specialize time
    \n3.Average temperature of a day
    \n4.Check high temperature of a 7 days
    \n5.Average temperature of week
    \n----------------------------
    Enter your menu option number :
    """))

    if user_input == 1:
        day = int(input("enter the day you want to input the data (1-7) :"))
        hours = int(input("enter the time you want to input the data (1-3) :"))
        temp = int(input("enter the temperature in Celsius :"))

        temp_per_day_for_week[day-1][hours-1] = temp

        print("Temperature updated successfully..")

        for temp in temp_per_day_for_week:
            print(temp)

    elif user_input == 2:
        day = int(input("enter the day you want to input the data (1-7) :"))
        hours = int(input("enter the time you want to input the data (1-3) :"))
        print(f"The temperature for{day} and {hours} is {temp_per_day_for_week[day-1] [hours]}")

    elif user_input == 3:
        day = int(input("enter the day you want to input the data (1-7)"))

        total = 0

        for temp in temp_per_day_for_week[day]:
            total +=temp

        average_temp = total / len(temp_per_day_for_week[day-1])

        print(f"the average temperature is {day} is {average_temp}")

    elif user_input == 4:
        day = int(input("enter the day you want to input the data (1-7) :"))

        temperature = temp_per_day_for_week[day-1]
        hottest_temp = temperature[0]

        for i in range(temperature):
            if temperature[i] >hottest_temp:
                hottest_temp = temperature[i]

        print(f"highest temperature of day {day} was {hottest_temp}")

    elif  user_input == 5:
        total_temp = 0

        for day_temps in temp_per_day_for_week:
            for temp in day_temps:
                total_temp += temp

        print(f"average of the week {total_temp/21} ")

    elif user_input == 6:
        break

    else:
        print("invalid login")



