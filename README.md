# Overview

This script fetches book metadata as JSON from an API, filters books based on specific categories (Nonfiction and Hobbies), applies a %20 price surcharge to books published after 2020 and saves processed data into a structured CSV file.

# Features
  - Fetches book data in JSON format from a given URL.
  - Filters books that belons to either the 'Nonfiction' or 'Hobbies' categories.
  - Increases the price by 20% for books published after 2020.
  - Ensures proper formatting of the price column.
  - Saves the processed data into a CSV file.

# Requirements
  - Python 3.7 or higher
  - Required libraries: pandas, json, urllib

# Installation
  - Install Python: https://www.python.org/downloads/
  - Install required libraries: ```pip install pandas``` or https://pandas.pydata.org/docs/getting_started/install.html

# Input
  - The script retrieves book data from the following API in JSON format: https://raw.githubusercontent.com/dk-books/tech-interview/refs/heads/main/ae/books.json

# Usage
  - Ensure your Python environment is set up with the necessary dependencies.
  - Run the script: ```python main.py```
  - The processed CSV file 'filtered_books.csv' will be saved in the same directory.
