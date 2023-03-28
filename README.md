# Whatsapp-Bulk
Bulk messages for Whatsapp web. Similar behaviour of sending a message to a broadcast list.

It's tested only on Ubuntu 22.04 on the 29/03/2023

## What Whatshapp-Bulk does
Whatsapp-Bulk through the [pywhatkit](https://pypi.org/project/pywhatkit/) library can send a message to several contacts using Whatsapp web.
The message is sent to a single contact per minute because Whatsapp web need some seconds to be opened in the browser.
The script will open a new Whatsapp web session for each contact.

### Example
If it's the 16:23
- First contact will receive the message at 16:24
- Second contact will receive the message at 16:25
- Third contact will receive the message at 16:26

## Idea to solve the issue
Avoid spam block: If the receiver hasn't got your Whatsapp contact already saved, it won't never receive your message sent to the broadcast list.
We want to send Message one-to-one, using either _array_ or _.csv file_ that contains all the contacts that you want send the message to. 

## How to use it
- If you want to send just the image, please refer to [pywhatkit](https://pypi.org/project/pywhatkit/)
- If you want to send just the text, please refer to [pywhatkit](https://pypi.org/project/pywhatkit/)

1) Edit the python script that you want to use
  - Choose the image and the text to send, modifying the content of **img** (line 43) and **msg** variable (line 48)

2) Edit contacts
  - If you are using .csv file edit the /contacts/contacs2.csv or import in the python script *bulk_msg.py* (line 59)
  - If you are using the *bulk_fixed_list.py* modify **contactList** list (line 58)

3) Clear the cache of your default browser (I suggest you to use Firefox)

4) Do the log-in to your whatsapp sender account in the browser

5) Install pywhatkit every time you need it
```pip install pywhatkit```
  
6) Launch the pyhon script choosen
```python3 bulk_msg.py```
or
```python3 bulk_fixed_list.py```
  
7) Uninstall it using
```pip uninstall pywhatkit```
  
***ATTENTION: During the execution don't press any key or use the device, otherwise it won't work***

## Additional Tool
There is also a script to do the steps 5, 6, 7 automatically.
Move in the cloned folder (/Whatsapp-Bulk/)

```sh launch.sh```

## Watch Out
- If the python script is run when the value of local time second is equal to 0 may cause a warning, don't worry, just repeat the command!
- If you need to send a message composed by many rows you must insert it inside triple high quotes as follow: _"""Your multi-rows message"""_
- In the body of your message you can also use Telegram/Whatsapp emoticons, you just need to copy-paste them. (I've used them in Visual Studio Code)
- The .csv file must be composed by just numbers in the first column: (check the /contacts/contacs2.csv)
  - List with phone number without + but with the country prefix before the phone number
  - Example +39 3401398234 must be written in the csv file like 393401398234

## Tools needed for the script launch.sh
- pip
- python3
- figlet

# Tips
Revolut:
[Revolut](https://revolut.me/mattiaw7o9)

Paypal:
[Paypal](https://www.paypal.me/mattiameneghin)
