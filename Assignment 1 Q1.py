from datetime import datetime
#Write a simple bash script that asks the user if they want to know today's date or the current time and gives them whichever choice they ask for.  

res = input("Do you want today's date or time? ")
print("response:", res, '\n')
today = datetime.now()
time = datetime.now()
current_time = time.strftime("%H:%M:%S")
current_date = today.strftime("%m/%d/%Y")

if res=="date":
    print ("Today's date:",current_date)
elif res == "time":
    print ("Current time:", current_time)