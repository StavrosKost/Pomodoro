import time
import datetime
import ctypes

def countdown(h,m,s):
    #Calculate the total number of seconds
    total_seconds = h * 3600 + m * 60 + s

    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)

        print(timer, end="\r")
        time.sleep(1)
        total_seconds -=1

    print("Bzzzt! Countdown is at zero seconds")
    print("Now lets take a 5 minute break!!")
    
    total_seconds = 5 * 60

    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        ctypes.windll.user32.LockWorkStation()
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -=1
        


if __name__ == "__main__":
    print("Do you want the classic pomodoro or do you want a custom(type 1 for classic and 2 for custom)")
    answer = input()
    if (answer == "1"):
        h=0
        m = 25
        s=0
        countdown(int(h),int(m), int(s))
    elif (answer == "2"):
        h = input("Enter the time in hours: ")
        m = input("Enter the time in minutes: ")
        s = input("Enter the time in seconds: ")
        countdown(int(h),int(m), int(s))
    else:
        print("Ooops you didn't type the number 1 or 2 please try again")

