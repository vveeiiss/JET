import requests
import json
import tkinter as tk


err = "Unable to fetch restaurant data"


def get_rest_data(postcode):
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    # check why it works with this header.
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


def get_postcode():
    postcode = postcode_entry.get()
    if postcode:
        restaurant_data = get_rest_data(postcode)
        if restaurant_data:
            save_json(restaurant_data, 'restaurant_data.json')
    root.destroy()


def main():
    global root
    root = tk.Tk()
    root.title("Postcode Search")

    title_label = tk.Label(root, text="Please Enter Postcode Without White Space", font=('Helvetica', 11, 'bold'))
    title_label.pack(pady=10)

    global postcode_entry
    postcode_entry = tk.Entry(root)
    postcode_entry.pack(pady=5)

    search_button = tk.Button(root, text="Search", command=get_postcode)
    search_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
