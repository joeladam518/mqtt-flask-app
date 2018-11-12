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
msg_c -b "I will now start provisioning your local development environment"
echo ""
echo ""


echo ""
msg_c -c "Update and Upgrade"
#----------------------------------------------
cd ${HOME} && sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove -y
#----------------------------------------------
msg_c -c "done!..."
echo ""

echo ""
msg_c -c "Installing your bashrc and vimrc"
#----------------------------------------------
if [ ! -d "${HOME}/repos" ]; then
    echo ""
    msg_c -c "Creating the repos directory in the home folder"
    #----------------------------------------------
    cd "$HOME" && mkdir repos
    #----------------------------------------------
    msg_c -c "done!..."
    echo ""
fi

if [ ! -f "${HOME}/repos/myvimrc/.vimrc" ]; then
    echo ""
    msg_c -c "Cloning the joeladam518/myvimrc github repo"
    #----------------------------------------------
    cd "${HOME}/repos" && git clone "https://github.com/joeladam518/myvimrc.git"
    #----------------------------------------------
    msg_c -c "done!..."
    echo ""
fi

if [[ ! -f "${HOME}/.bashrc.old" && -f "${HOME}/.bashrc" ]]; then
    echo ""
    msg_c -c "Cloning the joeladam518/mybashrc github repo"
    #----------------------------------------------
    cd "${HOME}/repos" && git clone "https://github.com/joeladam518/mybashrc.git"
    #----------------------------------------------
    msg_c -c "done!..."
    echo ""
fi
#----------------------------------------------
msg_c -c "done!..."
echo ""


echo ""
msg_c -c "Install Some Basic Packages."
#----------------------------------------------
cd "${HOME}" && sudo apt-get install -y vim git tree htop tmux ntp ntpdate
#----------------------------------------------
msg_c -c "done!..."
echo ""


echo ""
msg_c -c "Install nginx"
#----------------------------------------------
cd "${HOME}" && sudo apt-get install -y nginx
#----------------------------------------------
msg_c -c "done!..."
echo ""


echo ""
msg_c -c "Fix the UTC time."
#----------------------------------------------
sudo service ntp stop
sudo ntpdate -s time.nist.gov
sudo service ntp start
#----------------------------------------------
msg_c -c "done!..."
echo ""


echo ""
msg_c -c "Install python needs"
#----------------------------------------------
cd "${HOME}" && sudo apt-get install -y python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
#----------------------------------------------
msg_c -c "done!..."
echo ""


echo ""
msg_c -c "Install python virtual env"
#----------------------------------------------
cd "${HOME}" && sudo apt-get install -y python3-venv
#----------------------------------------------
msg_c -c "done!..."
echo ""


echo ""
msg_c -c "Setup the python venv"
#----------------------------------------------
cd "${path_to_dir}" && python3 -m venv flaskenv
#----------------------------------------------
msg_c -c "done!..."
echo ""

# echo ""
# msg_c -c "install python dependencies"
# #----------------------------------------------
# pip install wheel
# pip install uwsgi flask flask_restful
# pip install -U python-dotenv
# #----------------------------------------------
# msg_c -c "done!..."
# echo ""


# echo ""
# msg_c -c "Running: ln -sf .env-local .env"
# #----------------------------------------------
# #cd "$path_to_dir"/site && ln -sf .env-local .env
# #----------------------------------------------
# msg_c -c "done!..."
# echo ""


# echo ""
# msg_c -c "Running: Node install"
# #----------------------------------------------
# cd "$path_to_dir"/site && npm install
# #----------------------------------------------
# msg_c -c "done!..."
# echo ""


echo ""
echo ""
msg_c -b "You're local development environment is now provisioned."
echo ""
echo ""
