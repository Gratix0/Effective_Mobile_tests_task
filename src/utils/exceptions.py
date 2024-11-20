class LibraryError(Exception):
    """Базовый класс для исключений библиотеки."""
    pass

class BookNotFoundError(LibraryError):
    """Исключение, возникающее когда книга не найдена."""
    pass

class InvalidDataError(LibraryError):
    """Исключение, возникающее при некорректных данных."""
    pass