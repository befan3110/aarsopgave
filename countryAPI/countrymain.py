import requests

def get_data():
    #henter alle data fra Api
    url = "https://restcountries.com/v3.1/all?fields=name,capital,flag,lang"
    headers = {'Accept': 'application/json'}
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return [], 0
