import streamlit as st
import joblib
import numpy as np
from api import fetch_air_quality_data

co2_model=joblib.load("co2_model.pkl")
aqi_model=joblib.load("aqi_model.pkl")

st.title("Air Quality Predictor App")

lat = st.number_input("Enter Latitude", value=28.61)
lon = st.number_input("Enter Longitude", value=77.23)

if st.button("Fetch & Predict"):
    api_key = "852c5770fcdf1dd8a7effad7d260a839"
    pollutant_data = fetch_air_quality_data(lat, lon, api_key)

    if pollutant_data:
        pm25 = pollutant_data["PM2.5"]
        no2 = pollutant_data["NO2"]
        co = pollutant_data["CO"]
        so2 = pollutant_data["SO2"]
        aqi = pollutant_data["AQI"]


        features=np.array([[pm25,no2,co,so2,aqi]])
        co2_prediction=co2_model.predict(features)[0]
        aqi_status_prediction = aqi_model.predict(features)[0]

        st.subheader("🔍 Prediction Results")
        st.write(f"**Predicted CO₂ Level:** {co2_prediction:.2f} ppm")
        st.write(f"**Air Quality Status:** {aqi_status_prediction}")
    else:
        st.error("Oops!API failed....Try again later")