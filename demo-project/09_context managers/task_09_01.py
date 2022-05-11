from datetime import datetime


class MineManager:
    """Контекстный менеджер, выводящий в файл (указанный при конструировании менеджера) информацию
    по возникшей ошибке (в коде, обернутом контекстным менеджером), дате, времени выполнения кода.
    Выше ошибка прокидывается (происходит reraise)"""
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            with open(self.file_name, 'w') as out:
                print('Error ({}): {}: {}'.format(datetime.now(), exc_type.__name__, exc_val), file=out)
        return False


if __name__ == '__main__':
    with MineManager('output.txt'):
        for i in range(20):
            y = i ** 2
            if i == 10:
                y = y / 0  # Генерация ошибки
            print('{} = {}'.format(i, y))
