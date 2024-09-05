FROM python:3.11-slim

RUN apt update

# Install JetBrains Font
RUN apt install -y curl fontconfig unzip
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/install_manual.sh)"

# Build and Install BrotherLabelPrinterControl Submodule
COPY ./BrotherLabelPrinterControl /BrotherLabelPrinterControl
WORKDIR /BrotherLabelPrinterControl
RUN pip install -r requirements.txt
RUN pip install .

WORKDIR /

COPY ./api/requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./api /app
COPY ./motor /app/motor

WORKDIR /app
ENV PYTHONPATH="/app"

CMD ["fastapi", "run", "main.py", "--port", "80"]
