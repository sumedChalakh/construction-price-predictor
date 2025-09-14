import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Title
st.title(" Construction Material Price Predictor")

# Materials list
materials = ['Cement', 'Steel', 'Sand', 'Bricks', 'Wood']

# Sidebar inputs
material = st.sidebar.selectbox("Select Material", materials)
year = st.sidebar.number_input("Enter Year (e.g., 2026)", min_value=2025, max_value=2035, step=1)

# Load model
model = joblib.load(f"results/{material}_model.pkl")

# Predict price
pred_price = model.predict([[year]])[0]

st.subheader(f" Predicted Price for {material} in {year}")
st.write(f"**{pred_price:,.2f} INR per ton**")

# Show chart (historical + prediction)
df = pd.read_csv("data/material_prices.csv")
df = df[df['Material'] == material]

plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["Price (INR per ton)"], marker="o", label="Historical")
plt.scatter(year, pred_price, color="red", label="Predicted", s=100)
plt.xlabel("Year")
plt.ylabel("Price (INR per ton)")
plt.title(f"{material} Price Prediction")
plt.legend()
st.pyplot(plt)


