import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv("eco_impact_structured.csv")
    return df

df = load_data()

# App background color (Streamlit doesn't support full page color change via markdown, but you can style boxes)
st.title("🌱 Eco Impact Calculator")
st.write("Estimate your CO₂ savings from common eco-friendly swaps. Data is based on trusted sources (EPA, Carbon Trust, Our World in Data).")

swap = st.selectbox("Choose an eco swap:", df["swap"].unique())
quantity = st.number_input("How many times will you do this swap?", min_value=1, step=1, value=1)

if swap:
    row = df[df["swap"] == swap].iloc[0]

    co2_saved = quantity * row["co2_saved_kg"]
    scaled_equiv = quantity * row["base_equivalent_value"]
st.markdown(f"""
<div style="background-color:#bab691;padding:16px;border-radius:10px">
<h3 style="color:#4e5830;">🌍 Eco Impact</h3>
<p><b>By making this swap {quantity} times, you save approximately 
<span style='color:#4e5830;font-size:1.2em'>{co2_saved:.2f} kg CO₂e</span>.</b></p>
<p><i>Equivalent to {row['equivalent_desc']} for ~<span style='color:#d86123'>{scaled_equiv:.0f} {row['equivalent_unit']}</span>.</i></p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="background-color:#f3ede7;padding:14px;border-radius:10px;margin-top:12px">
⭐ <b>If you do this 3 times a week:</b> <span style='color:#485d3a'>{co2_3x_week:.2f} kg CO₂e</span> saved per week<br>
🤝 <b>If 100 people do this once:</b> <span style='color:#485d3a'>{co2_100_people:.2f} kg CO₂e</span> saved collectively
</div>
""", unsafe_allow_html=True)


    co2_3x_week = row["co2_saved_kg"] * 3
    co2_100_people = row["co2_saved_kg"] * 100

    st.markdown(f"""
    <div style="background-color:#f3ede7;padding:14px;border-radius:10px;margin-top:12px">
    ⭐ <b>If you do this 3 times a week:</b> <span style='color:#485d3a'>{co2_3x_week:.2f} kg CO₂e</span> saved per week<br>
    🤝 <b>If 100 people do this once:</b> <span style='color:#485d3a'>{co2_100_people:.2f} kg CO₂e</span> saved collectively
    </div>
    """, unsafe_allow_html=True)

    # Add a bar graph
    labels = ['Your Action', '3x a Week', '100 People Once']
    values = [co2_saved, co2_3x_week, co2_100_people]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['#4e5830', '#6d9c94', '#d86123'])
    ax.set_ylabel('kg CO₂e Saved')
    ax.set_title('Your Climate Impact', fontsize=14, color='#485d3a')
    st.pyplot(fig)

    """, unsafe_allow_html=True)
