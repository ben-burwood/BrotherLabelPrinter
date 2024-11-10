#!/bin/bash

python3 -m venv venv

source venv/bin/activate

source font.sh

cd BrotherLabelPrinterControl
pip install --no-cache-dir --upgrade -r requirements.txt
pip install --no-cache-dir .  # Build and Install BrotherLabelPrinterControl Submodule

cd ../motor
pip install --no-cache-dir .  # Build and Install ServoMotorControl Submodule

cd ../web
pip install --no-cache-dir --upgrade -r requirements.txt

sudo cp ../label-printer.service /etc/systemd/system/label-printer.service

sudo systemctl daemon-reload
sudo systemctl enable label-printer.service
sudo systemctl start label-printer.service

sudo systemctl status label-printer.service
