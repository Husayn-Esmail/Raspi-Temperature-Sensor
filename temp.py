import RPi.GPIO as GPIO
import dht11


if __name__ == '__main__':
    # init GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    # read in data using pin 4
    instance = dht11.DHT11(pin=4)
    result = instance.read()
    if result.is_valid():
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
    else:
        print("Error: %d" % result.error_code)