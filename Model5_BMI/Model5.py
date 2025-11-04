import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open("bmi_model.pkl", "rb"))

def depModel():
    st.title("Male-Female Prediction")
    height = st.number_input("Enter the height:")
    weight = st.number_input("Enter the weight:")
    gender = ['Female', 'Male']
    if st.button("Predict Gender"):
        G = model.predict([[height, weight]])[0]
        st.write(f"The predicted gender is: {gender[G]}")

depModel()