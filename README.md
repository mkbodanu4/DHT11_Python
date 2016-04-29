# DHT11 Python library

This simple class can be used for reading temperature and humidity values from DHT11 sensor on Odroid-C2.

# Requirements

This class require hardkernel's WiringPi2-Python lib https://github.com/hardkernel/WiringPi2-Python

# Pins

Before starting please check correct pin # at http://www.hardkernel.com/main/products/prdt_info.php?g_code=G145457216438&tab_idx=2, this class uses "Export GPIO#"

# Usage

1. Instantiate the `DHT11` class with the pin number as constructor parameter.
2. Call `read()` method, which will return `DHT11Result` object with actual values and error code.

For example:

```python
import wiringpi2 as wpi
import dht11

# initialize GPIO
wpi.wiringPiSetupGpio()

# read data using pin 235, WiringPi GPIO #12
instance = dht11.DHT11(pin = 235)
result = instance.read()

if result.is_valid():
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)
```

For working example, see `dht11_example.py` (you probably need to adjust pin for your configuration)