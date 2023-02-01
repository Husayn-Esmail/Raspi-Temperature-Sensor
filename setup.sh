#!/bin/bash
echo "Creating the virtual environment"
python3 -m venv venv
source venv/bin/activate
echo "cloning and installing dht library"
sudo apt-get install git build-essential python-dev -y
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python3 setup.py install 
echo "Installing requirements.txt"
cd ..
python3 -m pip install -r requirements.txt
echo "done! please run start.sh"

