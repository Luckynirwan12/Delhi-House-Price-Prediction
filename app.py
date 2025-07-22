import streamlit as st
import pandas as pd
import pickle
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder

# Load model
with open("xgb_house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load data
house_price_df = pd.read_csv("house_price_df.csv")

# Extract unique dropdown values from dataset
localities = sorted(house_price_df['Locality'].dropna().unique())
furnishing_options = sorted(house_price_df['Furnishing'].dropna().unique())
type_options = sorted(house_price_df['Type'].dropna().unique())

# App UI
st.title("🏠 Delhi House Price Predictor")

area = st.number_input("Area (sq ft)", min_value=100, max_value=3000, step= 100)
bhk = st.selectbox("BHK", sorted(house_price_df['BHK'].unique()))
bathroom = st.selectbox("Bathrooms", sorted(house_price_df['Bathroom'].unique()))
furnishing = st.selectbox("Furnishing", furnishing_options)
locality = st.selectbox("Locality", localities)
house_type = st.selectbox("Type", type_options)
parking = st.slider("Parking", 0, 5)

if st.button("Predict Price "):
    input_df = pd.DataFrame([{
        "Area": area,
        "BHK": bhk,
        "Bathroom": bathroom,
        "Furnishing": furnishing,
        "Locality": locality,
        "Parking": parking,
        "Type": house_type
    }])

    # Encode each categorical column
    label_encoders = {}
    for col in ['Furnishing', 'Locality', 'Type']:
        le = LabelEncoder()
        input_df[col] = le.fit_transform(input_df[col])
        label_encoders[col] = le

    # Predict
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Price: ₹ {prediction:,.0f}")
