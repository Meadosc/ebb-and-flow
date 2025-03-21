import requests
from bs4 import BeautifulSoup


class GutenbergModel():
    base_url = f"https://www.gutenberg.org" 

    @classmethod
    def get_book(cls, book_id):
        content_url = f"{cls.base_url}/files/{book_id}/{book_id}-0.txt"
        metadata_url = f"{cls.base_url}/ebooks/{book_id}"

        content_response = requests.get(content_url)
        content = content_response.text

        metadata_response = requests.get(metadata_url)
        metadata_response = metadata_response.text
        book_title = get_gutenberg_title(metadata_response)

        response = {
            "content": content,
            "metadata": metadata_response,
            "book_title": book_title,
            "book_id": book_id,
        }
        return response


def get_gutenberg_title(metadata_response):
    soup = BeautifulSoup(metadata_response, "html.parser")

    title_tag = soup.find("h1", attrs={"itemprop": "name"})  # Look for main title
    if title_tag:
        return title_tag.text.strip()
    return "Title not found"
