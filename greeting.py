# greeting.py
import datetime

def get_greeting():
    hour = datetime.datetime.now().hour
    if hour < 6:
        return "Good Night!"
    elif 6 <= hour < 12:
        return "Good Morning!"
    elif 12 <= hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"
