import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open("Iris.pkl", "rb"))

def depModel():
    st.title("Iris Flower Species Prediction")
    sepal_length = st.number_input("Enter sepal length:")
    sepal_width = st.number_input("Enter sepal width:")
    petal_length = st.number_input("Enter petal length:")
    petal_width = st.number_input("Enter petal width:")
    
    species = ["setosa", "versicolor", "virginica"]

    if st.button("Predict Species"):
        species_idx = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]

        st.write(f"The predicted Iris flower is: Iris {species[species_idx]}")

depModel()