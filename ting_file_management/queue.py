from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._data.pop(0)

    def size(self):
        return len(self._data)

    def is_empty(self):
        return not self.size()

    def search(self, index):
        if self.is_empty() or index > self.size() - 1 or index < 0:
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]
