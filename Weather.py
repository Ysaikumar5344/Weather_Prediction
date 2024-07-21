import streamlit as st
import pandas as pd
import pickle
st.image(r"C:\Users\Y SAI KUMAR\Music\innomatics-footer-logo.webp")
# Load the trained model
with open(r"C:\Users\Y SAI KUMAR\New folder\weather.pkl", 'rb') as file:
    model = pickle.load(file)
# Define the input fields
st.title('Weather Prediction')

temperature = st.number_input('Enter Temperature (°C)', min_value=-25.0, max_value=109.0,step=1.0)
humidity = st.number_input('Enter Humidity (%)', min_value=20.0, max_value=109.0,step=1.0)
wind_speed = st.number_input('Enter Wind Speed (km/h)', min_value=0.0, max_value=48.0,step=1.0)
precipitation = st.number_input('Enter Precipitation (%)', min_value=0.0, max_value=109.0,step=1.0)
cloud_cover = st.radio('Enter Cloud Cover',['partly cloudy', 'clear', 'overcast', 'cloudy'])
atmospheric_pressure= st.number_input('Enter Atmospheric Pressure (hPa)', min_value=800.0, max_value=1200.0,step=1.0)
uv_index= st.number_input('Enter UV Index', min_value=0.0, max_value=14.0,step=1.0)
season = st.radio('Enter Season', ['Winter', 'Spring', 'Summer', 'Autumn'])
visibility = st.number_input('Enter Visibility (km)', min_value=0.0, max_value=20.0,step=1.0)
location = st.radio('Location', ['inland', 'mountain', 'coastal'])

# Create a DataFrame from the input
input_data = pd.DataFrame({
    'Temperature': [temperature],
    'Humidity': [humidity],
    'Wind Speed': [wind_speed],
    'Precipitation (%)': [precipitation],
    'Cloud Cover': [cloud_cover],
    'Atmospheric Pressure': [atmospheric_pressure],
    'UV Index': [uv_index],
    'Season': [season],
    'Visibility (km)': [visibility],
    'Location': [location]
})

# Display the input data
st.write('Input Data:')
st.write(input_data)

# Make the prediction
if st.button('Predict Weather Type'):
    prediction = model.predict(input_data)
    st.write('Predicted Weather Type:', prediction[0])

    if True:

        if prediction[0]=='Rainy':
            st.image(r"C:\Users\Y SAI KUMAR\Music\Rainyweather.png")
        elif prediction[0]=='Cloudy':
            st.image(r"C:\Users\Y SAI KUMAR\Music\Cloudyweather.png")
        elif prediction[0]=='Sunny':
            st.image(r"C:\Users\Y SAI KUMAR\Music\Sunnyweather.png")
        else:
            st.image(r"C:\Users\Y SAI KUMAR\Music\Snowyimg.png")