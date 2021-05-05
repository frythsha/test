from random import randint
import math


def keyFunc(item):
    x = item[0]
    y = item[1]
    if x <= 0:
        return math.acos(y / ((x ** 2 + y ** 2) ** 0.5))
    else:
        return math.pi * 2 - math.acos(y / ((x ** 2 + y ** 2) ** 0.5))


n = int(input())
points = [(randint(-100, 100), randint(-100, 100)) for i in range(0, n)]

points.sort(key=keyFunc)
last = len(points) - 1
if points[last][0] > 0 and points[last][1] > 0:
    points.insert(0, points.pop(last))
print('Sorted points:', points)

dist = [(points[i][0] ** 2 + points[i][1] ** 2) ** 0.5 for i in range(0, n)]
print(
    'Maximal distance =', max(dist),
    '\n' + 'Minimal distance =', min(dist),
    '\n' + 'Average distance =', math.fsum(dist) / n)
