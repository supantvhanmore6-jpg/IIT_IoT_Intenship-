import datetime

now = datetime.datetime.now()

print("Current date and time:", now)

day_of_week = now.strftime("%A")
print("Day of the week:", day_of_week)
