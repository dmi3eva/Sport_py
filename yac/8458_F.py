from typing import *
from dataclasses import dataclass

from queue import Queue
@dataclass
class City:
    ind: int
    x: int
    y: int
    done: bool = False
    distance: Optional[int] = 0


def get_distance(city_1: City, city_2: City) -> int:
    return abs(city_1.x - city_2.x) + abs(city_1.y - city_2.y)

def solve():
    cities = [None]
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        cities.append(City(i + 1, x, y))
    k = int(input())
    start, finish = map(int, input().split())


    q = Queue()
    q.put(cities[start])
    cities[start].done = True
    while q.qsize() > 0:
        current = q.get()
        if current.ind == finish:
            print(current.distance)
            return
        for _city in cities[1:]:
            if not _city.done and get_distance(_city, current) <= k:
                _city.distance = current.distance + 1
                _city.done = True
                q.put(_city)
    if not cities[finish].done:
        print(-1)
    else:
        print(cities[finish].distance)


solve()









