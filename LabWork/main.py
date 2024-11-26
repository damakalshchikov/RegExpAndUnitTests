import funcs


def main() -> None:
    choice = input("Где искать номера карт? (1 - ввод текста, 2 - URL, 3 - файл): ")

    match choice:
        case "1":
            text = input("Введите текст: ")
        case "2":
            url = input("Введите URL: ")
            text = funcs.get_content_from_url(url)
        case "3":
            file_path = input("Введите путь к файлу: ")

            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    text = file.read()
            except FileNotFoundError:
                print("Файл не найден")
        case _:
            print("Неверный выбор")

    matches = funcs.find_credit_card_numbers(text)
    if matches:
        print("Найденные номера карт:")
        for match in matches:
            print(match)
    else:
        print("Номера банковских карт не найдены")


if __name__ == "__main__":
    main()
else:
    print("Запускай main.py")
