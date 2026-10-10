import streamlit as st
import pandas as pd

st.set_page_config(page_title="Life-OS", layout="wide")

st.title("🧠 Life-OS Wellbeing Dashboard")

df = pd.read_csv("screentime.csv")

dates = sorted(df["Date"].unique())
selected = st.sidebar.selectbox("Select Day", dates)    
goal = st.sidebar.slider("Daily Goal (minutes)",60,600,300)

today = df[df["Date"]==selected]
total = int(today["Minutes_Used"].sum())
top = today.groupby("App_Name")["Minutes_Used"].sum().idxmax()  
 
c1,c2,c3 = st.columns(3)
c1.metric("Today's Screen Time", f"{total} min")  
c2.metric("Most Used App", top)
c3.metric("Goal Delta", total-goal, delta_color="inverse")

st.subheader("14-Day Trend") 
st.line_chart(df.groupby("Date")["Minutes_Used"].sum())

st.subheader("Category Usage")
st.bar_chart(today.groupby("Category")["Minutes_Used"].sum())

st.info("Integrate Gemini API here to generate personalized coaching.")
