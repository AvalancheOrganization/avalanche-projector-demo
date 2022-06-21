#!/bin/bash
echo " "
echo " # Testing python install"
which python3
python3 --version
pip3 install --upgrade pip
pip3 install python-vlc

echo " "
echo " # Testing python libraries"
python3 -c "import RPi.GPIO as GPIO"

echo " "
echo " # Linking GPIO"
read -p ">> Pin of the button: " button_pin
echo $button_pin
echo "button_pin = $button_pin" > config.py

echo " "
echo " # Linking data"
read -p ">> Path to the main file: " path_main
echo $path_main
echo "path_main = $path_main" >> config.py

read -p ">> Path to the second file: " path_second
echo $path_second
echo "path_second = $path_second" >> config.py