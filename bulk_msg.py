import pywhatkit
import datetime
import time
import csv

# Date in datetime
now = datetime.datetime.now()
# Date in integer
year = int(now.strftime('%Y'))
month = int(now.strftime('%m'))
day = int(now.strftime('%d'))
hour = int(now.strftime('%H'))
minute = int(now.strftime('%M'))
second = int(now.strftime('%S'))

# Print date in string
print("")
print(str(year)+'/'+str(month)+'/'+str(day)+' at '+str(hour)+':'+str(minute)+':'+str(second))
time.sleep(5)

# Counter
count = 0

# Select image
img = "images/jetmarket3/main.jpg"

# Type your message
msg = """Dear Mattia,

i'm using your script csv import.
Thank you!

bye!"""

# Send Message with Caption
with open('contacts/contacts2.csv') as csvfile:
    contactList = csv.reader(csvfile)
    print(" ")
    for num in contactList:
        if minute < 59:
            minute=minute+1
        
        if min == 59:
                min == 0
                hour=hour+1

        cellphone = '+'+ str(num[0])
        print(cellphone)
        pywhatkit.sendwhats_image(cellphone, img , msg)
        count = count +1
        print(str(count) + '° operation done +'+ cellphone + ' at ' + str(hour) + ':' + str(minute))

time.sleep(5)
print(" ")
print(" ")
print(str(count)+" messages sent, operation complete succesfully")
print(" ")
print(" ")