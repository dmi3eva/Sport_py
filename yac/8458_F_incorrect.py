from typing import *
from dataclasses import dataclass


@dataclass
class City:
    ind: int
    x: int
    y: int
    done: bool = False
    distance: Optional[int] = None
    steps = None


def get_distance(city_1: City, city_2: City) -> int:
    return abs(city_1.x - city_2.x) + abs(city_1.y - city_2.y)


cities = []
n = int(input())
for i in range(n):
    x, y = map(int, input())
    cities.append(City(i + 1, x, y))
k = int(input())
start, finish = map(int, input())



cities[start].distance = 0
cities[start].steps = 0
min_ind = start
for _ in range(n):
    improving_city = cities[min_ind]
    improving_city.done = True
    for candidate in cities:
        if candidate.done:
            continue
        current_distance = get_distance(improving_city, candidate) + improving_city.distance
        if not candidate.distance or current_distance < candidate.distance:
            candidate.distance = current_distance
            candidate.steps = improving_city.steps + 1
    min_distance = None
    for ind, city in enumerate(cities):
        if not city.done and (not min_distance or city.distance < min_distance):
            min_ind = ind
            min_distance = city.distance

if cities[finish].distance > k:
    print(-1)
else:
    print(cities[finish].steps)







