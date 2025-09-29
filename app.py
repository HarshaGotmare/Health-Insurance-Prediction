import streamlit as st
import pickle

# ✅ Custom Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #011425, #1F4959, #5C7C89);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    label, .stNumberInput label, .stRadio > label {
        color: #C1E8FF !important;
        font-weight: 600;
        font-size: 16px;
    }
    .stRadio div[role="radiogroup"] label p {
        color: #FFFFFF !important;
        font-weight: bold !important;
        font-size: 15px;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #5C7C89, #1F4959);
        color: white;
        border-radius: 12px;
        padding: 0.6em 1.2em;
        font-size: 16px;
        font-weight: 600;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #242424, #011425);
        color: #DEAACC;
    }
    .premium-box {
        background: linear-gradient(135deg, #4A148C, #6A1B9A, #8E24AA);
        border-radius: 18px;
        padding: 30px;
        margin-top: 30px;
        text-align: center;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.45);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center; color:#C1E8FF;'>💼 Health Insurance Premium Prediction</h1>", unsafe_allow_html=True)

# Inputs
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Age', step=1, format="%d")
with col2:
    bmi = st.number_input('BMI', step=1, format="%d")
with col3:
    children = st.number_input('Number of Children', step=1, format="%d")

col4, col5 = st.columns(2)
with col4:
    gender = st.radio("Select Gender", ["Male", "Female"])
with col5:
    smoker = st.radio("Do you smoke?", ["Yes", "No"])

# Load Model
model = pickle.load(open('model.pkl', 'rb'))

# Prediction
if st.button('Predict'):
    # Encode inputs according to training
    gender_val = 0 if gender.upper() == 'MALE' else 1
    smoker_val = 0 if smoker.upper() == 'NO' else 1

    # Correct feature order: [age, sex_enc, bmi, children, smoker_enc]
    X_test = [[age, gender_val, bmi, children, smoker_val]]

    # ✅ Only change: minimum premium = 500
    yp_val = max(500, model.predict(X_test)[0])
    yp = str(round(yp_val, 2))

    # Premium Output inside beautiful gradient box
    st.markdown(
        f"""
        <div class="premium-box">
            <h2 style='color:#FFD54F;'>💡 Your Premium is:</h2>
            <h1 style='color:#FFFFFF; font-size:50px; font-weight:bold;'>💰 {yp}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
