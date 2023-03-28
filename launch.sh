#!/bin/bash
figlet Whatsapp-Bulk

# Install package
pip install pywhatkit

# Launch python script
figlet Script launched
python3 bulk_msg.py

# Uninstall package
pip uninstall pywhatkit --y

figlet Well Done
