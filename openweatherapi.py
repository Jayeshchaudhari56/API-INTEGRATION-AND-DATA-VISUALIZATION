
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

API_KEY = 'd2933251cc69cf5f01177cd31adbe6a6' 
CITY = 'pune'

def fetch_forecast_data(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    if 'list' not in data:
        print("Error: API key may be invalid or city not found.")
        print("Full response:" ,data)
        exit()

    forecast_data = []
    for entry in data['list']:
        forecast_data.append({
            'datetime': datetime.strptime(entry['dt_txt'], "%Y-%m-%d %H:%M:%S"),
            'temperature': entry['main']['temp']
        })

    return pd.DataFrame(forecast_data)
def plot_forecast(df, city):
    plt.figure(figsize=(10, 5))
    sns.lineplot(x='datetime', y='temperature', data=df , marker='o')
    plt.title(f'Temperature forcast for {city} (Next 5 Days)', fontsize=13)
    plt.xlabel('Date & Time')
    plt.ylabel('Temperature (c)')
    plt.xticks(rotation= 40)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    df = fetch_forecast_data(CITY)
    if not df.empty:
        plot_forecast(df, CITY)
    else:
        print("No forecast data available.")
