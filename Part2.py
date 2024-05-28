currenttime = int(input("Enter the current time in 24 hour format:" ))
if(currenttime<0 or currenttime>24):
    print("Invalid Time.")
else:
    hourstowait = int(input("Enter the number of hours to wait for the alarm: "))
    alarmtime = (currenttime + hourstowait) % 24
    print(f"When the alarm goes off the time will be {alarmtime:2d}:00")