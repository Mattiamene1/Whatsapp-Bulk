#!/bin/bash
# Author: Mattia Meneghin
# Run the bulk

# Functions
selection() {
    printf "\n"
    printf "    \e[100m\e[1;77m:: Please choose the script:                        ::\e[0m\n"
    printf "    \e[1;92m[\e[0m\e[1;77m0\e[0m\e[1;92m]\e[0m\e[1;91m EXIT            ::\e[0m\n" 
    printf "    \e[1;92m[\e[0m\e[1;77m1\e[0m\e[1;92m]\e[0m\e[1;91m Fixed List      ::\e[0m\n"                                
    printf "    \e[1;92m[\e[0m\e[1;77m2\e[0m\e[1;92m]\e[0m\e[1;91m Contacts List   ::\e[0m\n"
    printf "\n"
    read -p "    Choose an option: " option

    if [[ $option == 1 ]]; then
        fixed

    elif [[ $option == 2 ]]; then
        contanscsv

    elif [[ $option == 0 ]]; then
        exit

    else
        printf "\e[1;93m [!] Invalid option!\e[0m\n"
        selection
    fi

}

contanscsv(){
    printf "    \e[100m\e[1;77m:: WhatsApp-Bulk csv launched                       ::\e[0m\n"
    printf "\n"
    gnome-terminal --title="Contacts List" -- python3 $HOME/Whatsapp-Bulk/bulk_msg.py
}

fixed(){
    printf "    \e[100m\e[1;77m:: WhatsApp-Bulk fixed list launched                ::\e[0m\n"
    printf "\n"
    gnome-terminal --title="Fixed List" -- python3 $HOME/Whatsapp-Bulk/bulk_fixed_list.py
}

banner() {
    clear
    printf "   \n"
    printf "   \e[100m\e[1;77m:: Whatsapp bulk messages                             ::\e[0m\n"
    printf "   \e[100m\e[1;77m:: Author: Meneghin Mattia                            ::\e[0m\n"
    printf "   \n"
}

banner

bash ./scripts/install.sh
sleep 1

# Select Mode
selection