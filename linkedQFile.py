class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    def __str__(self):
        return self.value


class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self, item):
        self.__last.next = item
    
    def dequeue(self):
        self.__first = self.__first.next