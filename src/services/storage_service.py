import json
from typing import List
from ..models.book import Book
from pathlib import Path

class StorageService:
    """
    Сервис для работы с хранилищем данных.
    """

    def __init__(self, filename: str = 'data/books.json'):
        """
        Инициализация сервиса хранения.

        Args:
            filename (str): Путь к файлу с данными
        """
        self.filename = Path(filename)
        self.filename.parent.mkdir(parents=True, exist_ok=True)
        if not self.filename.exists():
            self.filename.write_text('[]')

    def load_books(self) -> List[Book]:
        """
        Загружает книги из файла.

        Returns:
            List[Book]: Список книг
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Book.from_dict(book_data) for book_data in data]
        except json.JSONDecodeError:
            return []

    def save_books(self, books: List[Book]) -> None:
        """
        Сохраняет книги в файл.

        Args:
            books (List[Book]): Список книг для сохранения
        """
        data = [book.to_dict() for book in books]
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
