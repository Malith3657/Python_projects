current_celsius = float(input("Enter celsius : "))

kelvin_temp = current_celsius + 273.15
fahrenheit_temp = (current_celsius * 9 / 5) + 32

print(f"{current_celsius} in celsius equal to \n{kelvin_temp}"
      f"in kelvin & \n{fahrenheit_temp} in fahrenheit ")