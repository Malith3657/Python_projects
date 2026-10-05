sleep_hours = []
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

for i in range(7):
    hour = int(input(f"Enter your slept hours at {days[i]} ="))
    sleep_hours.append(hour)

print(sleep_hours)

total = 0

for i  in sleep_hours:
    total = total + i
print(f"\nYour weekly slept hours was  - {total}")

