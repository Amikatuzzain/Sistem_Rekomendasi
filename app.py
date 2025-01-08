import pickle
import streamlit as st

# Memuat model dari file pkl
with open("laptop_recommender.pkl", "rb") as file:
    model = pickle.load(file)

# Judul aplikasi
st.title("Laptop Recommender System")

# Input dari pengguna
st.sidebar.header("Input Preferences")
brand = st.sidebar.selectbox("Select Brand", ["Dell", "HP", "Lenovo", "Asus", "Acer"])
budget = st.sidebar.slider("Select Budget (in USD)", 300, 2000, step=100)
usage = st.sidebar.selectbox("Primary Usage", ["Gaming", "Work", "Student", "All-purpose"])

# Tombol untuk merekomendasikan
if st.sidebar.button("Recommend"):
    # Blok kode harus terindeks di sini
    try:
        # Ganti fungsi ini dengan metode prediksi/model Anda
        recommendations = model.recommend(brand=brand, budget=budget, usage=usage)
        st.subheader("Recommended Laptops")
        for rec in recommendations:
            st.write(f"- {rec}")
    except AttributeError:
        st.error("Model doesn't support the required method.")
