import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Demand Forecasting App")
st.header("Enter Inputs")

# Inputs
store_id = st.number_input("Store ID", value=1)
item_id = st.number_input("Item ID", value=1)

price = st.number_input("Price", value=21.3)
promo = st.selectbox("Promo (0 = No, 1 = Yes)", [0, 1])

weekday = st.slider("Weekday (0-6)", 0, 6, 1)
month = st.slider("Month (1-12)", 1, 12, 1)

lag_1 = st.number_input("Lag 1 (Yesterday Sales)", value=45.0)
lag_7 = st.number_input("Lag 7 (Last Week Sales)", value=42.0)
lag_30 = st.number_input("Lag 30 (Last Month Sales)", value=40.0)

rolling_mean_7 = st.number_input("7-Day Rolling Mean", value=44.0)
rolling_mean_30 = st.number_input("30-Day Rolling Mean", value=43.0)

day_of_week = st.slider("Day of Week", 0, 6, 1)
day_of_month = st.slider("Day of Month", 1, 31, 15)

# Prediction
if st.button("Predict Demand"):
    
    input_data = np.array([[ 
        store_id, item_id, price, promo, weekday, month,
        lag_1, lag_7, lag_30,
        rolling_mean_7, rolling_mean_30,
        day_of_week, day_of_month
    ]])

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Demand: {round(prediction, 2)}")

    # Chart
    values = [lag_1, lag_7, rolling_mean_7, prediction]
    labels = ["Yesterday", "Last Week", "7-Day Avg", "Prediction"]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Demand Comparison")
    st.pyplot(plt)

    # Insight
    if prediction > rolling_mean_7:
        st.info("Expected demand increase compared to recent trend.")
    else:
        st.info("Demand likely stable or decreasing.")


#TEST CASES 1

#Store ID: 1
#Item ID: 1

#Price: 18.0
#Promo: 1

#Weekday: 5
#Month: 6

#Lag 1: 55
#Lag 7: 48
#Lag 30: 45

#Rolling Mean 7: 47
#Rolling Mean 30: 46

#Day of Week: 5
#Day of Month: 20



#TEST CASE 2 

#Store ID: 1
#Item ID: 1

#Price: 26.0
#Promo: 0

#Weekday: 2
#Month: 2

#Lag 1: 30
#Lag 7: 35
#Lag 30: 40

#Rolling Mean 7: 38
#Rolling Mean 30: 39

#Day of Week: 2
#Day of Month: 10
