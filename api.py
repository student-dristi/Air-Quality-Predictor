import requests

def fetch_air_quality_data(lat, lon, api_key):
    api_url = f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        components = data["list"][0]["components"]
        aqi_index = data["list"][0]["main"]["aqi"] * 100
        return {
            "PM2.5": components["pm2_5"],
            "NO2": components["no2"],
            "CO": components["co"],
            "SO2": components["so2"],
            "AQI": aqi_index
        }
    else:
        return None
