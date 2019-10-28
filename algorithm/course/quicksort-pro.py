quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])

if __name__ == '__main__':
    text = [1,4,16,64,342,231,55,313,56,24,2,31]
    res = quick_sort(text)
    print(res)