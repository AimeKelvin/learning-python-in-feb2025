import datetime


current_time = datetime.datetime.now()


current_hour = current_time.hour


if 5 <= current_hour < 12:
    print("Good Morning!")
elif 12 <= current_hour < 18:
    print("Good Afternoon!")
else:
    print("Good Night!")