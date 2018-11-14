#!/usr/bin/env bash

## Variables
path_to_dir="${HOME}/mqttflask"

## Functions
msg_c() { # Output messages in color! :-)
    local OPTIND=1; local o; local newline="1"; local CHOSEN_COLOR; local RESET=$(tput sgr0);
    while getopts ":ndrgbcmya" o; do
        case "${o}" in
            n) newline="0" ;; # no new line
            d) CHOSEN_COLOR=$(tput bold) ;;    # bold
            r) CHOSEN_COLOR=$(tput setaf 1) ;; # color red
            g) CHOSEN_COLOR=$(tput setaf 2) ;; # color green
            b) CHOSEN_COLOR=$(tput setaf 4) ;; # color blue
            c) CHOSEN_COLOR=$(tput setaf 6) ;; # color cyan
            m) CHOSEN_COLOR=$(tput setaf 5) ;; # color magenta
            y) CHOSEN_COLOR=$(tput setaf 3) ;; # color yellow
            a) CHOSEN_COLOR=$(tput setaf 7) ;; # color gray
            \? ) echo "msg_c() invalid option: -${OPTARG}"; return ;;
        esac
    done
    shift $((OPTIND - 1))
    if [ ! -z $CHOSEN_COLOR ] && [ $newline == "1" ]; then
        echo -e "${CHOSEN_COLOR}${1}${RESET}"
    elif [ ! -z $CHOSEN_COLOR ] && [ $newline == "0" ]; then
        echo -ne "${CHOSEN_COLOR}${1}${RESET}"
    elif [ -z $CHOSEN_COLOR ] && [ $newline == "0" ]; then
        echo -n "${1}"
    else
        echo "${1}"
    fi
}

####################################################################################################

echo ""
echo ""
msg_c -b "I will now move your set up files into position"
echo ""
echo ""

echo ""
msg_c -c "Move the nginx config file into position"
#----------------------------------------------
if [ -f "${path_to_dir}/setup/mqttflask.nginx.conf" ]; then
    if [ -d "/etc/nginx/sites-available/" ]; then
        sudo cp "${path_to_dir}/setup/mqttflask.nginx.conf" "/etc/nginx/"
    else
        msg_c -r "It seems like nginx is not installed..."
    fi
else
    msg_c -r "Couldn't find the nginx config file..."
fi
#----------------------------------------------
msg_c -c "done!..."
echo ""


echo ""
msg_c -c "Move the mqttflask service into position"
#----------------------------------------------
if [ -f "${path_to_dir}/setup/mqttflask.service" ]; then
    if [ -d "/etc/systmd/system/" ]; then
        sudo cp "${path_to_dir}/setup/mqttflask.service" "/etc/systmd/system/"
    else
        msg_c -r "I cannot locate the /etc/systmd/system/ directory..."
    fi
else
    msg_c -r "Couldn't locate the mqttflask service file..."
fi
#----------------------------------------------
msg_c -c "done!..."
echo ""


echo ""
echo ""
msg_c -b "Done moving you setup files into position!"
echo ""
echo ""
