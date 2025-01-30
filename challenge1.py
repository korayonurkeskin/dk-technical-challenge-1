import urllib.request
import pandas as pd
import json
from datetime import datetime

# URL of the API containing book data
url = "https://raw.githubusercontent.com/dk-books/tech-interview/refs/heads/main/ae/books.json"

def fetch_books(url):
    # Fetch book data from the URL --> return it as JSON
    try:
        with urllib.request.urlopen(url) as response:
            # Load JSON data from the response
            return json.loads(response.read())
    except Exception as e:
        print(f"Error fetching data: {e}")
        # If the request fails, initialize an empty list
        return []

def convert_json_to_dataframe(books_json):
    # Convert JSON book data into a Pandas DataFrame

    df = pd.DataFrame(columns = [
        'title', 'isbn', 'price', 'description',
        'author', 'publisher', 'publication_date',
        'pages', 'format', 'categories', 'image_url'
        ]
    )
    for i in range(len(books_json)):
        book = books_json[i]
        df.loc[i] = [
            book['title'], book['isbn'], book['price'], book['description'],
            book['author'], book['publisher'], book['publication_date'],
            book['pages'], book['format'], book['categories'], book['image_url'],
        ]

    return df

def filter_books_by_category(df):
    # Filter books that belong to either the "Nonfiction" or "Hobbies" categories
    
    # edge case: ensure 'categories' is a list
    df['categories'] = df['categories'].apply(lambda x: x if isinstance(x, list) else [])

    return df[df["categories"].apply(lambda x: any(category in x for category in ["Nonfiction", "Hobbies"]))]

def adjust_prices_for_recent_books(df):
    # Increase the price by 20% for books published after 2020

    # Convert to datetime
    df["publication_date"] = pd.to_datetime(df["publication_date"], errors="coerce")
    df.loc[df["publication_date"].dt.year > 2020, "price"] *= 1.2

    return df

def format_prices(df):
    # Format the price column to always display two decimal places
    df["price"] = df["price"].astype(float).round(2)

    return df

def save_to_csv(df, filename="filtered_books.csv"):
    csv_filename = "filtered_books.csv"
    df.to_csv(csv_filename, index=False, encoding="utf-8") 
    print(f"Filtered and updated data saved to {csv_filename}")

if __name__ == "__main__":
    books_json = fetch_books(url)
    if books_json:
        df = convert_json_to_dataframe(books_json) 
        df = filter_books_by_category(df) 
        df = adjust_prices_for_recent_books(df)
        df = format_prices(df) 
        save_to_csv(df)