from ..services.book_service import BookService
from ..utils.exceptions import LibraryError


class CLI:
    """
    Интерфейс командной строки для управления библиотекой.
    """

    def __init__(self):
        """Инициализация CLI с сервисом для работы с книгами."""
        self.book_service = BookService()
        self.commands = {
            'add': self.add_book,
            'remove': self.remove_book,
            'search': self.search_books,
            'list': self.list_books,
            'status': self.change_status,
            'help': self.show_help,
            'exit': self.exit
        }

    def run(self) -> None:
        """Запускает интерактивный режим работы с библиотекой."""
        print("Добро пожаловать в систему управления библиотекой!")
        self.show_help()

        while True:
            try:
                command = input("\nВведите команду: ").strip().lower()
                if command in self.commands:
                    if self.commands[command]() is False:
                        break
                else:
                    print("Неизвестная команда. Введите 'help' для справки.")
            except LibraryError as e:
                print(f"Ошибка: {str(e)}")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {str(e)}")

    def add_book(self) -> None:
        """Добавление новой книги."""
        print("\n=== Добавление новой книги ===")
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания: ")

        book = self.book_service.add_book(title, author, int(year))
        print(f"\nКнига успешно добавлена: {book}")

    def remove_book(self) -> None:
        """Удаление книги."""
        print("\n=== Удаление книги ===")
        book_id = int(input("Введите ID книги для удаления: "))
        self.book_service.remove_book(book_id)
        print("Книга успешно удалена")

    def search_books(self) -> None:
        """Поиск книг."""
        print("\n=== Поиск книг ===")
        print("Выберите тип поиска:")
        print("1. По названию")
        print("2. По автору")
        print("3. По году")

        choice = input("Ваш выбор (1-3): ")
        search_types = {'1': 'title', '2': 'author', '3': 'year'}

        if choice not in search_types:
            print("Некорректный выбор")
            return

        query = input("Введите поисковый запрос: ")
        books = self.book_service.search_books(query, search_types[choice])

        if books:
            print("\nНайденные книги:")
            for book in books:
                print(book)
        else:
            print("Книги не найдены")

    def list_books(self) -> None:
        """Отображение списка всех книг."""
        print("\n=== Список всех книг ===")
        books = self.book_service.get_all_books()
        if books:
            for book in books:
                print(book)
        else:
            print("Библиотека пуста")

    def change_status(self) -> None:
        """Изменение статуса книги."""
        print("\n=== Изменение статуса книги ===")
        book_id = int(input("Введите ID книги: "))
        print("Выберите новый статус:")
        print("1. В наличии")
        print("2. Выдана")

        choice = input("Ваш выбор (1-2): ")
        statuses = {'1': 'в наличии', '2': 'выдана'}

        if choice not in statuses:
            print("Некорректный выбор")
            return

        book = self.book_service.change_book_status(book_id, statuses[choice])
        print(f"Статус книги обновлен: {book}")

    def show_help(self) -> None:
        """Отображение справки по командам."""
        print("\nДоступные команды:")
        print("add    - Добавить новую книгу")
        print("remove - Удалить книгу")
        print("search - Поиск книги")
        print("list   - Показать все книги")
        print("status - Изменить статус книги")
        print("help   - Показать справку")
        print("exit   - Выйти из программы")

    def exit(self) -> bool:
        """Завершение работы программы."""
        print("\nСпасибо за использование библиотеки!")
        return False
