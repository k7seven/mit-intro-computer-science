# Problem 1 - Print all the subsequences which sum = x
def print_sum_x(input_array, n, i, subsequence_array, x, subsequence_sum):
    if(i >= n):
        if(subsequence_sum == x):
            print(subsequence_array)
            return
        return
    # take
    subsequence_array.append(input_array[i])
    subsequence_sum += input_array[i]
    print_sum_x(input_array, n, i + 1, subsequence_array, x, subsequence_sum)

    # not take
    subsequence_array.remove(input_array[i])
    subsequence_sum -= input_array[i]
    print_sum_x(input_array, n, i + 1, subsequence_array, x, subsequence_sum)


arr = [1, 2, 1, 2]
x = 4
array_length = len(arr)

print("Print all the subsequences which sum =", x)
print_sum_x(arr, array_length, 0, [], x, 0)

# Problem 2 - Print any subsequence which sum = x
def print_any_subsequence_sum_x(input_array, n, i, subsequence_array, x, subsequence_sum):
    if(i >= n):
        if(subsequence_sum == x):
            print(subsequence_array)
            return True
        return False
    # take
    subsequence_array.append(input_array[i])
    subsequence_sum += input_array[i]
    if (print_any_subsequence_sum_x(input_array, n, i + 1, subsequence_array, x, subsequence_sum) == True):
        return True

    # not take
    subsequence_array.remove(input_array[i])
    subsequence_sum -= input_array[i]
    if (print_any_subsequence_sum_x(input_array, n, i + 1, subsequence_array, x, subsequence_sum) == True):
        return True

    return False

print("Print any subsequences which sum =", x)
print_any_subsequence_sum_x(arr, array_length, 0, [], x, 0)

# Problem 3 - Count how many subsequences have sum =  x
def count_subsequences_sum_x(input_array, n, i, subsequence_array, x, subsequence_sum):
    if(i >= n):
        if(subsequence_sum == x):
            return 1
        return 0
    subsequence_array.append(input_array[i])
    subsequence_sum += input_array[i]
    left = count_subsequences_sum_x(input_array, n, i + 1, subsequence_array, x, subsequence_sum)

    subsequence_array.remove(input_array[i])
    subsequence_sum -= input_array[i]
    right = count_subsequences_sum_x(input_array, n, i + 1, subsequence_array, x, subsequence_sum)

    return left + right

print("Return the count of how many subsequences have sum =", x)
print(count_subsequences_sum_x(arr, array_length, 0, [], x, 0))
