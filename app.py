######### PART 1 - Importing Libraries
import streamlit as st
from operator import index
import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import ydata_profiling as ydp

######### PART 2 - APPLICATION FRONT-END UPPER SECTION
# Title
st.title("Data Analytics Automation Software")

# Subtitle
col1, col2 = st.columns([2,1])
with col1:
    st.markdown("## Web Application for Analysts")
with col2:
    st.image('Assets/data-analysis.png', width=50)

# Description
st.markdown("This application allows you and/or your organization to automatically analyze " + 
            "your data based on numerical and categorical information. " + 
            "The output from this product allows for further data exploration, " +
            "maximize insights, extract essential variables, detect outliers and/or anomalies. " + 
            "This tool (built with Pandas-Profiling package) can find out missing values, " + 
            "duplicated rows, No. of columns , No. of rows, shape of data, size of data & statistical " +
            "information (such as correlation). Please note that your dataset must have CSV format. " + 
            "You may download your interactive report at the bottom of the page.")
st.markdown("#### Please make sure your data is as cleaned and organized as possible")

######### PART 3 - UPLOAD CSV
file = st.file_uploader("Upload Your Dataset")

######### PART 4 - REPORT GENERATOR & DOWNLOAD
if file is not None:
    df = pd.read_csv(file, index_col=None)
    st.dataframe(df)
    st.header("Pandas Profiling (EDA - Exploratory Data Analysis)")
    profile_df = df.profile_report()
    st_profile_report(profile_df)
    ######### DOWNLOAD BUTTON
    st.markdown("#### Download Full Report in HTML Format")
    export = profile_df.to_html()
    st.download_button(label="Download", data = export, file_name = 'data_analysis.html')

######### PART 5 - APPLICATION FRONT-END BOTTOM SECTION
st.markdown("")
st.caption("Data Analytics Product Made by Juan L. Moctezuma-Flores")

################################### END OF APPLICATION ###################################


