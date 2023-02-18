#######################################################################################################################
### IMPORTS
#######################################################################################################################
import sqlite3
import boto3
import yaml
import streamlit as st
import pandas as pd
from functions import get_url_geos, download_and_upload_s3_file, get_link_goes
import logging

#######################################################################################################################
### AWS Variables
#######################################################################################################################

src_bucket_name = "noaa-goes18"
dest_bucket_name = "damg7245-noaa-assignment"

AWS_ACCESS_KEY = st.secrets["AWS_ACCESS_KEY"]
AWS_SECRET_KEY = st.secrets["AWS_SECRET_KEY"]
AWS_LOG_ACCESS_KEY = st.secrets["AWS_LOG_ACCESS_KEY"]
AWS_LOG_SECRET_KEY = st.secrets["AWS_LOG_SECRET_KEY"]


#######################################################################################################################
### AWS Client
#######################################################################################################################

s3_client = boto3.client(
    "s3",
    region_name="us-east-1",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
)


s3_session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY
)

s3_client_logs = boto3.client(
    "logs",
    region_name="us-east-1",
    aws_access_key_id=AWS_LOG_ACCESS_KEY,
    aws_secret_access_key=AWS_LOG_SECRET_KEY,
)

#######################################################################################################################
### Helper Functions
#######################################################################################################################


def search_file(file_name, s3):
    file_name = get_link_goes(file_name)
    try:
        s3.head_object(Bucket="noaa-goes18", Key=file_name)
        return True
    except:
        return False


options = ["Search by Parameters", "Search by File Name"]
selected_option = st.sidebar.selectbox("Select an option", options)

if selected_option == "Search by Parameters":
    st.header("Get Hyperlinks by Parameters")
    col1, col2, col3 = st.columns(3)
    # Connect to the database
    conn = sqlite3.connect("noaa_goes_date.db")
    cursor = conn.cursor()
    ####################################################################
    #### Selecting Year
    ####################################################################
    # Execute a SELECT query to fetch the data
    cursor.execute("SELECT distinct year FROM noaa_goes_date order by year")
    # Fetch all the rows
    years = cursor.fetchall()
    # Extract the unique years
    unique_years = [year[0] for year in years]
    # Use Streamlit to display the dropdown
    selected_year = col1.selectbox("Select a year:", unique_years)
    # Use Streamlit to display the selected year
    ####################################################################
    #### Selecting Day in Year
    ####################################################################
    cursor.execute(
        f"""SELECT distinct day FROM noaa_goes_date
                        where year = {selected_year} order by day"""
    )
    # Fetch all the rows
    days = cursor.fetchall()
    # Extract the unique years
    unique_days = [day[0] for day in days]
    # Use Streamlit to display the dropdown
    selected_day = col2.selectbox("Select a day:", unique_days)
    # Use Streamlit to display the selected year
    ####################################################################
    #### Selecting Hour in Day
    ####################################################################
    cursor.execute(
        f"""SELECT distinct hour FROM noaa_goes_date
                        where year = {selected_year}
                        and day = '{str(selected_day).zfill(3)}' order by hour"""
    )
    # Fetch all the rows
    hours = cursor.fetchall()
    # Extract the unique years
    unique_hours = [hour[0] for hour in hours]
    # Use Streamlit to display the dropdown
    selected_hour = col3.selectbox("Select a hour:", unique_hours)
    # Use Streamlit to display the selected year
    ####################################################################
    #### Prefix Generation
    ####################################################################

    prefix = f"ABI-L1b-RadC/{selected_year}/{selected_day}/{selected_hour}/"
    bucket = "noaa-goes18"
    result = s3_client.list_objects(Bucket=bucket, Prefix=prefix)
    files = [content["Key"].split("/")[-1] for content in result.get("Contents", [])]

    selected_file = st.selectbox("Please select a file to Download:", files)
    hyperlink = get_url_geos(selected_file)
    st.write(f"Link to the GEOS S3 Bucket is \n - {hyperlink}")
    parts = hyperlink.split("/")
    src_file_name = "/".join(map(str, parts[3:]))

if selected_option == "Search by File Name":
    st.header("Get Hyperlinks by Name")
    selected_file = st.text_input("Name of File")
    if selected_file != "":
        hyperlink = get_url_geos(selected_file)
        if search_file(selected_file, s3_client):
            st.write("File found in GEOS S3 bucket!")
            st.write(f"Link to the GEOS S3 Bucket is \n - {hyperlink}")
            parts = hyperlink.split("/")
            src_file_name = "/".join(map(str, parts[3:]))
        else:
            st.warning("File not found in the goes18 S3 bucket.")

copy_files = st.button("Copy Files !")
if copy_files:
    logging.info("Started Logging")
    download_and_upload_s3_file(
        src_bucket_name,
        src_file_name,
        dest_bucket_name,
        "goes",
        selected_file,
        s3_client,
        s3_client_logs,
    )
