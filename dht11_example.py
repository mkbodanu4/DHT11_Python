import wiringpi2 as wpi
import dht11
import time
import datetime

# initialize GPIO
wpi.wiringPiSetupGpio()

# read data using pin 235, WiringPi GPIO #12
instance = dht11.DHT11(pin = 235)

while True:
	result = instance.read()
	if result.is_valid():
		print("Last valid input: " + str(datetime.datetime.now()))
		print("Temperature: %d C" % result.temperature)
		print("Humidity: %d %%" % result.humidity)
    		
	time.sleep(1)
