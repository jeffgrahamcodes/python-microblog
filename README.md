# Microblog App

A minimalist blogging platform built with Python and Flask that lets users write and share short posts.

---

## Features

- Add and display blog entries
- Recent entries appear in reverse chronological order
- Lightweight, responsive front-end design using HTML and CSS
- Posts stored in a database (MongoDB integration inferred)

---

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (custom styles)
- **Database:** MongoDB (via `pymongo`)

---

## File Structure

```
├── app.py                # Flask application logic
├── home.html             # HTML template for homepage
├── styles.css            # Main CSS styles
├── requirements.txt      # Project dependencies
└── static/
    └── logo.svg          # Site logo
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jeffgrahamcodes/python-microblog.git
cd python-microblog
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file in the root directory with:

```bash
FLASK_APP=app.py
FLASK_ENV=development
MONGO_URI=your_mongodb_connection_string
```

### 5. Run the app

```bash
flask run
```

---

## Usage

1. Navigate to `http://localhost:5000` in your browser.
2. Add a new entry using the form.
3. Scroll down to view recent posts.

---

## Styling

Custom CSS is located in `static/css/styles.css`, with responsive layout and simple UI components.

---

## License

This project is open source under the [MIT License](LICENSE).

---

## Created By

**Jeff Graham**
Full-Stack Cloud Developer & Educator
[LinkedIn](https://linkedin.com/in/jeffgrahamcodes)
[GitHub](https://github.com/jeffgrahamcodes)
[jeffgraham.codes](https://jeffgraham.codes)
