'''
algorithmName: Binary Search
author: Xu Mengnan
input: Non-decrementing array, a number that need to looked up.
output: position or "not found"
date: 2019/10/14
'''
import sys


def binarySearch(arr, num):
    left = 0
    right = len(arr)
    mid = (left + right) // 2
    while(left<=right):
        if arr[mid] == num:
            return mid
        if arr[mid] < num:
            left = mid + 1
            mid = (left + right) // 2
        if arr[mid] > num:
            right = mid - 1
            mid = (left + right) // 2

if __name__ == '__main__':
    temp = input("请输入整数序列，以逗号分隔，要求序列非递减:")
    a = temp.split(',')
    arr = []
    # 格式转换
    for i in a:
        try:
            arr.append(int(i))
        except Exception as e:
            print("InputError:{}".format(i))
            sys.exit()
    #判断合法性
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            print("InputError: {}, {}".format(arr[i], arr[i+1]))
            sys.exit()
    num = int(input("请输入要查找的数字"))
    print(binarySearch(arr, num))