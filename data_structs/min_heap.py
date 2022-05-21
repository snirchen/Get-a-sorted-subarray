import math


class MinHeap:
    def __init__(self, arr: [int] = None) -> None:
        self.heap = []
        self.counter = 0
        self.current_size = 0
        if arr:
            self.build_min_heap_from_arr(arr)

    @staticmethod
    def __parent(i: int) -> int:
        """
        Function to return the index of
        parent for the node currently at index i
        """
        return i // 2

    @staticmethod
    def __left_child(i: int) -> int:
        """
        Function to return the index of
        the left child for the node currently at index i
        """
        return 2 * i

    @staticmethod
    def __right_child(i: int) -> int:
        """
        Function to return the index of
        the right child for the node currently at index i
        """
        return (2 * i) + 1

    def __swap(self, i1: int, i2: int) -> None:
        """
        Function to swap two nodes of the heap
        """
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

    def __is_leaf(self, pos) -> bool:
        """
        This function returns whether or not the node in
        the given pos is a leaf
        """
        return pos * 2 >= self.current_size - 1

    def __min_heapify(self, i: int) -> None:
        """
        Function to heapify the node at index i
        """
        if self.__is_leaf(i):
            return

        current_node_val = self.heap[i]
        left_child_val = self.heap[self.__left_child(i)]
        right_child_val = self.heap[self.__right_child(i)]

        self.counter += 2
        if current_node_val <= left_child_val and current_node_val <= right_child_val:
            return

        # If we get here, it means the current node is not a leaf,
        # and its value is not lower than its 2 children

        self.counter += 1
        if left_child_val < right_child_val:
            self.__swap(i, self.__left_child(i))
            self.__min_heapify(self.__left_child(i))
        else:
            self.__swap(i, self.__right_child(i))
            self.__min_heapify(self.__right_child(i))

    def insert(self, value: int) -> None:
        """
        Function to insert a node into the heap
        """
        self.heap.append(value)
        self.current_size += 1

        current = self.current_size - 1

        # This part takes care of the rearrangement of the MinHeap to
        # keep it follow the MinHeap rules
        while self.heap[current] < self.heap[self.__parent(current)]:
            self.__swap(current, self.__parent(current))
            current = self.__parent(current)

    def build_min_heap(self) -> None:
        """
        Function to build the min heap using
        the min_heapify function
        """
        for i in range(math.floor(self.current_size / 2), 0, -1):
            self.__min_heapify(i)

    def heap_extract_min(self) -> int:
        """
        Function to remove and return the minimum
        element from the heap. Then it arranges the MinHeap back
        """
        popped = self.heap[0]
        self.heap[0] = self.heap[self.current_size - 1]
        self.current_size -= 1
        self.__min_heapify(0)
        return popped

    def build_min_heap_from_arr(self, arr: [int]):
        for num in arr:
            self.insert(num)
        self.build_min_heap()
