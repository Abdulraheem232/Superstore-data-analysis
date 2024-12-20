import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


st.title("Super store data analysis")
st.write("The Superstore Data Analytics Dashboard is designed to provide a comprehensive overview of the business's performance, helping users gain insights into sales, profitability, customer behavior, and operational efficiency.")

df = pd.read_excel("Sample - Superstore.xls")

    # raw data representation
st.header("Raw data presentation")
st.dataframe(df)

    # description of numerical values of sheet
st.header("Description of numerical values of excel sheet")
st.dataframe(df.describe())

    # filter data by region
st.header("Filter data by region")
region = st.selectbox("Select region : ",df["Region"].unique())
filteredregion = df[df["Region"]==region]
st.dataframe(filteredregion)

    # filter data by state
st.header("Filter data by state")
state = st.selectbox("Select state : ",df["State"].unique())
filteredstate = df[df["State"]==state]
st.dataframe(filteredstate)

    # profit and loss by each state
st.header("Total profit and loss by each state : ")
total_sales_state = df.groupby("State")["Profit"].sum()
st.bar_chart(total_sales_state)

    # most sold category
st.header("The most sold category")
sold_category = df.groupby("Category")["Quantity"].sum().reset_index()
fig = px.pie(sold_category, names='Category', values='Quantity', title="Most Sold Category")
st.plotly_chart(fig)

    # most profit at each date
st.header("Graph of Most Profit by Each Date")
profit_eachdate = df.groupby("Ship Date")["Profit"].sum()
st.line_chart(profit_eachdate, use_container_width=True)

