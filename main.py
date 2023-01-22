import flask
import time
import Adafruit_DHT
from livereload import Server

app = flask.Flask(__name__)
class EnvironmentSensor:
    def __init__(self, sensor_pin):
        self.humidity = None
        self.temperature = None
        self.sensor_name = Adafruit_DHT.DHT11
        self.sensor_pin = sensor_pin
        
    def read_sensor(self, sleep_time: int):
        time.sleep(sleep_time)
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor_name, self.sensor_pin) # read respective values from sensor and save in vars
    
    def get_temperature(self):
        if self.temperature == None:
            raise Exception("Temperature has not been updated yet! call read_sensor first!")
        return self.temperature

    def get_humidity(self):  
        if self.humidity == None:
            raise Exception("Humidity has not been updated yet! call read_sensor first!")
        return self.humidity

@app.route('/', methods=['GET'])
def index():
    sensor_pin = 17
    sensor = EnvironmentSensor(sensor_pin)
    sleep_time = 2
    sensor.read_sensor(sleep_time)
    temperature = sensor.get_temperature()
    humidity = sensor.get_humidity() 
    return flask.render_template('index.html', temperature=temperature, humidity=humidity)

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve(host='0.0.0.0')
