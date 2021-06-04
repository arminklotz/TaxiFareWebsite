import streamlit as st
import pandas as pd
import datetime
import requests

'''
# NY TaxiFare estimator
'''


pickup_date = st.date_input('Date', datetime.date.today())
pickup_time = st.time_input('Time', datetime.datetime.now())
pickup_longitude = st.number_input('Pickup Longitude')
pickup_latitude = st.number_input('Pickup Latitude')
dropoff_longitude = st.number_input('Dropoff Longitude')
dropoff_latitude = st.number_input('Dropoff Latitude')
passenger_count = st.slider('How many passengers?', 1, 7, 2)

url = 'https://taxifare.lewagon.ai/predict'

# 2. Let's build a dictionary containing the parameters for our API...
pickup_datetime = datetime.datetime.combine(pickup_date, pickup_time)

params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

coords = pd.DataFrame({
    'lat': [pickup_latitude, dropoff_latitude],
    'lon': [pickup_longitude, dropoff_longitude]
})

#coords

st.map(coords)

# 3. Let's call our API using the `requests` package...
response = requests.get(url=url, params=params)

# 4. Let's retrieve the prediction from the **JSON** returned by the API...
if response.status_code == 200:
    prediction = response.json()
else:
    st.text('There seems to be an error...')

## Finally, we can display the prediction to the user
st.info(f"Predicted fare price: {round(prediction['prediction'], 2)}$")
