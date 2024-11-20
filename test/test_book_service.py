import unittest
from unittest.mock import Mock, patch
from src.services.book_service import BookService
from src.models.book import Book
from src.utils.exceptions import BookNotFoundError, InvalidDataError


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book_service = BookService()
        self.book_service.storage.save_books([])  # Очищаем хранилище перед каждым тестом

    def test_add_book(self):
        """Тест добавления книги"""
        book = self.book_service.add_book("Тестовая книга", "Автор", 2023)
        self.assertEqual(book.title, "Тестовая книга")
        self.assertEqual(len(self.book_service.get_all_books()), 1)

    def test_add_invalid_book(self):
        """Тест добавления книги с некорректными данными"""
        with self.assertRaises(InvalidDataError):
            self.book_service.add_book("", "Автор", 2023)

    def test_remove_book(self):
        """Тест удаления книги"""
        book = self.book_service.add_book("Тестовая книга", "Автор", 2023)
        self.book_service.remove_book(book.id)
        self.assertEqual(len(self.book_service.get_all_books()), 1)

    def test_remove_nonexistent_book(self):
        """Тест удаления несуществующей книги"""
        with self.assertRaises(BookNotFoundError):
            self.book_service.remove_book(999)

    def test_search_books(self):
        """Тест поиска книг"""
        self.book_service.add_book("Тестовая книга", "Автор", 2023)
        self.book_service.add_book("Другая книга", "Другой автор", 2022)

        results = self.book_service.search_books("Тестовая", "title")
        self.assertEqual(len(results), 1)

    def test_change_book_status(self):
        """Тест изменения статуса книги"""
        book = self.book_service.add_book("Тестовая книга", "Автор", 2023)
        updated_book = self.book_service.change_book_status(book.id, "выдана")
        self.assertEqual(updated_book.status, "выдана")
