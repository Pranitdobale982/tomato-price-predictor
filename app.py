import streamlit as st
import pandas as pd
import numpy as np

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Tomato Price Predictor", page_icon="🍅", layout="centered")

st.title("🍅 AI Tomato Price Predictor")
st.markdown("""
Welcome to the Tomato Price Forecasting Dashboard! 
Adjust the environmental, economic, and regional factors to see the predicted price in **US Dollar ($)**.
""")

# --- 2. SIDEBAR: USER INPUTS ---
st.sidebar.header("Input Parameters")

def user_input_features():
    # --- NEW: COUNTRY SELECTION ---
    # You can add more countries to this list as needed
    country = st.sidebar.selectbox("Select Country for Context", 
                                   ["Nigeria", "United States", "United Kingdom", "Canada", "Ghana", "India", "Other"])

    # Environmental Factors
    temperature = st.sidebar.slider("Avg Temperature (°C)", min_value=10.0, max_value=45.0, value=25.0, step=0.5)
    rainfall = st.sidebar.slider("Monthly Rainfall (mm)", min_value=0.0, max_value=500.0, value=120.0, step=10.0)
    
    # Time/Seasonal Factors
    month = st.sidebar.selectbox("Month of Harvest", 
                                 ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    
    # Economic Factors - Updated to Naira (₦)
    fuel_price = st.sidebar.number_input("Local Fuel Price ($/Liter)", min_value=1.0, max_value=2.0, value=1.25, step=0.5)
    
    # Format inputs into a dataframe
    data = {
        'country': country,
        'temperature': temperature,
        'rainfall': rainfall,
        'month': month,
        'fuel_price': fuel_price
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Display the user's inputs on the main page
st.subheader("Current Market Conditions")
st.write(input_df)

# --- 3. PREDICTION LOGIC ---
st.write("---")

if st.button("🔮 Predict Tomato Price", type="primary"):
    with st.spinner("Analyzing data..."):
        
        # Mock logic updated for Dollar values
        # Base price per kg in Dollar (Adjusted for realistic scale)
        base_price_dollar = 2.5 
        
        temp_effect = (input_df['temperature'][0] - 25) * 20.0  
        rain_effect = (120 - input_df['rainfall'][0]) * 5.0   
        fuel_effect = input_df['fuel_price'][0] * 0.5
        
        predicted_price = base_price_dollar + temp_effect + rain_effect + fuel_effect

        # Display result with Dollar Symbol
        st.success(f"### Predicted Wholesale Price: **${predicted_price:,.2f} per kg**")
        
        # Chart with Dollar label
        st.subheader(f"Projected Price Trend ({input_df['country'][0]})")
        trend_data = pd.DataFrame(
            np.random.randn(20, 1) * 50 + predicted_price,
            columns=['Price ($)']
        )
        st.line_chart(trend_data)