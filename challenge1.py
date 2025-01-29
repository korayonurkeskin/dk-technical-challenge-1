import urllib.request
import pandas as pd
import json
from datetime import datetime

# URL of the API containing book data
url = "https://raw.githubusercontent.com/dk-books/tech-interview/refs/heads/main/ae/books.json"

# Initialize an empty DataFrame with the expected columns
df = pd.DataFrame(columns = [
    'title', 
    'isbn', 
    'price',
    'description',
    'author',
    'publisher',
    'publication_date',
    'pages',
    'format',
    'categories',
    'image_url'
    ]
)

# Fetch book data from the URL
try:
    with urllib.request.urlopen(url) as response:
        # Load JSON data from the response
        books_json = json.loads(response.read())
except Exception as e:
    print(f"Error fetching data: {e}")
    # If the request fails, initialize an empty list
    books_json = []

# Loop through the book data and populate the DataFrame
for i in range(len(books_json)):
    book = books_json[i]
    df.loc[i] = [
        book['title'],
        book['isbn'],
        book['price'],
        book['description'],
        book['author'],
        book['publisher'],
        book['publication_date'],
        book['pages'],
        book['format'],
        book['categories'],
        book['image_url'],
    ]


# Filter books that belong to either the "Nonfiction" or "Hobbies" categories
filtered_df = df[df["categories"].apply(lambda x: any(category in x for category in ["Nonfiction", "Hobbies"]))]

# Convert 'publication_date' to a proper datetime format for easier comparisons
filtered_df["publication_date"] = pd.to_datetime(filtered_df["publication_date"], errors="coerce")

# Increase the price by 20% for books published after 2020
filtered_df.loc[filtered_df["publication_date"].dt.year > 2020, "price"] *= 1.2

# Format the price column to always display two decimal places
filtered_df["price"] = filtered_df["price"].astype(float).round(2)

# Save the cleaned and updated book data to a CSV file
csv_filename = "filtered_books.csv"
filtered_df.to_csv(csv_filename, index=False, encoding="utf-8")

print(f"Filtered and updated data saved to {csv_filename}")