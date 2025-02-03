import csv
import requests
from datetime import datetime
import os
import sys

def fetch_data(url):
    """
    Fetches JSON data from a given URL.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def filter_books(books):
    """
    Filters books to include only those that have "Nonfiction" or "Hobbies" 
    in their categories.
    """
    filtered = []
    for book in books:
        categories = book.get("categories", [])
        if "Nonfiction" in categories or "Hobbies" in categories:
            filtered.append(book)
    return filtered

def update_prices(books):
    """
    For books published after 2020, add 20% to the price.
    """
    for book in books:
        pub_date = datetime.strptime(book['publication_date'], '%Y-%m-%d')
        if pub_date.year > 2020:
            original_price = book['price']
            book['price'] = round(original_price * 1.2, 2)
    return books

def write_csv(books, filename):
    """
    Writes the list of books to a CSV file.
    """
    if not books:
        return

    header = list(books[0].keys())
    
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        
        writer.writerow(header)
        
        for book in books:
            writer.writerow([book.get(key) for key in header])

def main():
    url = "https://raw.githubusercontent.com/dk-books/tech-interview/refs/heads/main/ae/books.json"
    try:
        books = fetch_data(url)
    except requests.RequestException as e:
        sys.exit(f"Error fetching data: {e}")

    filtered_books = filter_books(books)

    updated_books = update_prices(filtered_books)

    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_filename = os.path.join(script_dir, 'filtered_books.csv')
    write_csv(updated_books, output_filename)

if __name__ == '__main__':
    main()