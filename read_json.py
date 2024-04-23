import json
import csv

def write_to_csv(file_path, rest_list):
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
        headers = ['Name', 'Cuisines', 'Rating', 'Address']
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for rest in rest_list:
            cuisines = ", ".join([cuisine.get('name', '') for cuisine in rest.get('cuisines', [])])
            writer.writerow({
                'Name': rest.get('name', ''),
                'Cuisines': cuisines,
                'Rating': rest.get('rating', {}).get('starRating', ''),
                'Address': f"{rest.get('address', {}).get('firstLine', '')}, {rest.get('address', {}).get('city', '')}, {rest.get('address', {}).get('postalCode', '')}"
            })

def get_data(file_path):
    with open(file_path, 'r') as j_file:
        data = json.load(j_file)
        if 'restaurants' in data:
            rest = data['restaurants'][:10]
            return rest
        else:
            return None


if __name__ == "__main__":
    file_path = 'FILE_PATH' #replace with file path
    restaurants = get_data(file_path)
    if restaurants:
        print("data retrieved successfully")

        csv_file_path = f'restaurants.csv'
        write_to_csv(csv_file_path, restaurants)

    else:
        print("no data found")

