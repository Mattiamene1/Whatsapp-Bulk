# Script made by Mattia Meneghin https://github.com/Mattiamene1 https://mattiameneghin.tk
# Python Bulk message for all the contacts in Business WA account
# Idea: Avoid spam block: If the receiver hasn't got your WA contact already saved, it won't never receive your broadcast list message
# Send Message one-to-one with pywhatkit library, using csv file that contains all the numbers
# Good way to use it is to uninstall pywhatkit using the command    pip uninstall pywhatkit
# Then re-intall it using                                           pip install pywhatkit
# clear the cache of your default browser (I suggest you to use firefox)
# Do the log in to your whatsapp sender account
# Run the script with the command                                   python3 bulk_msg.py
# Attention: During the execution don't press any key or use the device

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

#Print date in string
print("")
print(str(year)+'/'+str(month)+'/'+str(day)+' at '+str(hour)+':'+str(minute)+':'+str(second))
time.sleep(5)

# Sending Messages
# One contact per minute because WA web need some seconds to open the web client
# If now it is the 16:23
#       First contact will receive the message at 16:24
#       Second contact will receive the message at 16:25
#       Third contact will receive the message at 16:26

# Counter
count = 0

# Select image
img = "images/jetmarket3/main.jpg"

# Type your message
# Note 1: If your message isn't composed by just 1 row, use triple """ """ to use multiple rows
# Note 2: If you want you can copy-paste any emoticons from Telegram/Whatsapp in the code (i0m using visual studio code)
msg = """Dear Mattia,

i'm using your script csv import.
Thank you!

bye!"""

# Import the csv file containing the phone numbers, using the right path
# List with phone number without +, but with the country prefix before the phone number
# Note: example +39 3401398234 must be imported like 393401398234 

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