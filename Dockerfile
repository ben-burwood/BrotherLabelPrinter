FROM python:3.11-slim

RUN apt update
RUN apt install -y usbutils

# Install JetBrains Font
RUN apt install -y curl fontconfig unzip
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/install_manual.sh)"

# Copy Code to Container
COPY ./web /app

RUN pip install --upgrade -r /app/requirements.txt

# Build and Install ServoMotorControl
COPY ./motor /motor
WORKDIR /motor
RUN pip install .
WORKDIR /

# Build and Install BrotherLabelPrinterControl Submodule
#RUN pip install https://github.com/ben-burwood/BrotherLabelPrinterControl/releases/download/0.8.0/brotherlabelprintercontrol-0.8.0-py3-none-any.whl
COPY ./BrotherLabelPrinterControl /BrotherLabelPrinterControl
WORKDIR /BrotherLabelPrinterControl
RUN pip install --upgrade -r requirements.txt
RUN pip install .
WORKDIR /

WORKDIR /app
ENV PYTHONPATH="/app"

CMD ["fastapi", "run", "main.py", "--port", "80"]
