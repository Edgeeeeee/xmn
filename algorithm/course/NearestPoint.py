'''
AlgorithmName: Nearest Point
Author: Xu Mengnan
date: 2019/10/14
Input: the amount of point and point coordinate.
Output: the closest two points and distance
'''
from math import sqrt
import sys

class Point():
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

def get_distance(point):
    return sqrt((point[0].x-point[1].x)**2 + (point[0].y-point[1].y)**2)


def nearestPoint(orderedPointList):
    m = len(orderedPointList) // 2
    left, right = [], []
    for i in range(m):
        left.append(orderedPointList[i])
    for i in range(m, len(orderedPointList)):
        right.append(orderedPointList[i])
    if len(left) >= 2:
        left_nearest_point = nearestPoint(left)
        left_min_distance = get_distance(left_nearest_point)
    else:
        left_min_distance = float("inf")
    if len(right) >= 2:
        right_nearest_point = nearestPoint(right)
        right_min_distance = get_distance(right_nearest_point)
    else:
        right_min_distance = float("inf")
    d = min(left_min_distance,right_min_distance)

    candidate = []
    for i in left:
        if orderedPointList[m].x - i.x < d:
            for j in right:
                if abs(i.x - j.x) < d and abs(i.y - j.y) < d:
                    if get_distance((i,j)) < d:
                        candidate.append((i,j))
    if candidate:
        dic = []
        for i in candidate:
            dic.append({get_distance(i): i})
        dic.sort(key=lambda x: x.keys())
        for item in dic[0].values():
            return item
    elif left_min_distance < right_min_distance:
        return left_nearest_point
    else:
        return right_nearest_point


if __name__ == '__main__':
    pointList = []
    amount = int(input("输入点的数量"))
    if amount < 2:
        print(float("inf"))
        sys.exit()
    for i in range(amount):
        temp = input("请输入第{}个点的x，y坐标".format(i))
        x,y = temp.strip(' ').split(" ")
        a = Point(int(x),int(y),i)
        pointList.append(a)
    orderedPointList = sorted(pointList, key=lambda a: a.x)
    x,y = nearestPoint(orderedPointList)
    print('({},{}), ({},{})'.format(x.x,x.y,y.x,y.y))