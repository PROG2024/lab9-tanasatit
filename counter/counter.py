"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""
import logging


class Counter:
    __instances = {}
    __count = 0

    def __new__(cls, *args, **kwargs):
        if not cls.__instances:
            cls.__instances = super().__new__(cls, *args, **kwargs)
        return cls.__instances

    def __str__(self):
        return f"{self.__count}"

    @property
    def count(self):
        return self.__count

    def increment(self):
        self.__count += 1
        return self.__count
