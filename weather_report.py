# !pip install plotly
# !pip install requests

import plotly.graph_objects as go
import requests
import pandas as pd
import datetime

API_KEY = "97d69fe6c895f05ffe2e68996c7ecdfb" 
CITY = "Vijayawada" 

def get_weather_data(city, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
        
weather_data = get_weather_data(CITY, API_KEY)


if weather_data:
    data = weather_data['list']

    temperatures = [item['main']['temp'] for item in data]
    humidity = [item['main']['humidity'] for item in data]
    wind_speed = [item['wind']['speed'] for item in data]
    timestamps = [datetime.datetime.fromtimestamp(item['dt']) for item in data]
    weather_descriptions = [item['weather'][0]['description'] for item in data]
    
    df = pd.DataFrame({'Timestamp': timestamps, 'Temperature': temperatures, 'Humidity': humidity, 'Wind Speed': wind_speed, 'Description': weather_descriptions})

    df = df.head(8)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Timestamp'], y=df['Temperature'], mode='lines+markers', name='Temperature (°C)'))
    fig.add_trace(go.Scatter(x=df['Timestamp'], y=df['Humidity'], mode='lines+markers', name='Humidity (%)', yaxis="y2"))
    fig.add_trace(go.Scatter(x=df['Timestamp'], y=df['Wind Speed'], mode='lines+markers', name='Wind Speed (m/s)', yaxis="y3"))
    fig.update_layout(
        width=1500,
        height=600,
        title=f'Weather Forecast for {CITY}',
        xaxis_title='Time',
        xaxis=dict(side='bottom', domain=[0.0, 1.0]),
        yaxis=dict(title='Temperature (°C)', side='left', domain=[0.6, 1.0]),
        yaxis2=dict(title='Humidity (%)', side='left', domain=[0.33,0.6]),
        yaxis3=dict(title='Wind Speed (m/s)',side='left', domain=[0.0, 0.32]),
        hovermode="x"
    )
    fig.show()
else:
    print('Could not retrieve weather data. Check the city name and API key')

