def reverse(arr, start, end):
    if((start >= end)):
        return
    (arr[start], arr[end]) = (arr[end], arr[start])
    return reverse(arr, start + 1, end - 1)

array = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19]
print("Before reverse:", array)
reverse(array, 0, len(array) - 1)
print("After reverse:", array)
