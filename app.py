import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

st.set_page_config(
    page_title="Real-Time Underground Coal Dashboard",
    page_icon="✅",
    layout="wide",
)

# read csv from a github repo
dataset_url = "https://raw.githubusercontent.com/Jasley/risk_exposure/main/methane_test.csv"

# read csv from a URL
@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

# dashboard title
st.title("Real-Time / Underground Coal Dashboard")

# top-level filters
job_filter = st.selectbox("Select DAU", pd.unique(df["DAU"]))

# creating a single-element container
placeholder = st.empty()

# dataframe filter
df = df[df["DAU"] == job_filter]

# near real-time / live feed simulation
for seconds in range(200):

    temp = np.max(df["Max_Temp"])
    hum = np.max(df["Max_Hum"])

    # creating KPIs
    #avg_age = np.mean(df["age_new"])

    pres = np.max(df["Max_Pres"])
    meth = np.max(df["Max_Meth"])

    with placeholder.container():

        # create three columns
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)

        # fill in those four columns with respective metrics or KPIs
        kpi1.metric(
            label="Methane ⏳",
            value=round(meth),
            delta=round(meth) + 5,
        )
        
        kpi2.metric(
            label="Temperature 💍",
            value=round(temp),
            delta=round(temp) + 5,
        )
        
        kpi3.metric(
            label="Pressure ＄",
            value=round(pres),
            delta=round(pres) + 5,
        )

        kpi4.metric(
            label="Humidity ＄",
            value=round(hum),
            delta=round(hum) + 5,
        )

        # create two columns for charts
        fig_col1, fig_col2, fig_col3, fig_col4 = st.columns(4)
        with fig_col1:
            #st.markdown("### Methane Reading")
            fig = px.line(
                data_frame=df, y="MM261", x="date_time",title='Methane over Period'
            )
            st.write(fig)
            
        with fig_col2:
            #st.markdown("### Second Chart")
            fig2 = px.line(data_frame=df, y="TP1721", x="date_time",title='Temperature over Period')
            st.write(fig2)

        with fig_col3:
            #st.markdown("### Second Chart")
            fig3 = px.line(data_frame=df, y="BA1723", x="date_time",title='Pressure over Period')
            st.write(fig3)

        with fig_col4:
            #st.markdown("### Second Chart")
            fig4 = px.line(data_frame=df, y="RH1722", x="date_time",title='Humidity over Period')
            st.write(fig4)

        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
    #placeholder.empty()


