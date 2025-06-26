import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
data= pd.read_csv("simulated_air_quality.csv")
x1=data[['PM2.5','NO2','CO','SO2','AQI']]
y1=data['CO2']
x1_train,x1_test,y1_train,y1_test=train_test_split(x1,y1,test_size=0.2,random_state=42)
co2_model=LinearRegression()
co2_model.fit(x1_train,y1_train)

joblib.dump(co2_model,"co2_model.pkl")


y2=data['AQI_Status']
x2_train,x2_test,y2_train,y2_test=train_test_split(x1,y2,test_size=0.2,random_state=42)
aqi_model=LogisticRegression()
aqi_model.fit(x2_train,y2_train)

joblib.dump(aqi_model,"aqi_model.pkl")

