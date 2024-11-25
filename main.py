from library_functionality import Library


def menu() -> str:
    """Функция выводит меню приложения"""

    start: int = 1
    print("Welcome to Library!")

    while start:
        print("-" * 10)
        print("1. Добавить книгу.\n2. Удалить книгу.\n3. Найти книгу.\n4. Вывести список книг.\n"
              "5. Изменить статус книги.\n6. Завершить приложение.")
        print("-" * 10)

        answer: str = input("Выберите пункт меню: ")
        print("\033[H\033[J")
        lib = Library()
        match answer:
            case "1":
                print(lib.add_book())
            case "2":
                print(lib.remove_book())
            case "3":
                print(lib.search_book())
            case "4":
                print(lib.display_book())
            case "5":
                print(lib.update_status_book())
            case "6":
                start = 0
    return "Приложение завершило работу!"


if __name__ == "__main__":
    print(menu())
