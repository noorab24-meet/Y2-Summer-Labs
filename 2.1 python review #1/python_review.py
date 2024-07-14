import random
temperatures = []
for i in range(7):
    temperatures.append(random.randint(26, 40))

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

evendays = []
for i in range(len(temperatures)):
    if temperatures[i] % 2 == 0:
        evendays.append(days_of_the_week[i])

count = len(evendays)

print("Generated Temperatures:", temperatures)
print("Days of the week:", days_of_the_week)

print("\nDays with even temperatures:")
for day in evendays:
    print(day)

average_temp = sum(temperatures) / len(temperatures)
print(f"\nAverage temperature of the week: {average_temp:.2f}")

highest_temp = max(temperatures)
lowest_temp = min(temperatures)
highest_temp_day = days_of_the_week[temperatures.index(highest_temp)]
lowest_temp_day = days_of_the_week[temperatures.index(lowest_temp)]

print(f"\nHighest temperature of the week: {highest_temp} on {highest_temp_day}")
print(f"Lowest temperature of the week: {lowest_temp} on {lowest_temp_day}")

above_avg = []
for temp in temperatures:
    if temp > average_temp:
        above_avg.append(temp)

print("Temperatures above average:")
for temp in above_avg:
    print(temp)


#I_Can_Say_Finaly!!
print("Weekly Temperature Report")
print("--------------------------")
print("Temperatures for the week:", temperatures)
print("Good days for Shelly (even temperatures):")
for i in range(len(temperatures)):
    if temperatures[i] % 2 == 0:
        print(f"  {days_of_the_week[i]}: {temperatures[i]}")
print("Highest temperature:", highest_temp, "on", highest_temp_day)
print("Lowest temperature:", lowest_temp, "on", lowest_temp_day)
print("Average temperature:", f"{average_temp:.2f}")
print("Days with temperatures above average:")
for temp in above_avg:
    temp_index = temperatures.index(temp)
    print(f"  {days_of_the_week[temp_index]}: {temp}")
