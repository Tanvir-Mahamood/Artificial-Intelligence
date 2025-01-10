import datetime

date = datetime.date(2024, 12, 13)
today = datetime.date.today()
print(date)
print(today)

time = datetime.time(12, 30, 5)
now = datetime.datetime.now()
print(now)
now = now.strftime("%H:%M:%S %d-%m-%y")
print(time)
print(now)

target_datetime = datetime.datetime(2024, 12, 31, 9, 30, 0)
current_datetime = datetime.datetime.now()
if current_datetime > target_datetime:
    print("Target has passed")
else: 
    print("Not passed")