import streamlit as st
import joblib
import numpy as np

import streamlit as st
import base64

def set_bg(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
 

    st.markdown(page_bg, unsafe_allow_html=True)

# Call it at the top of your app
set_bg("background.jpg")

# Load the trained model and encoders
model = joblib.load("gradient1_model.joblib")
le_gender = joblib.load("le_gender.joblib")
le_state = joblib.load("le_state.joblib")
le_stay = joblib.load("le_stay.joblib")
le_age = joblib.load("le_age.joblib")
le_visitcount = joblib.load("le_visitcount.joblib")

# Event labels for decoding multi-label prediction
event_labels =['Fair/Cultural Event/Sightseeing', 'Veneration of Relics', 'Mass']

st.title("Basilica Event Guide")

# Input fields
age_group = st.selectbox("Select Age Group", le_age.classes_)
gender = st.selectbox("Select Gender", le_gender.classes_)
state = st.selectbox("Select State/Country", le_state.classes_)
visitor_type = st.selectbox("Type of Visitor", le_visitcount.classes_)
camping = st.selectbox("Are you camping at the Basilica?", le_stay.classes_)
weekend = st.selectbox("Is it a weekend?", ['Yes', 'No'])
feast_day = st.selectbox("Is it the Feast Day?", ['Yes', 'No'])

# Encode input
input_data = np.array([[
    le_age.transform([age_group])[0],
    le_gender.transform([gender])[0],
    le_state.transform([state])[0],
    le_visitcount.transform([visitor_type])[0],
    le_stay.transform([camping])[0],
    1 if weekend == 'Yes' else 0,
    1 if feast_day == 'Yes' else 0
]])

# Predict and decode
if st.button("Predict Events"):
    prediction = model.predict(input_data)
    predicted_array = prediction[0]
    decoded_events = [event_labels[i] for i, val in enumerate(predicted_array) if val == 1]

    if decoded_events:
        st.success("Predicted Event(s): " + ", ".join(decoded_events))
    else:
        st.warning("No event participation predicted based on the input.")
# myenv\Scripts\activate
#streamlit run app.py