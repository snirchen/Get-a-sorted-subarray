"""
This python file contains a class with akk the relevant functions to do a pivot sort
"""

import random


class PivotSort:

    def __init__(self):
        self.counter = 0

    def partition(self, arr: [int], p: int, r: int) -> int:
        pivot = arr[r]
        ptr = p
        for i in range(p, r):
            if arr[i] <= pivot:
                arr[i], arr[ptr] = arr[ptr], arr[i]
                ptr += 1
            self.counter += 1
        arr[ptr], arr[r] = arr[r], arr[ptr]
        return ptr

    def randomized_partition(self, arr: [int], p: int, r: int) -> int:
        i = random.randrange(p, r)
        arr[i], arr[r] = arr[r], arr[i]
        return self.partition(arr, p, r)

    def randomized_select(self, arr: [int], p: int, r: int, i: int, comp_counter: int) -> int:
        if p == r:
            return arr[p]
        q = self.randomized_partition(arr, p, r)
        k = q - p + 1
        if i == k:
            return arr[q]
        elif i < k:
            return self.randomized_select(arr, p, q - 1, i, comp_counter)
        else:
            return self.randomized_select(arr, q + 1, r, i - k, comp_counter)

    def quick_sort(self, arr: [int], p: int, r: int) -> None:
        """
        This function sort an array with a quick sort technique
        """
        if len(arr) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
            return arr
        if p < r:
            pi = self.partition(arr, p, r)
            self.quick_sort(arr, p, pi - 1)  # Recursively sorting the left values
            self.quick_sort(arr, pi + 1, r)  # Recursively sorting the right values
        return arr
