# Dictionary API

A small Flask application that serves word definitions from a CSV dataset and exposes them through a simple REST API.

## Features

- Simple web page at the home route
- JSON API endpoint for word lookup
- Definitions loaded from a CSV file in the dataset folder
- Easy to run locally with Flask and pandas

## Project Structure

```text
dictionary_api/
├── dataset/
│   └── dictionary.csv
├── templates/
│   └── home.html
├── main.py
├── README.md
└── .git/
```

## Prerequisites

- Python 3.8+
- Flask
- pandas

## Installation

1. Open a terminal in the project folder.
2. Install the required packages:

```bash
pip install flask pandas
```

## Run the app

```bash
python main.py
```

The app will run in debug mode at:

```text
http://127.0.0.1:5000/
```

## API Usage

### Home page

```text
GET /
```

Returns the HTML landing page.

### Word lookup

```text
GET /api/v1/<word>
```

Example:

```text
http://127.0.0.1:5000/api/v1/abiotic%20factor
```

Example response:

```json
{
  "word": "abiotic factor",
  "definition": "Physical, chemical and other non-living environmental factor."
}
```

If a word is not found, the API returns:

```json
{
  "status": "error",
  "message": "word <word> not found"
}
```

## Notes

- The dataset is stored in `dataset/dictionary.csv`.
- The word matching is done against the `word` column in the CSV.
- The app uses Flask's built-in development server, which is intended for local development.
