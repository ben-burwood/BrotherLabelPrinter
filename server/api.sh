# Run this Script with the following command:
#/bin/bash -c "$(curl -fsSL https://github.com/benbur98/BrotherLabelPrinter/server/api.sh)"

git clone https://github.com/benbur98/BrotherLabelPrinter.git


cd BrotherLabelPrinter

python -m venv brother-printer-venv

source brother-printer-venv/bin/activate


# Build the BrotherLabelPrinterControl Module

cd BrotherLabelPrinterControl

pip install -r requirements.txt

poetry build

poetry install


# Setup the API Module

cd ../api

pip install -r requirements.txt
