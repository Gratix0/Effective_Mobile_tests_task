import unittest
import tempfile
import json
from pathlib import Path
from src.services.storage_service import StorageService
from src.models.book import Book


class TestStorageService(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.temp_file = Path(self.temp_dir) / "test_books.json"
        self.storage = StorageService(str(self.temp_file))

    def test_save_and_load_books(self):
        """Тест сохранения и загрузки книг"""
        books = [
            Book("Книга 1", "Автор 1", 2023, id=1),
            Book("Книга 2", "Автор 2", 2022, id=2)
        ]

        self.storage.save_books(books)
        loaded_books = self.storage.load_books()

        self.assertEqual(len(loaded_books), 2)
        self.assertEqual(loaded_books[0].title, "Книга 1")
        self.assertEqual(loaded_books[1].title, "Книга 2")

    def test_load_empty_file(self):
        """Тест загрузки из пустого файла"""
        loaded_books = self.storage.load_books()
        self.assertEqual(len(loaded_books), 0)

    def tearDown(self):
        self.temp_file.unlink(missing_ok=True)