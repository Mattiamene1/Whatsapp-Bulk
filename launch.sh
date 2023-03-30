#!/bin/bash
figlet Whatsapp-Bulk

# Install package
pip install pywhatkit

# Launch copyq in other terminal
gnome-terminal -- copyq

# Launch python script
figlet WhatsApp-Bulk csv launched && python3 bulk_msg.py
#figlet WhatsApp-Bulk Fixed List launched && python3 bulk_fixed_list.py

# Uncomment the desired py script
#python3 bulk_msg.py
#python3 bulk_fixed_list.py

# Uninstall package
pip uninstall pywhatkit --y

figlet Well Done
