import streamlit as st
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.graph_objects as go

st.title("Global Corn Supply & Demand Forecast")

# Upload Dataset
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Show raw data
    st.subheader("Raw Data")
    st.dataframe(df)

    # Ensure columns are correct
    if 'Year' not in df.columns:
        st.error("Dataset must have a 'Year' column!")
    else:
        # Forecasting supply
        for col in ['Supply', 'Demand']:  # Change these if your column names differ
            if col in df.columns:
                st.write(f"## Forecast for {col}")

                # Prepare data for Prophet
                ts = df[['Year', col]].rename(columns={'Year':'ds', col:'y'})

                # Train model
                model = Prophet(yearly_seasonality=True)
                model.fit(ts)

                # Future data (next 5 years)
                future = model.make_future_dataframe(periods=5, freq='Y')
                forecast = model.predict(future)

                # Plot forecast
                fig = plot_plotly(model, forecast)
                st.plotly_chart(fig)
            else:
                st.warning(f"Column {col} not found in dataset.")
s
