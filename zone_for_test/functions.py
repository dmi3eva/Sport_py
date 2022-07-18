from typing import *


class Dota:
    def __init__(self):
        self.x = 10
        self.title = "Pupa"


def foo(age: int, name: str, books: List[str], marks: List[int], game: Dota):
    print(id(age))
    print(id(name))
    print(id(books))
    print(id(marks))
    print(id(game))


a = 10
n = "Vasya"
b = ["Puh", "Harry"]
m = [5, 2, 3]
g = Dota()
print(id(a))
print(id(n))
print(id(b))
print(id(m))
print(id(g))
foo(a, n, b, m, g)