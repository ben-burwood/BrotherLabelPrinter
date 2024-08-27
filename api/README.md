# Brother Printer API

## Config

The YAML Configuration file - located at `config.yaml` - is used to configure the Brother Printer API. The following is an example of the configuration file:

```yaml
backend: usb
printer: PTP_700
media: W12
font: /path/to/font.ttf
```

| Configuration | Description                          | Required | Options                                          |
|---------------|--------------------------------------|----------|--------------------------------------------------|
| backend       | Backend Type for Printer Connection  | True     | usb, bluetooth, wifi                             |
| printer       | Printer Model                        | True     | PTP_700, PTP_750W, PTP_H500, PTP_E500, PTP_E550W |
| media         | Printer Media (Tape) Inserted        | False    | W3_5, W6, W9, W12, W18, W24                      |
| font          | Truetype Font Path to use by Default | False    |                                                  |

## API

`fastapi run` - Starts the FastAPI server

## Endpoints

### Print

`POST /print`

#### Request Body:

```json
{
  "text": "Hello World",
  "height": 50,
  "font": "font.ttf",
  "padding": {
    "top": 0,
    "right": 0,
    "bottom": 0,
    "left": 0
  }
}
```