from datetime import datetime
from .exceptions import InvalidDataError


def validate_book_data(title: str, author: str, year: int) -> None:
    """
    Проверяет корректность данных книги.

    Args:
        title (str): Название книги
        author (str): Автор книги
        year (int): Год издания

    Raises:
        InvalidDataError: Если данные некорректны
    """
    if not title or not isinstance(title, str):
        raise InvalidDataError("Название книги должно быть непустой строкой")

    if not author or not isinstance(author, str):
        raise InvalidDataError("Имя автора должно быть непустой строкой")

    current_year = datetime.now().year
    try:
        year = int(year)
        if year < 1000 or year > current_year:
            raise InvalidDataError(f"Год должен быть между 1000 и {current_year}")
    except ValueError:
        raise InvalidDataError("Год должен быть числом")
