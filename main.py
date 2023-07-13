import requests
import os
import dotenv
from flask import Flask, render_template, request

dotenv.load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index(weather_data=[]):
    if request.method == 'POST':
        city = request.form.get('city')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.environ["OPENWEATHERMAP_API_KEY"]}&units' \
              f'=metric'
        response = requests.get(url)
        data = dict(response.json())
        weather = dict(city=data['name'], main=data['weather'][0]['main'], temperature=data['main']['temp'],
                       max=data['main']['temp_max'], min=data['main']['temp_min'], feels=data['main']['feels_like'])
        weather_data.append(weather)
        return render_template('weather.html', city=city, main=data['weather'][0]['main'],
                               temperature=data['main']['temp'],
                               max=data['main']['temp_max'], min=data['main']['temp_min'],
                               feels=data['main']['feels_like'])
    return render_template('index.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
