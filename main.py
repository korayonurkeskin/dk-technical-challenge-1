import csv
import requests
from datetime import datetime
import sys
import os
import unittest

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
    updated_books = []
    for book in books:
        pub_date = datetime.strptime(book['publication_date'], '%Y-%m-%d')
        if pub_date.year > 2020:
            original_price = book['price']
            book['price'] = round(original_price * 1.2, 2)
        updated_books.append(book)
    return updated_books

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


# -------------------------------
# Unit Tests
# -------------------------------
import unittest

class TestBookProcessing(unittest.TestCase):
    def setUp(self):
        # Sample book data for testing
        self.sample_books = [
            {
                "title": "Book A",
                "isbn": "111",
                "price": 10.00,
                "publication_date": "2022-01-01",
                "categories": ["Nonfiction", "Science"],
                "description": "Desc A",
                "author": "Author A",
                "publisher": "Publisher A",
                "pages": 100,
                "format": "Paperback",
                "image_url": "http://example.com/a.jpg"
            },
            {
                "title": "Book B",
                "isbn": "222",
                "price": 15.00,
                "publication_date": "2020-05-05",
                "categories": ["Hobbies", "LEGO"],
                "description": "Desc B",
                "author": "Author B",
                "publisher": "Publisher B",
                "pages": 200,
                "format": "Hardcover",
                "image_url": "http://example.com/b.jpg"
            },
            {
                "title": "Book C",
                "isbn": "333",
                "price": 20.00,
                "publication_date": "2019-08-08",
                "categories": ["Cooking", "Food & Drink"],
                "description": "Desc C",
                "author": "Author C",
                "publisher": "Publisher C",
                "pages": 300,
                "format": "Paperback",
                "image_url": "http://example.com/c.jpg"
            }
        ]

    def test_filter_books(self):
        # Only Book A and Book B should be filtered in.
        filtered = filter_books(self.sample_books)
        self.assertEqual(len(filtered), 2)
        titles = [book["title"] for book in filtered]
        self.assertIn("Book A", titles)
        self.assertIn("Book B", titles)
        self.assertNotIn("Book C", titles)

    def test_update_prices(self):
        # Test that books published after 2020 get a 20% price increase.
        filtered = filter_books(self.sample_books)
        updated = update_prices(filtered)
        for book in updated:
            if book["title"] == "Book A":
                self.assertEqual(book["price"], round(10.00 * 1.2, 2))
            elif book["title"] == "Book B":
                self.assertEqual(book["price"], 15.00)

if __name__ == '__main__':
    # If the script is run with the argument 'test', run unit tests.
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        sys.argv.pop(1)
        unittest.main()
    else:
        main()