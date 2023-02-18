import boto3
import yaml
import streamlit as st
from io import BytesIO
import logging
import time

def get_url_geos(file_name):
    try:
        parts = file_name.split("_")
        name = "-".join(parts[1].split("-")[:3])
        if name[-1].isdigit():
            name = name[: len(name) - 1]
        year = parts[3][1:5]
        day_of_year = parts[3][5:8]
        hour = parts[3][8:10]
        url = f"https://noaa-goes18.s3.amazonaws.com/ABI-L1b-RadC/{year}/{day_of_year}/{hour}/{file_name}"
        return url
    except:
        return ""


def get_url_nextrad(file_name):
    try:
        parts = file_name.split("_")
        station = parts[0][0:4]
        year = parts[0][4:8]
        month = parts[0][8:10]
        day = parts[0][10:12]
        url = f"https://noaa-nexrad-level2.s3.amazonaws.com/{year}/{month}/{day}/{station}/{file_name}"
        return url
    except Exception as e:
        pass


def get_object_url(bucket_name, object_key, s3_client):
    return s3_client.generate_presigned_url(
        ClientMethod="get_object", Params={"Bucket": bucket_name, "Key": object_key}
    )


def download_and_upload_s3_file(
    src_bucket, src_object, dest_bucket, dest_folder, dest_object, s3_client, s3_client_logs
):
    # Read the S3 object as a bytes object
    write_logs(f"Downloading {src_object} from {src_bucket}", s3_client_logs)
    s3_object = s3_client.get_object(Bucket=src_bucket, Key=src_object)
    file_content = s3_object["Body"].read()
    file_obj = BytesIO(file_content)
    write_logs("Downloading completed", s3_client_logs)
    write_logs(
        f"uploading {src_object} from {src_bucket} to {dest_bucket} under {dest_folder}",
        s3_client_logs
    )
    dest_path = dest_folder + "/" + dest_object
    # Upload the bytes object to another S3 bucket
    s3_client.upload_fileobj(file_obj, dest_bucket, dest_path)
    write_logs(f"uploading completed", s3_client_logs)
    ## Execute Under Copy Files Function
    user_s3_download_link = get_object_url(dest_bucket, dest_path, s3_client).split(
        "?"
    )[0]
    st.write(f"This is the User S3 source Link \n - {user_s3_download_link}")
    logging.info("Logging ends")


def write_logs(message: str, s3_client_logs):
    s3_client_logs.put_log_events(
        logGroupName="damg7245-noaa-assignment",
        logStreamName="app-logs",
        logEvents=[
            {
                "timestamp": int(time.time() * 1e3),
                "message": message,
            }
        ],
    )


def get_link_nexrad(file_name):
    try:
        parts = file_name.split("_")
        station = parts[0][0:4]
        year = parts[0][4:8]
        month = parts[0][8:10]
        day = parts[0][10:12]
        url = f"{year}/{month}/{day}/{station}/{file_name}"
        return url
    except Exception as e:
        pass


def get_link_goes(file_name):
    try:
        parts = file_name.split("_")
        name = "-".join(parts[1].split("-")[:3])
        if name[-1].isdigit():
            name = name[: len(name) - 1]
        year = parts[3][1:5]
        day_of_year = parts[3][5:8]
        hour = parts[3][8:10]
        url = f"ABI-L1b-RadC/{year}/{day_of_year}/{hour}/{file_name}"
        return url
    except Exception as e:
        pass
