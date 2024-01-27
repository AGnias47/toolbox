class FullHeapException(Exception):
    def __init__(self):
        super().__init__("No space left on heap")


class Heap:
    def __init__(self, max_size=2048):
        self.first_element_index = 1
        self.max_size = max_size + self.first_element_index
        self._heap = [None] * self.max_size

    @property
    def size(self):
        i = self.first_element_index
        try:
            while self._heap[i]:
                i += 1
            return i - self.first_element_index
        except IndexError:
            return i - self.first_element_index

    @property
    def height(self):
        h = 0
        i = self.first_element_index * 2
        try:
            while self._heap[i]:
                h += 1
                i *= 2
            return h
        except IndexError:
            return h

    def is_full(self):
        return self.size == self.max_size

    def insert(self, v):
        if self.is_full():
            raise FullHeapException
        i = self.size + self.first_element_index
        self._heap[i] = v
        self.heapify_up(i)

    def find_min(self):
        return self._heap[self.first_element_index]

    def delete(self, i):
        self._heap[i] = self._heap[self.size]
        self._heap[self.size] = None
        self.heapify_down(i)

    def extract_min(self):
        heap_min = self.find_min()
        self.delete(self.first_element_index)
        self.heapify_down(self.first_element_index)
        return heap_min

    def heapify_up(self, i):
        if i > self.first_element_index:
            j = self.parent(i)
            if self._heap[i] < self._heap[j]:
                self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
                self.heapify_up(j)

    def heapify_down(self, i):
        n = self.size
        if 2 * i > n:
            return
        elif 2 * i == n:
            j = 2 * i
        else:
            left_child = self.left_child(i)
            right_child = self.right_child(i)
            if self._heap[left_child] <= self._heap[right_child]:
                j = left_child
            else:
                j = right_child
        if self._heap[j] < self._heap[i]:
            self._heap[j], self._heap[i] = self._heap[i], self._heap[j]
            self.heapify_down(j)

    @staticmethod
    def left_child(i):
        return 2 * i

    @staticmethod
    def right_child(i):
        return 2 * i + 1

    @staticmethod
    def parent(i):
        return i // 2
