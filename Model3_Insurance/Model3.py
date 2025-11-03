import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open("Insurance.pkl", "rb"))

def depModel():
    st.title("Health Insurance Prediction")
    area = st.number_input("Enter age:")

    if st.button("Predict if Insurance taken"):
        result = model.predict([[area]])[0]
        st.write(f"Insured status: {['YES', 'NO'][result]}")

depModel()