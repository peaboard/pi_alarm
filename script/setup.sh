#!/bin/bash
# --
# Script to install python packages needed to run pi_alarm
# Note that you may need to run this script as root
# --

# Required Python Libraries

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

if [[ "$VIRTUAL_ENV" = "" ]]; then
   echo "It is suggested that you run setup script through virtualenv."
   read -p "Do you want to continue? Y/n  " choice
   case "$choice" in
     y|Y ) echo "Continuing..";;
     n|N ) exit 1;;
     * ) echo "invalid";;
   esac
fi

python_libs=(
    'flask==0.10.1'             # The web framework we're using
    'Mako==0.9.0'               # Mako templates for the site
    'flask-mako'                # Flask integration for Mako
    'uwsgi'                     # for serving the site
    'Flask-BasicAuth'           # for locking down the site
    'python-crontab==2.1.1'     # for accessing the crontab
    'RPi.GPIO'                  # for driving the GPIO pins on the Pi
    'radiopy'                   # for Web Radio
)

# Install each of the libraries
for i in "${python_libs[@]}"; do
    pip install $i
done

linux_packages=(
    'mpd'
    'mpc'
)

apt-get update

for i in "${linux_packages[@]}"; do
    apt-get install -y $i
done
