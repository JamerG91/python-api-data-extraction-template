from client import fetch_data
from config import BASE_URL, TIMEOUT, HEADERS, PARAMS

def main():
    print("API data extraction template")
    data = fetch_data(url = BASE_URL, params=PARAMS,  headers = HEADERS)
    print(data)


if __name__ == "__main__":
    main()
