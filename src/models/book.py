from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    """
    Модель книги в библиотеке.

    Attributes:
        title (str): Название книги
        author (str): Автор книги
        year (int): Год издания
        status (str): Статус книги ('в наличии' или 'выдана')
        id (Optional[int]): Уникальный идентификатор книги
    """
    title: str
    author: str
    year: int
    status: str = 'в наличии'
    id: Optional[int] = None

    def to_dict(self) -> dict:
        """Преобразует объект книги в словарь."""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        """Создает объект книги из словаря."""
        return cls(
            title=data['title'],
            author=data['author'],
            year=data['year'],
            status=data['status'],
            id=data['id']
        )

    def __str__(self) -> str:
        """Возвращает строковое представление книги."""
        return f"ID: {self.id} | {self.title} | {self.author} | {self.year} | {self.status}"