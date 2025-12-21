# Python API Data Extraction Template

This repository contains a **generic Python template** for API-based data extraction and ETL workflows.

It is intended as a reusable starting point for:
- collecting data from public or authorized APIs
- handling pagination and retries
- exporting structured data to CSV or Excel


## Features
- Requests-based API client
- Pagination handling
- Basic error handling
- CSV / Excel export


## Configuration
Configuration is done in the CONFIG.py
Request Configuration
### EXTRACT_DATA: boolean
If EXTRACT_DATA is True, data are extracted via urls
in json format. We setup the base url, timeouts and headers.

### I/O
If EXTRACT_DATA is set to False, an INPUT_PATH needs
to be specified. Appropriate loader is used, according
to INPUT_PATH suffix. .json, .csv, .xls and .xlsx types
are supported.

### Saving raw data
Set SKIP_PARSING to False, to save the raw data. 
You can then specify them as input files, to avoid
making repeating requests to source or to work on parsing.


## Making requests
Use the configuration file to input data to construct
multiple urls, based on the BASE_URL. Currently, only 
get requests are supported. You must manually add changes
to the urls you are requesting, e.g., changing parameters
or even parts of the base url. 

All url data saved in a dictionary, so you must specify
a key for each call you make. All data are expected to be
json and are saved in all_raw_data which is a dict of list of dicts
all_raw_data: dict[list[dict]]

## Parser will depend on the data received

## Output
exporter type is determined from the suffix of the 
output path. .cvs, .xlsx, .xls and .json types are supported.
Exporters expect a dictionary that holds a list of dictionaries.
dict[str, list[dict]]
e.g., 

parsed_data = {
    "UK": [
        {"population":X},
        {"continent":"Y"}
    ],
    "USA": [
        {"population":X},
        {"continent":"Y"}
    ]
}

An excel output will have the high level keys as sheets. 
A .csv will create a different .csv for each sheet.

## Disclaimer
This repository is for educational and demonstration purposes only.


