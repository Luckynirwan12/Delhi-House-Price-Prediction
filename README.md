# 🏠 Delhi House Price Predictor
A Streamlit web application that predicts property prices in Delhi based on various user inputs such as area, number of bedrooms and bathrooms, locality, furnishing status, house type, and parking availability — powered by a trained XGBoost Regressor model.

### 🚀 Features
- 💸 Predicts estimated house price in ₹ (INR)

- 🧾 Uses real-world housing data from Delhi

- ⚡ Fast and accurate price prediction using XGBoost

- 📊 User-friendly and interactive UI built with Streamlit

- 🧠 Trained on structured tabular data with categorical encoding


### 🧠 Tech Stack
- Python

- Pandas – for data handling

- XGBoost – gradient boosting algorithm for prediction

- Scikit-learn – preprocessing and model support

- Streamlit – to build the web interface

- Pickle – for saving and loading the trained model

### 📦 Dataset Overview
The model is trained on a dataset containing real estate listings from Delhi, with the following key features:

- `Area` (in square feet)

- `BHK` (Number of bedrooms)

- `Bathroom` (Number of bathrooms)

- `Furnishing` (Furnished/Semi-Furnished/Unfurnished)

- `Locality` (Area in Delhi)

- `Type` (Apartment, Builder Floor, etc.)

- `Parking` (Number of parking slots)

### 📂 File Structure

├── app.py                        # Streamlit web app

├── xgb_house_price_model.pkl    # Trained XGBoost model

├── house_price_df.csv           # Dataset for dropdown values

├── requirements.txt             # Required Python libraries

└── README.md 

### ⚙️ How to Run Locally
1. Clone the repository:

       git clone https://github.com/your-username/Delhi-House-Price-Predictor.git
       cd Delhi-House-Price-Predictor

2. Install dependencies:

       pip install -r requirements.txt

3. Ensure the following files are present:

  - xgb_house_price_model.pkl

  - house_price_df.csv

4. Run the Streamlit app:

       streamlit run app.py

5. Use the interface to input property details and get the predicted price.

### 📌 Sample requirements.txt
 
    streamlit
    pandas
    scikit-learn
    xgboost

### 🌐 Live Demo
If you plan to deploy it (e.g., via Streamlit Cloud or Hugging Face Spaces), you can add:

🔗 Live App Demo : 
