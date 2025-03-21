# Ebb and Flow

## Overview
**ebb-and-flow** is a backend server that provides book-related functionalities, including retrieving book content, generating AI-powered plot summaries, and managing a local book database.

## Features
- Retrieve book data from a local JSON-based database
- Generate AI-powered plot summaries using Groq API
- Provide book metadata and content via API endpoints

## Installation
### Prerequisites
- Python 3.11+
- `pip` (Python package manager)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/ebb-and-flow.git
   cd ebb-and-flow
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the root directory and add:
     ```sh
     API_KEY=your_groq_api_key
     ```

## Usage
### Running the Server
Start the backend server with:
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### API Endpoints
#### Get Book List
- **Endpoint:** `GET /api/get_book_list`
- **Response:**
  ```json
  [
    { "book_id": "1", "book_title": "Frankenstein" },
    { "book_id": "2", "book_title": "Dracula" }
  ]
  ```

#### Get Book Data
- **Endpoint:** `GET /api/read/{book_id}`
- **Response:**
  ```json
  {
    "book_id": "1",
    "book_title": "Frankenstein",
    "content": "Once upon a time...",
    "metadata": "<html>...</html>"
  }
  ```

#### Generate AI Plot Summary
- **Endpoint:** `POST /api/summary`
- **Request Body:**
  ```json
  {
    "book_title": "Frankenstein"
  }
  ```
- **Response:**
  ```json
  {
    "summary": "A scientist creates a monster that seeks revenge."
  }
  ```

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome! Please open an issue first to discuss changes.
