import streamlit as st
import pickle
import numpy as np
# 1. model loading
with open('insurance_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# 2. Web App Title/Heading
st.title("🏥 Medical Insurance Cost Predictor")
st.write("Fill your details and know your annual insurance cost")

# 3. User Interface
age = st.slider("what is your age?) kya hai?", 18, 100, 30)

sex = st.selectbox("select your gender", ["Female", "Male"])
sex_encoded = 1 if sex == "Male" else 0

bmi = st.number_input("How much is your BMI? (e.g., 25.5)", min_value=10.0, max_value=50.0, value=25.0)

children = st.selectbox("How many children do you have?", [0, 1, 2, 3, 4, 5])

smoker = st.selectbox("Do you smoke?", ["No", "Yes"])
smoker_encoded = 1 if smoker == "Yes" else 0

region = st.selectbox("What is your region?", ["Southwest", "Southeast", "Northwest", "Northeast"])
region_map = {"Southwest": 1, "Southeast": 2, "Northwest": 3, "Northeast": 4}
region_encoded = region_map[region]

# 4. predict button
if st.button("Predict Cost"):
    # Putting all the features into an array
    features = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])
    
    # Prediction
    prediction = loaded_model.predict(features)
    
    # Result
    st.success(f"💰 Your estimated insurance cost will be: ${prediction[0]:.2f}")