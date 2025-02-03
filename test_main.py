# -------------------------------
# Unit Tests
# -------------------------------
import unittest
import main
import os

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
        filtered = main.filter_books(self.sample_books)
        self.assertEqual(len(filtered), 2)
        titles = [book["title"] for book in filtered]
        self.assertIn("Book A", titles)
        self.assertIn("Book B", titles)
        self.assertNotIn("Book C", titles)

    def test_update_prices(self):
        # Test that books published after 2020 get a 20% price increase.
        filtered = main.filter_books(self.sample_books)
        updated = main.update_prices(filtered)
        for book in updated:
            if book["title"] == "Book A":
                self.assertEqual(book["price"], round(10.00 * 1.2, 2))
            elif book["title"] == "Book B":
                self.assertEqual(book["price"], 15.00)

if __name__ == '__main__':
    unittest.main()