import Adafruit_DHT

def get_readings(pin):
    """
    This function takes in the Pin where the data pin of DHT11 sensor
    is connected and returns the temperature and humidity in a tuple.
    """
    if pin == 0:
        raise Exception("Error: pin cannot be 0")
    sensor = Adafruit_DHT.DHT11
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return (humidity, temperature)

if __name__ == '__main__':
    # # init GPIO
    # # GPIO.setwarnings(False)
    # GPIO.setmode(GPIO.BCM)
    # # GPIO.cleanup()
    # # read in data using pin 4
    # instance = dht11.DHT11(4)
    # result = instance.read()
    # # time.sleep(2)
    # print(result.is_valid())
    # print(result.error_code)
    # if result.is_valid():
    #     print("Temperature: %-3.1f C" % result.temperature)
    #     print("Humidity: %-3.1f %%" % result.humidity)
    # else:
    #     print("Error: %d" % result.error_code)
    # GPIO.cleanup()
    print(get_readings(4))




