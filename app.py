import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier  # Jika model menggunakan sklearn

# Memuat model dari file pkl
try:
    with open("laptop_recommender.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.title("Laptop Recommender System")

# Input dari pengguna
st.sidebar.header("Input Preferences")
brand = st.sidebar.selectbox("Select Brand", ["Dell", "HP", "Lenovo", "Asus", "Acer"])
budget = st.sidebar.slider("Select Budget (in USD)", 300, 2000, step=100)
usage = st.sidebar.selectbox("Primary Usage", ["Gaming", "Work", "Student", "All-purpose"])

# Tombol untuk merekomendasikan
if st.sidebar.button("Recommend"):
    try:
        # Validasi apakah model memiliki metode recommend
        if hasattr(model, "recommend"):
            recommendations = model.recommend(brand=brand, budget=budget, usage=usage)
        elif hasattr(model, "predict"):
            input_data = pd.DataFrame({
                "brand": [brand],
                "budget": [budget],
                "usage": [usage]
            })
            recommendations = model.predict(input_data)
        else:
            st.error("Model does not support recommendation or prediction.")
            st.stop()

        # Menampilkan hasil rekomendasi
        st.subheader("Recommended Laptops")
        for rec in recommendations:
            st.write(f"- {rec}")
    except Exception as e:
        st.error(f"Error during recommendation: {e}")
