import json
import os


class DBModel:
    db_path = '/home/data/db.json'

    @classmethod
    def get_all_data(cls):
        # Check if db.json exists, and if not, create it
        os.makedirs(os.path.dirname(cls.db_path), exist_ok=True)
        if not os.path.exists(cls.db_path):
            with open(cls.db_path, 'w') as f:
                json.dump({}, f)  # Initialize with an empty dictionary

        with open(cls.db_path, 'r') as f:
            try:
                db_data = json.load(f)
            except json.decoder.JSONDecodeError:
                db_data = {}
        return db_data
    
    @classmethod
    def get_book_list(cls):
        data = cls.get_all_data()
        return [{"book_id": k, "book_title": v['book_title']} for k, v in data.items()]
    
    @classmethod
    def get_book(cls, book_id):
        data = cls.get_all_data()
        return data.get(str(book_id), {})
    
    @classmethod
    def add_book(cls, book_data):
        db_data = cls.get_all_data()
        db_data[book_data['book_id']] = book_data
        with open(cls.db_path, 'w') as f:
            json.dump(db_data, f)
        return True
