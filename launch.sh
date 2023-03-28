#!/bin/bash
figlet Whatsapp-Bulk

# Install packages
pip install pywhatkit

# Launch python script
figlet Script launched
python3 bulk_msg.py

# Uninstall packages
pip uninstall pywhatkit --y

figlet Well Done