import streamlit as st
import pandas as pd

# Load the data
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/maressabenz/ecoswaps/main/eco_impact_data.csv'
df = pd.read_csv("eco_impact_data.csv")
return df
df = load_data()
st.title("🌱 Eco Impact Calculator")
st.write("This tool estimates CO2 savings for common eco-friendly swaps. Estimates are based on reputable data sources (EPA, Our World in Data, Carbon Trust, etc.).")

# User selects swap
swap = st.selectbox("Choose an eco swap:", df["swap"].unique())

# User inputs quantity
quantity = st.number_input("How many units?", min_value=1, step=1, value=1)

# Display result
if swap:
    row = df[df["swap"] == swap].iloc[0]
    co2_saved = quantity * row["co2_saved_kg"]
    st.success(f"🌍 By making this swap {quantity} times, you save approximately **{co2_saved:.2f} kg CO₂e**.")
    st.caption(f"Source: {row['source']}")
