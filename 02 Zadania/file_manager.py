# Zad8/9

class FileManager:
    """
    Klasa służaca do obsugi plików za pomocą metod:

    read_file - wczytanie pliku

    update_file - modyfikacja pliku
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        try:
            file_opened = open(self.file_name, 'r', encoding='utf-8')
            file_read = file_opened.read()
            return file_read
        except IOError:
            return "Wystąpił błąd odczytu pliku."

    def update_file(self, text_data):
        try:
            file_opened = open(self.file_name, 'a', encoding='utf-8')
            file_opened.write(text_data)
            file_opened.close()
        except IOError:
            return "Wystąpił błąd zapisu pliku"
