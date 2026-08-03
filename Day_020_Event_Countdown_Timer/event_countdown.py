from datetime import datetime
import time

text = input("Event date and time (YYYY-MM-DD HH:MM): ")

event = datetime.strptime(text,"%Y-%m-%d %H:%M")

while True:
    remaining = event - datetime.now()
    if remaining.total_seconds() <= 0:
        print("The event has started!")
        break
    days = remaining.days
    hours, remainder = divmod(remaining.seconds,3600)
    minutes, seconds = divmod(remainder,60)
    print(f"\r{days}d {hours:02}h {minutes:02}m {seconds:02}s ",end= "")
    time.sleep(1)