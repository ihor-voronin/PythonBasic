class custom_context_file_reader:
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def read(self):
        return self.__file_object.read()

    def __exit__(self, type, val, tb):
        self.__file_object.close()
