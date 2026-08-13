#practice1
from datetime import datetime
now = datetime.now()
print(now)

#practice2
now = datetime.now()
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")

#practice3
the_datetime = datetime(2025, 12, 25, 14, 30)
print(the_datetime)

#practice4
from datetime import timedelta, datetime
date = datetime(2025, 12, 25)
new_date = date + timedelta(days= 10)
print(new_date)

#practice5
date1 = datetime(2025, 12, 25)
date2 = datetime(2026, 1, 10)
difference = date2 - date1
print(difference)

#practice6
formatted_date = date1.strftime("%d/%m/%Y")
print(formatted_date)

#practice7
date_string = "2025-12-25"
date = datetime.strptime(date_string, "%Y-%m-%d")
print(date)
print(type(date))

#practice8
date = datetime(2025, 12, 25)
day = date.strftime("%A")
print(day)

#practice9
today = datetime(2025, 12, 25)
target = datetime(2026, 1, 1)
days_left = (target - today).days
print(days_left)

#practice10
date = datetime(2025, 12, 25, 14, 30)
time = date.strftime("%H:%M")
print(time)
