import pywhatkit
import datetime
import time


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
i'm using your script fixed list.
Thank you!
bye!"""

# Contacts list
contactList = [393401398232, 393333333333]

# Send Message with Caption
for num in contactList:
    if minute < 59:
        minute=minute+1
    if min == 59:
            min == 0
            hour=hour+1
    cellphone = '+'+ str(num)


    print(cellphone)
    pywhatkit.sendwhats_image(cellphone, img , msg)
    count = count +1
    print(str(count) + '° operation done +'+ cellphone + ' at ' + str(hour) + ':' + str(minute))
    print(" ")

time.sleep(5)
print(" ")
print(" ")
print(str(count)+" messages sent, operation complete succesfully")
print(" ")
print(" ")