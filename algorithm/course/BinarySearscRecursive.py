'''
algorithmName: Binary Search
author: Xu Mengnan
input: Non-decrementing array, a number that need to looked up.
output: position or "not found"
date: 2019/10/14
'''
import sys
def binarySearch(arr, num, low, high):
    # 格式转换，判断输入是否合法

    mid = (low + high) // 2
    if low == high:
        if arr[mid] == num:
            print(low)
            sys.exit()
        else:
            print("not found")
            sys.exit()
    if arr[mid] == num:
        print(mid)
        sys.exit()
    if arr[mid] < num:
        binarySearch(arr, num, mid+1, high)
    if arr[mid] > num:
        binarySearch(arr, num, low, mid-1)


if __name__ == '__main__':
    temp = input("请输入整数序列，以逗号分隔，要求序列非递减:")
    a = temp.split(',')
    arr = list()

    # 格式转换
    for i in a:
        try:
            arr.append(int(i))
        except Exception as e:
            print("InputError: '{}'".format(i))
            sys.exit()
    #判断合法性
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            print("InputError: {}, {}".format(arr[i], arr[i+1]))
            sys.exit()

    num = int(input("请输入要查找的数字"))
    binarySearch(arr, num, low=0, high=len(a)-1)
