from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.files = []

    def __len__(self):
        return len(self.files)

    def enqueue(self, value):
        self.files.append(value)

    def dequeue(self):
        if len(self.files) > 0:
            return self.files.pop(0)
        else:
            raise IndexError("Índice Inválido ou Inexistente")

    def search(self, index):
        if 0 <= index <= (len(self.files) - 1):
            return self.files[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")
