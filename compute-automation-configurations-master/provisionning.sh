#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y python3-pip
sudo python3 -m pip install azure-servicebus
sleep 30s
sudo python3 /var/lib/waagent/custom-script/download/1/test.py