import unittest
from src.models.book import Book


class TestBook(unittest.TestCase):

    def setUp(self):
        """Инициализация данных для каждого теста"""
        self.book = Book(
            title="Тестовая книга",
            author="Тестовый автор",
            year=2023,
            id=1
        )

    def test_book_creation(self):
        """Тест создания книги"""
        self.assertEqual(self.book.title, "Тестовая книга")
        self.assertEqual(self.book.author, "Тестовый автор")
        self.assertEqual(self.book.year, 2023)
        self.assertEqual(self.book.status, "в наличии")
        self.assertEqual(self.book.id, 1)

    def test_book_to_dict(self):
        """Тест преобразования книги в словарь"""
        book_dict = self.book.to_dict()
        self.assertEqual(book_dict['title'], "Тестовая книга")
        self.assertEqual(book_dict['author'], "Тестовый автор")
        self.assertEqual(book_dict['year'], 2023)
        self.assertEqual(book_dict['status'], "в наличии")
        self.assertEqual(book_dict['id'], 1)

    def test_book_from_dict(self):
        """Тест создания книги из словаря"""
        book_dict = {
            'title': "Тестовая книга",
            'author': "Тестовый автор",
            'year': 2023,
            'status': "в наличии",
            'id': 1
        }
        book = Book.from_dict(book_dict)
        self.assertEqual(book.title, "Тестовая книга")
        self.assertEqual(book.author, "Тестовый автор")
        self.assertEqual(book.year, 2023)
        self.assertEqual(book.status, "в наличии")
        self.assertEqual(book.id, 1)


if __name__ == '__main__':
    unittest.main()
