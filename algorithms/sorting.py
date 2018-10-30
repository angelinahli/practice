"""
FILENAME: sorting.py
AUTHOR: Angelina Li
DATE: 12/24/2017
DESC: Practice implementing the following sort methods:
- Selection sort
- Insertion sort
- Bubble sort
- Quick sort
- Merge sort
"""

class SortableList:

    def __init__(self, el_list):
        self.el_list = el_list

    def sort(smethod=quick_sort):
        self.el_list.smethod()

    def selection_sort():
        # last element is always sorted
        for i in range(len(self.el_list) - 1):
            smallest_index = i
            smallest_value = self.el_list[i]
            # don't need to check i or el_list[i] again
            for j in range(i + 1, len(self.el_list)):
                current_el = self.el_list[j]
                if current_el < smallest_val:
                    smallest_value = current_el
                    smallest_index = j
            _swap(self.el_list, i, smallest_index)

    def insertion_sort():
        # first element is already sorted
        for i in range(1, len(self.el_list)):
            for j in range(i):
                if self.el_list[j] > 

    def _swap(lst, i1, i2):
        lst[i1], lst[i2] = lst[i2], lst[i1]



