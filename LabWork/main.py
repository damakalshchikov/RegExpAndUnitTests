import funcs
import regexp_classes


def main(pattern: str) -> None:
    regexp_finder: regexp_classes.RegExpFinder = regexp_classes.RegExpFinder(pattern)
    choice: str = input("Где искать номера карт? (1 - ввод текста, 2 - URL, 3 - файл): ")

    match choice:
        case "1":
            text = input("Введите текст: ")
        case "2":
            url: str = input("Введите URL: ")
            raw_html: str = funcs.get_content_from_url(url)

            if not raw_html:
                print('Ошибка: не удалось загрузить данные с указанного URL')
                return

            text: str = funcs.extract_text_from_html(raw_html)
        case "3":
            file_path = input("Введите путь к файлу: ")

            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    text = file.read()
            except FileNotFoundError:
                print("Файл не найден")
        case _:
            print("Неверный выбор")

    matches = regexp_finder.find_regexp(text)
    if matches:
        print("Найденные номера карт:")
        for match in matches:
            print(match)
    else:
        print("Номера банковских карт не найдены")


if __name__ == "__main__":
    regexp_pattern: str = r"\b(?:\d{4}[-\s]?){3}\d{4}\b"
    main(regexp_pattern)
else:
    print("Запускай main.py")
