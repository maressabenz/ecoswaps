import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # Use local file or replace with raw GitHub URL once uploaded
    df = pd.read_csv("eco_impact_final.csv")
    return df

df = load_data()

st.title("🌱 Eco Impact Calculator")
st.write("Estimate your CO₂ savings from common eco-friendly swaps. Data is based on trusted sources (EPA, Carbon Trust, Our World in Data).")

# User selects swap
swap = st.selectbox("Choose an eco swap:", df["swap"].unique())

# User inputs quantity
quantity = st.number_input("How many times will you do this swap?", min_value=1, step=1, value=1)

if swap:
    row = df[df["swap"] == swap].iloc[0]
    
    co2_saved = quantity * row["co2_saved_kg"]
    co2_3x_week = row["impact_3x_week_kg"]
    co2_100_people = row["impact_100_people_once_kg"]
    
    st.markdown(f"""
    <div style="background-color:#e0f7fa;padding:10px;border-radius:8px">
    <b>🌍 By making this swap {quantity} times, you save approximately 
    <span style='color:#2e7d32'>{co2_saved:.2f} kg CO₂e</span>.</b><br>
    <i>Equivalent to {row['impact_equivalent']}.</i>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background-color:#f1f8e9;padding:10px;border-radius:8px;margin-top:10px">
    ⭐ <b>If you do this 3 times a week:</b> ~{co2_3x_week:.2f} kg CO₂e saved per week<br>
    🤝 <b>If 100 people do this once:</b> ~{co2_100_people:.2f} kg CO₂e saved collectively
    </div>
    """, unsafe_allow_html=True)
