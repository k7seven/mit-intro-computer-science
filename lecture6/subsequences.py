def subsequence(i, n, subsequence_array, input_array):
    if(i >= n):
        print(subsequence_array)
        return
    subsequence_array.append(input_array[i])
    subsequence(i + 1, n, subsequence_array, input_array)
    subsequence_array.remove(input_array[i])
    subsequence(i + 1, n, subsequence_array, input_array)

array = [3, 2, 1]
n = len(array)

subsequence(0, n, [], array)
