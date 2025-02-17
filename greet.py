import datetime

day = datetime.datetime.now()

hour = day.hour
name =  input("What is your name?: ")

if 5 <= hour < 12:
    print(f"Rise n shine {name} ☀️")
elif 12 <= hour < 18:
    print(f"Sup {name} its the middle of the day. 🦾")
else :
    print(f"Its late Mr {name}, time to get some sleep, 🥱")