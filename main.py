from shedule_class import FileShedule
from watchdog.observers import Observer
try:
    while True:
        print("Введите словов: ")
        true: bool = True
        word: str = input()
        if word.isalpha() and len(word) > 3:
            file = f"D:\\Programmirovanie\\SergeyAntuh.Python.PR2\\test\\{word}.txt"
            with open (file, "w"):
                print("Успешное создание файла")
        else:
            print("Введите корректно данные")
except Exception:
    print("Произошла ошибка")
except KeyboardInterrupt:
    print("Заверешение работы")