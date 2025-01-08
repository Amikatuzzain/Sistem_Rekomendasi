import pickle
import streamlit as st

# Coba memuat file model
try:
    with open("laptop_recommender.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Judul aplikasi
st.title("Laptop Recommender System")

# Input dari pengguna
st.sidebar.header("Input Preferences")
brand = st.sidebar.selectbox("Select Brand", ["Dell", "HP", "Lenovo", "Asus", "Acer"])
budget = st.sidebar.slider("Select Budget (in USD)", 300, 2000, step=100)
usage = st.sidebar.selectbox("Primary Usage", ["Gaming", "Work", "Student", "All-purpose"])

# Tombol untuk merekomendasikan
if st.sidebar.button("Recommend"):
    try:
        # Pastikan fungsi recommend tersedia dalam model
        if hasattr(model, "recommend"):
            recommendations = model.recommend(brand=brand, budget=budget, usage=usage)
            st.subheader("Recommended Laptops")
            for rec in recommendations:
                st.write(f"- {rec}")
        else:
            st.error("The loaded model does not have a 'recommend' method.")
    except Exception as e:
        st.error(f"Error during recommendation: {e}")
