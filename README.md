# ⛪ Basilica Event Prediction System

This project is an interactive Streamlit web application that predicts the type of event a visitor is likely to attend at the Basilica of Bom Jesus, based on user characteristics and visit details. It leverages machine learning and label encoding techniques to offer personalized event suggestions.

## 📌 Project Overview

During large-scale religious events like the Exposition of St. Francis Xavier, managing crowds and guiding visitors efficiently is essential. This application uses user inputs (age, gender, location, etc.) and predicts the most likely event(s) the visitor would attend:

- 🎭 Fair/Cultural Event/Sightseeing
- 🙏 Veneration of Relics
- 🕊️ Mass
</br>
  ![Streamlit app Preview](Streamlit app recording.gif)  
</br>
## 🧠 Machine Learning Model

- **Model**: Gradient Boosting Classifier (multi-label classification)
- **Preprocessing**: Label Encoding for categorical variables
- **Tools Used**:
  - `scikit-learn`
  - `joblib` for saving models
  - `Streamlit` for building the web interface

## 📁 Project Structure

📂 BasilicaEventPrediction
│
├── app.py # Streamlit app for event prediction
├── model_selctn.ipynb #Notebook for data preprocessing, label binarization, EDA, and model selection
├── GBM_model.ipynb #  Notebook for training and saving the ML model with encoders
├── gradient1_model.joblib # Trained ML model file
├── le_gender.joblib # Label encoder for Gender
├── le_state.joblib # Label encoder for State/Country
├── le_stay.joblib # Label encoder for Stay status
├── le_age.joblib # Label encoder for Age group
├── le_visitcount.joblib # Label encoder for Visit frequency
├── background.jpg # Background image for the Streamlit UI
└── README.md # This documentation file


## 🖥️ How to Run

1. **Install dependencies**

bash
- pip install streamlit scikit-learn joblib numpy

2. **Run the app**
- bash
- streamlit run app.py

3. **Interact via browser**
Select age, gender, state, visitor type, stay details, and date context
Get predicted event recommendations

## 🖼️ App Interface
The app uses multiple dropdowns for user inputs. The result is shown after clicking "Predict Events".

## 📊 Model Training
Dataset includes:
- Age group
- Gender
- Country/State
- Visitor frequency
- Stay (camping or not)
- Event attending
- Weekend/Feast day indicators

## Target:
Multi-label output for events predicted


## 🚀 Features
Multi-label event prediction
Label encoding with pre-trained encoders
Clean UI with visual theming
Real-time prediction with Streamlit


