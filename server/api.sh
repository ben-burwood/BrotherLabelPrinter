
python -m venv brother-printer-venv

source brother-printer-venv/bin/activate


# Build the BrotherLabelPrinterControl Module

cd BrotherLabelPrinterControl

pip install -r requirements.txt

poetry install


# Setup the API Module

cd ../api

pip install -r requirements.txt
