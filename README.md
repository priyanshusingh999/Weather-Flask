# Weather Flask App

A simple Flask web application that allows users to search for current weather information by city. The app fetches real-time weather data from the WeatherAPI service and displays it in a clean, user-friendly interface.

## Features

- Search weather by city name
- Displays region, country, time zone, temperature (°C), humidity, and weather condition
- Responsive design using Bootstrap 5

## Installation

1. Clone the repository or download the project files.

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/Scripts/activate   # On Windows
# or
source venv/bin/activate       # On macOS/Linux
```

3. Install the required Python packages:

```bash
pip install flask requests
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to:

3. Enter a city name in the search bar and click "Search" to view the current weather details.

## Project Structure

```
Projects/Weather-Flask/
├── app.py              # Main Flask application
├── static/
│   └── style.css       # CSS styles for the app
└── templates/
    └── index.html      # HTML template for the home page
```

## API

This app uses the [WeatherAPI](https://www.weatherapi.com/) to fetch current weather data. An API key is embedded in the app.py file for demonstration purposes.

## Notes

- The app runs with debug mode off.
- Ensure you have an active internet connection to fetch weather data from the API.

## License

This project is open source and available under the MIT License.
