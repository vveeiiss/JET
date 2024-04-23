import csv
import tkinter as tk

def read_csv(file_path):
    data = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data

def more_info(item_data):
    more_info_win = tk.Toplevel()
    more_info_win.title(item_data['Name'])

    name_lab = tk.Label(more_info_win, text=item_data['Name'], font=('Helvetica', 13, 'bold'))
    name_lab.grid(row=0, column=0, columnspan=2, pady=(10, 5), sticky="ew")

    rating_lab = tk.Label(more_info_win, text=f"Rating: {item_data['Rating']}", font=('Helvetica', 11))
    rating_lab.grid(row=1, column=0, sticky="w", padx=10)

    cuisines_lab = tk.Label(more_info_win, text=f"Cuisines: {item_data['Cuisines']}", font=('Helvetica', 11))
    cuisines_lab.grid(row=2, column=0, columnspan=2, padx=10, sticky="w")

    address_lab = tk.Label(more_info_win, text=f"Address: {item_data['Address']}", font=('Helvetica', 11))
    address_lab.grid(row=3, column=0, columnspan=2, padx=10, sticky="w")

    back_button = tk.Button(more_info_win, text="Back", command=more_info_win.destroy)
    back_button.grid(row=4, column=0, columnspan=2, pady=(10, 0), sticky="ew")

def main():
    file_path = 'restaurants.csv'
    data = read_csv(file_path)
    data.sort(key=lambda x: float(x['Rating']), reverse=True)

    root = tk.Tk()
    root.title("Top Restaurants in the Area")

    heading_lab = tk.Label(root, text="Starting with best!", font=('Helvetica', 14, 'bold'))
    heading_lab.pack(pady=10)

    item_frame = tk.Frame(root)
    item_frame.pack(padx=10, pady=10)

    for idx, row in enumerate(data, 1):
        frame_in = tk.Frame(item_frame, relief=tk.RAISED, borderwidth=1)
        frame_in.grid(row=idx, column=0, sticky="nsew", padx=5, pady=5)

        name_lab = tk.Label(frame_in, text=row['Name'], font=('Helvetica', 12, 'bold'))
        name_lab.grid(row=0, column=0, sticky="w", padx=5)

        rating_lab = tk.Label(frame_in, text=f"Rating: {row['Rating']}", font=('Helvetica', 11))
        rating_lab.grid(row=0, column=1, sticky="e", padx=10)

        more_info_button = tk.Button(frame_in, text="More Info", command=lambda item=row: more_info(item), width=10)
        more_info_button.grid(row=0, column=2, pady=(5, 10), padx=10, sticky="e")

    root.mainloop()

if __name__ == "__main__":
    main()
