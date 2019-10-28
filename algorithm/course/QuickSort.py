'''
algorithmName: Quick Sort
author: Xu Mengnan
input: unordered array
output: ordered array
date: 2019/10/14
'''
import sys
import json
def quickSort(arr):
    """快速排序"""
    if len(arr) < 2:
        return arr
    # 选取基准，随便选哪个都可以，选中间的便于理解
    mid = arr[len(arr) // 2]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    arr.remove(mid)
    for i in arr:
        # 大于基准值放右边
        if i >= mid:
            right.append(i)
        else:
            # 小于基准值放左边
            left.append(i)
    # 使用迭代进行比较
    return quickSort(left) + [mid] + quickSort(right)

if __name__ == '__main__':
    temp = input("请输入整数序列，以逗号分隔:")
    a = temp.split(',')
    arr = list()
    # 格式转换
    for i in a:
        try:
            arr.append(int(i))
        except Exception as e:
            print("InputError: '{}'".format(i))
            sys.exit()
    print(json.dumps(quickSort(arr))[1:-1])