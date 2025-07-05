
# 🌱 Eco Impact Calculator

This is an interactive tool that lets users estimate their CO2 savings from everyday eco-friendly swaps.

## 🚀 How it works
- The app loads data from `eco_impact_data.csv`, which contains 50 common eco swaps, CO2 savings estimates (kg CO2e per unit), and source references.
- Users select a swap and input how many times they do it.
- The tool calculates total CO2 savings and displays the source.

## 📊 Data sources
Data is aggregated from:
- [EPA Household Carbon Calculator](https://www.epa.gov/ghgemissions/household-carbon-footprint-calculator)
- [Our World in Data](https://ourworldindata.org/environmental-impacts-of-food)
- [Carbon Trust](https://www.carbontrust.com/)
- [Project Drawdown](https://drawdown.org/solutions/table-of-solutions)

## ⚙️ Run locally
```bash
pip install streamlit pandas
streamlit run streamlit_eco_calculator_app.py
```

## 🌐 Deploy
You can deploy this app using:
- [Streamlit Cloud](https://streamlit.io/cloud)
- Vercel / Netlify (if wrapped in a web app)

This tool is for educational purposes. CO2 savings are estimates; actual impact varies by region and context.
