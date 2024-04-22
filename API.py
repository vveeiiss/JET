import requests
import json


err = "unable to fetch restaurant data"


def get_restaurant_data(postcode):
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    #check why this header works
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("API fetched")
        return response.json()
    else:
        print(err)
        return None

def save_json(data, filename):
    with open(filename, 'w') as j_file:
        json.dump(data, j_file, indent=4)

if __name__ == "__main__":
    postcode = input("Enter postcode: ")
    restaurant_data = get_restaurant_data(postcode)

    if restaurant_data:
        save_json(restaurant_data, f'restaurant_data{postcode}.json')
    else:
        print(err)
