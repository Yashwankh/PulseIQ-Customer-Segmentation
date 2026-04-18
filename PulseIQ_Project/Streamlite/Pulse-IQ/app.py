import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from pulseiq.db import fetch_df
from pulseiq.queries import MONTHLY_KPIS, CHANNEL_SHARE,  CUSTOMER_GROWTH
from pulseiq.charts import kpi_cards, line_monthly, donut_share, bar_top
from pulseiq.forecast import prophet_forecast
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_dark"


load_dotenv()

st.set_page_config(page_title='PulseIQ, Real-Time Sales & Forecasting', page_icon='📈', layout='wide')
st.title('📈 PulseIQ — RealTime Business Intelligence Dashboard ')

fallback_start = '2024-01-01'
fallback_end = '2025-10-31'

st.sidebar.header('Filters')
start = st.sidebar.date_input('Start date', value=pd.to_datetime(fallback_start).date())
end = st.sidebar.date_input('End date', value=pd.to_datetime(fallback_end).date())
params = {'start': start.isoformat(), 'end': end.isoformat()}

st.subheader('Overview')
monthly = fetch_df(MONTHLY_KPIS, params)
if not monthly.empty:
    monthly['month'] = pd.to_datetime(monthly['month'])
kpi_cards(st, monthly)

c1, c2 = st.columns((3,2))
with c1:
    st.subheader('Revenue & Orders Trend')
    st.plotly_chart(line_monthly(monthly), config={'responsive': True})
with c2:
    st.subheader('Revenue by Channel')
    ch = fetch_df(CHANNEL_SHARE, params)
    st.plotly_chart(donut_share(ch), config={'responsive': True})



st.subheader('Revenue Trend')

if not monthly.empty:
    fig = px.bar(
        monthly,
        x="month",
        y="revenue",
        title="Monthly Revenue (Bar Chart)"
    )
    st.plotly_chart(fig, use_container_width=True)



st.subheader('Customer Growth')

cust = fetch_df(CUSTOMER_GROWTH, params)

if not cust.empty:
    cust['month'] = pd.to_datetime(cust['month'])

    fig2 = px.line(
        cust,
        x="month",
        y="customers",
        title="Customer Growth Over Time",
        color_discrete_sequence=["#FF4B4B"]
    )


    st.plotly_chart(fig2, use_container_width=True)


st.header('Forecasts')
if monthly.empty:
    st.info('No monthly data to forecast.')
else:
    fc, err = prophet_forecast(monthly[['month','revenue']])
    if err:
        st.warning(f'Forecast unavailable: {err}')
    else:
        st.dataframe(fc)


import streamlit as st
import requests

st.title("Customer Churn Prediction")

recency = st.number_input("Recency")
frequency = st.number_input("Frequency")
monetary = st.number_input("Monetary")
total_amount = st.number_input("Total Amount")

if st.button("Predict"):
    url = "http://127.0.0.1:8000/predict"

    data = {
        "Recency": recency,
        "Frequency": frequency,
        "Monetary": monetary,
        "Total_Amount": total_amount
    }

    response = requests.post(url, json=data)

    result = response.json()

    st.write("Prediction:", result["prediction"])
    st.write("Result:", result["result"])