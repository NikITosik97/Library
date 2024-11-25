from write_and_read import read_file, write_file


class Library:

    def add_book(self) -> str:
        """Функция добовляет книгу в library.json"""

        title: str = input('Введите название книги: ')
        author: str = input('Введите автора книги: ')
        while True:
            try:
                year: int = int(input('Введите год книги: '))
                if 999 <= int(year) <= 9999:
                    break
                else:
                    print("Год должен содержать 4 цыфры...Попробуйте снова!")
            except ValueError:
                print("Данные не корректны...Попробуйте снова!")

        books: dict = read_file()
        books_id: list = list(map(int, list(books.keys())))
        book_id: int = 0
        while True:
            if book_id in books_id:
                book_id += 1
            else:
                break

        result: dict = {
            book_id: {
                "title": title,
                "author": author,
                "year": str(year),
                "status": True
            }
        }

        books.update(result)
        write_file(books)

        print("-" * 10)
        return "Данные успешно добавлены!"

    def remove_book(self) -> str:
        """Функция удаляет книгу из library.json"""

        id_book: str = input("Введите ID книги для ee удаления: ")
        books: dict = read_file()
        if len(books) == 0 or id_book not in books:
            return "Данной книги нет в наличии!"

        for id_ in books:
            if id_book == id_:
                books.pop(id_)
                break

        write_file(books)
        print("-" * 10)
        return "Книга удалена!"

    def search_book(self) -> str:
        """Функция делает поиск нужной книги в library.json"""

        search_book: str = input("Введите название книги, автора или год издания: ")
        books: dict = read_file()
        lst_books: list = []
        for id_ in books:
            book = books.get(id_)
            for val in book:
                if book.get(val) == search_book:
                    lst_books.append(books[id_])
                    break
        if len(lst_books) == 0:
            return "Книга не была найдена!"
        for val_book in lst_books:
            title = val_book['title']
            author = val_book['author']
            year = val_book['year']
            status = "В наличии" if val_book['status'] == True else "Выдана"

            print(f"Title: {title}\nAuthor: {author}\nYear: {year}\nStatus: {status}")
            print("-" * 10)

        return "Данные выгружены успешно!"

    def display_book(self) -> str:
        """Функция собирает все книги из library.json"""

        books: dict = read_file()
        if len(books) == 0:
            return 'Книг нет!'
        for id_ in books:
            print(f"ID: {id_} ")
            title: str = books[id_]['title']
            author: str = books[id_]['author']
            year: str = books[id_]['year']
            status: str = "В наличии" if books[id_]['status'] == True else "Выдана"
            print(f"Title: {title}\nAuthor: {author}\nYear: {year}\nStatus: {status}")
            print("-" * 10)
        return "Данные выгружены успешно!"

    def update_status_book(self) -> str:
        """Функция меняет статус книги"""

        id_book: str = input("Введите ID книги: ")
        books: dict = read_file()
        if id_book not in books:
            return 'Данной книги нет!'
        select_status: str = input("1. В наличии.\n2. Выдана.\nВведите статус книги: ")
        status_books: bool = books[id_book]['status']
        if select_status == '1' and status_books == True:
            return 'Книга уже в наличии!'
        elif select_status == '2' and status_books == False:
            return 'Книга уже выдана!'
        else:
            match select_status:
                case '1':
                    books[id_book]['status'] = True
                case '2':
                    books[id_book]['status'] = False

        write_file(books)

        return "Статус изменен!"
