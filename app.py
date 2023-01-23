from .temp import get_readings
import flask

# define the app
app = flask.Flask(__name__)

@app.route('/', methods =['GET'])
def index():
    readings = get_readings(4)
    return {"temperature":readings[0], "humidity":readings[1]}

if __name__ == '__main__':
    app.run()