from typing import List, Optional, Union
from ..models.book import Book
from ..services.storage_service import StorageService
from ..utils.exceptions import BookNotFoundError, InvalidDataError
from ..utils.validators import validate_book_data


class BookService:
    """
    Сервис для управления книгами в библиотеке.
    """

    def __init__(self):
        """Инициализация сервиса с хранилищем данных."""
        self.storage = StorageService()
        self._load_books()

    def _load_books(self) -> None:
        """Загружает книги из хранилища."""
        self.books = self.storage.load_books()
        self._update_next_id()

    def _update_next_id(self) -> None:
        """Обновляет счетчик ID для новых книг."""
        self.next_id = max([book.id for book in self.books], default=0) + 1

    def add_book(self, title: str, author: str, year: int) -> Book:
        """
        Добавляет новую книгу в библиотеку.

        Args:
            title (str): Название книги
            author (str): Автор книги
            year (int): Год издания

        Returns:
            Book: Добавленная книга

        Raises:
            InvalidDataError: Если данные книги некорректны
        """
        # Валидация данных
        validate_book_data(title, author, year)

        # Создание новой книги
        book = Book(title=title, author=author, year=year, id=self.next_id)
        self.books.append(book)
        self.next_id += 1

        # Сохранение изменений
        self.storage.save_books(self.books)
        return book

    def remove_book(self, book_id: int) -> None:
        """
        Удаляет книгу из библиотеки.

        Args:
            book_id (int): ID книги для удаления

        Raises:
            BookNotFoundError: Если книга не найдена
        """
        book = self.get_book_by_id(book_id)
        self.books.remove(book)
        self.storage.save_books(self.books)

    def search_books(self, query: str, search_type: str) -> List[Book]:
        """
        Поиск книг по заданным критериям.

        Args:
            query (str): Поисковый запрос
            search_type (str): Тип поиска ('title', 'author', 'year')

        Returns:
            List[Book]: Список найденных книг
        """
        query = query.lower()
        if search_type == 'year':
            try:
                year = int(query)
                return [book for book in self.books if book.year == year]
            except ValueError:
                raise InvalidDataError("Год должен быть числом")

        return [book for book in self.books
                if query in getattr(book, search_type).lower()]

    def get_all_books(self) -> List[Book]:
        """
        Возвращает список всех книг.

        Returns:
            List[Book]: Список всех книг
        """
        return self.books

    def change_book_status(self, book_id: int, new_status: str) -> Book:
        """
        Изменяет статус книги.

        Args:
            book_id (int): ID книги
            new_status (str): Новый статус

        Returns:
            Book: Обновленная книга

        Raises:
            BookNotFoundError: Если книга не найдена
            InvalidDataError: Если статус некорректен
        """
        if new_status not in ['в наличии', 'выдана']:
            raise InvalidDataError("Некорректный статус книги")

        book = self.get_book_by_id(book_id)
        book.status = new_status
        self.storage.save_books(self.books)
        return book

    def get_book_by_id(self, book_id: int) -> Book:
        """
        Получает книгу по ID.

        Args:
            book_id (int): ID книги

        Returns:
            Book: Найденная книга

        Raises:
            BookNotFoundError: Если книга не найдена
        """
        for book in self.books:
            if book.id == book_id:
                return book
        raise BookNotFoundError(f"Книга с ID {book_id} не найдена")
