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
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.environ["OPENWEATHERMAP_API_KEY"]}&units=metric'
        response = requests.get(url)
        data = dict(response.json())
        print(data)
        weather = dict(city=data['name'],
                       main=data['weather'][0]['main'],
                       description=data['weather'][0]['description'],
                       temperature=data['main']['temp'],
                       max=data['main']['temp_max'],
                       min=data['main']['temp_min'],
                       feels=data['main']['feels_like'],
                       humidity=data['main']['humidity'],
                       wind_speed=data['wind']['speed'],
                       pressure=data['main']['pressure'],
                       sunrise=data['sys']['sunrise'],
                       sunset=data['sys']['sunset'],
                       timezone=data['timezone'])
        weather_data.append(weather)
        return render_template('weather.html', city=city, main=data['weather'][0]['main'],
                               description=data['weather'][0]['description'],
                               temperature=data['main']['temp'],
                               max=data['main']['temp_max'], min=data['main']['temp_min'],
                               feels=data['main']['feels_like'],
                               humidity=data['main']['humidity'],
                               wind_speed=data['wind']['speed'],
                               pressure=data['main']['pressure'],
                               sunrise=data['sys']['sunrise'],
                               sunset=data['sys']['sunset'],
                               timezone=data['timezone'])
    return render_template('index.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
