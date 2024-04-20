import requests

def get_restaurants_data(postcode):
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"

    response = requests.get(url)
    response_type = response.headers.get('content_type', 'unknown')
    print(f"response type: {response_type}")

    print(response.content.decode('utf-8'))
    return None


#test
postcode = "EC4M7RF"
restaurants_data = get_restaurants_data(postcode)

