# DK Book Processing Script

## Overview

This Python script processes book metadata from an API. It performs the following tasks:

- **Fetches** book data in JSON format from a provided URL.
- **Filters** the books to include only those that belong to the "Nonfiction" or "Hobbies" categories.
- **Updates Prices:** Applies a 20% surcharge to books published after 2020.
- **Exports** the processed data into a CSV file, saved in the same directory as the script.

## Features

- **Data Fetching:** Retrieves book data from the DK API in JSON format.
- **Category Filtering:** Selects only books categorized as "Nonfiction" or "Hobbies".
- **Price Adjustment:** Increases the price by 20% for books with a publication date after 2020.
- **CSV Export:** Writes the filtered and updated data to a CSV file, maintaining the original JSON key order.

## Requirements

- **Python:** Version 3.7 or higher
- **Dependencies:** See [Installation](#installation)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/korayonurkeskin/dk-technical-challenge-1.git
   cd dk-technical-challenge-1
   ```

## Step-by-Step Instructions to Run the Script

1. **Activate Your Virtual Environment:**

   - If the virtual environment is not already active, run the following command based on your operating system:
     - **On macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```
     - **On Windows:**
       ```bash
       venv\Scripts\activate
       ```
   - Your terminal prompt should then display `(venv)`, indicating that the virtual environment is active.

2. **Install Dependencies (if not already installed):**

   - Run:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Script:**

   - Execute:
     ```bash
     python main.py
     ```

4. **Verify the Output:**
   - A file named `filtered_books.csv` will be generated in the project directory containing the processed book data.
