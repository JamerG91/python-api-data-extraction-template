import requests
from config import TIMEOUT


def fetch_data(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()
        return {
            "ok": True,
            "status_code": response.status_code,
            "data": response.json(),
        }
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return {
            "ok": False,
            "error": str(e),
        }
