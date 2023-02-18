# Big Data Systems and Int Analytics - Assignment 1
## Team Information and Contribution 

Name | NUID | Contribution 
--- | --- | --- |
Karan Agrawal | 001090008 | 25% 
Rishabh Singh | 002743830 | 25% 
Lokeshwaran Venugopal Balamurugan | 002990533 | 25% 
Sivaranjani S | 002742197 | 25% 

## Project Flow 
![image](https://user-images.githubusercontent.com/90572559/218140875-d2c0c6de-a82b-4bf0-a8d2-3af77871ddaa.png)
- This project involved building a prototype application using Streamlit to explore datasets sourced from the NOAA's GEOS & NEXTRAD dataset. The application allows an analyst to choose a station, year, day, and hour through the Streamlit interface. The metadata(Folder Structure) is scraped from the GOES and NEXTRAD S3 bucket and stored in a SQLite database. The app lists all available files in real-time and upon selection, the chosen file is transferred from the GOES location to an AWS S3 bucket and a link to the S3 bucket is made available to the user along with a link to the original GOES site for comparison. The application also tracks the dataset downloads to prevent direct downloads from the GOES website.

## Project Tree 
```
📦 
├─ .DS_Store
├─ .github
│  └─ workflows
│     ├─ pytest.yml <- Github Workflow for PyTest
│     └─ static.yml <- Github Workflow for Great Expectations
├─ .gitignore
├─ GEOS-18.py <- Streamlit Main Page
├─ GOES-MetaData-ETL.ipynb <- ETL to extract MetaData from GEOS S3 Bucket
├─ GreatExpectations_GEOS.ipynb <- Great Expectations Test on GEOS Metadata
├─ GreatExpectations_NEXTRAD.ipynb <- Great Expectations Test on NEXTRAD Metadata
├─ NEXRAD-MetaData-ETL.ipynb <- ETL to extract MetaData from NEXTRAD S3 Bucket
├─ README.md
├─ functions.py <- Helper Functions for Streamlit Data Crunching
├─ great_expectations
│  ├─ expectations
│  │  ├─ .ge_store_backend_id
│  │  ├─ geos_suite.json
│  │  └─ nextrad_suite.json
│  ├─ great_expectations.yml
│  ├─ plugins
│  │  └─ custom_data_docs
│  │     └─ styles
│  │        └─ data_docs_custom_styles.css
│  └─ uncommitted
│     ├─ config_variables.yml
│     ├─ data_docs
│     │  └─ local_site
│     │     ├─ expectations
│     │     │  ├─ geos_suite.html
│     │     │  └─ nextrad_suite.html
│     │     ├─ index.html
│     │     ├─ static
│     │     │  ├─ fonts
│     │     │  │  └─ HKGrotesk
│     │     │  │     ├─ HKGrotesk-Bold.otf
│     │     │  │     ├─ HKGrotesk-BoldItalic.otf
│     │     │  │     ├─ HKGrotesk-Italic.otf
│     │     │  │     ├─ HKGrotesk-Light.otf
│     │     │  │     ├─ HKGrotesk-LightItalic.otf
│     │     │  │     ├─ HKGrotesk-Medium.otf
│     │     │  │     ├─ HKGrotesk-MediumItalic.otf
│     │     │  │     ├─ HKGrotesk-Regular.otf
│     │     │  │     ├─ HKGrotesk-SemiBold.otf
│     │     │  │     └─ HKGrotesk-SemiBoldItalic.otf
│     │     │  ├─ images
│     │     │  │  ├─ favicon.ico
│     │     │  │  ├─ glossary_scroller.gif
│     │     │  │  ├─ iterative-dev-loop.png
│     │     │  │  ├─ logo-long-vector.svg
│     │     │  │  ├─ logo-long.png
│     │     │  │  ├─ short-logo-vector.svg
│     │     │  │  ├─ short-logo.png
│     │     │  │  └─ validation_failed_unexpected_values.gif
│     │     │  └─ styles
│     │     │     ├─ data_docs_custom_styles_template.css
│     │     │     └─ data_docs_default_styles.css
│     │     └─ validations
│     │        ├─ geos_suite
│     │        │  └─ __none__
│     │        │     └─ 20230208T123514.819212Z
│     │        │        └─ c59c2bdb213b5f9e335d32dae79e3ecb.html
│     │        └─ nextrad_suite
│     │           └─ __none__
│     │              ├─ 20230208T124414.909973Z
│     │              │  └─ 3569fdb9ee9f77966268f4060430f226.html
│     │              └─ 20230208T124447.357538Z
│     │                 └─ 3569fdb9ee9f77966268f4060430f226.html
│     ├─ datasource_new.ipynb
│     ├─ edit_geos_suite.ipynb
│     ├─ edit_nextrad_suite.ipynb
│     └─ validations
│        ├─ .ge_store_backend_id
│        ├─ geos_suite
│        │  └─ __none__
│        │     └─ 20230208T123514.819212Z
│        │        └─ c59c2bdb213b5f9e335d32dae79e3ecb.json
│        └─ nextrad_suite
│           └─ __none__
│              ├─ 20230208T124414.909973Z
│              │  └─ 3569fdb9ee9f77966268f4060430f226.json
│              └─ 20230208T124447.357538Z
│                 └─ 3569fdb9ee9f77966268f4060430f226.json
├─ main.py <- HyperLink Creation Functions for Pytest
├─ nexrad-stations.csv
├─ noaa_goes_date.db <- SQLite DB hosting Metadata for both GEOS and NEXTRAD
├─ pages
│  ├─ .DS_Store
│  ├─ NEXRAD.py <- Streamlit Page for NEXTRAD
│  └─ NEXRAD_Stations.py <- Streamlit Page for NEXTRAD stations
├─ requirements.txt <- Requirenments File
├─ setup.sh
└─ test.py
```
## Link to the Live Applications
- Streamlit Application : https://bigdataia-spring2023-team-04-bigdataia-assignme-geos-18-tz9ba6.streamlit.app/
- Great Expectations : https://bigdataia-spring2023-team-04.github.io/BigDataIA-Assignment-01/

## Link to S3 Buckets
- GEOS S3 : https://noaa-goes18.s3.amazonaws.com/index.html#ABI-L1b-RadC/
- NEXTRAD S3 : https://noaa-nexrad-level2.s3.amazonaws.com/index.html

## Logs Example
![image](https://user-images.githubusercontent.com/90572559/218146471-7490aece-3b8a-411f-8bfb-c6df680967a2.png)
