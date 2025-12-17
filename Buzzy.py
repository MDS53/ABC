import requests

def fetch_current_temperature(city="Bern, CH"):
    """
    Fetches current temperature using OpenWeatherMap API.
    """
    api_key = "8b65933c05a2cbf560499ed7d8351370"  # <-- Replace with your real key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters: q = city, appid = your key, units = metric (Celsius)
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status() # Raise error for bad status codes
        data = response.json()
        
        # Extract the temperature from the JSON structure
        # 
        current_temp = data["main"]["temp"]
        return float(current_temp)
        
    except Exception as e:
        print(f"Weather API Error: {e}")
        return None
inp=input("Enter Location")
k=fetch_current_temperature(inp)
print(f"Temperature in Bern: {k}")
