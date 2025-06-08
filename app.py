from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    city = None
    if request.method == "POST":
        city = request.form.get("city")
        r = requests.get(f'http://api.weatherapi.com/v1/current.json?key=d1717561b5ba4624ac4233140250706&q={city}')
        data = r.json()
        # Extract weather data safely
        location = data.get('location', {})
        current = data.get('current', {})
        weather = {
            'region': location.get('region'),
            'country': location.get('country'),
            'tz_id': location.get('tz_id'),
            'temp_c': current.get('temp_c'),
            'humidity': current.get('humidity'),
            'condition': current.get('condition', {}).get('text')
        }
    return render_template('index.html', city=city, weather=weather)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8000)
