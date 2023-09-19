def is_palindrome(arr, start, end):
    if(start >= end):
        return True
    if(arr[start] != arr[end]):
        return False
    return is_palindrome(arr, start + 1, end - 1)

word = "saippuakivikauppias"
start = 0
end = len(word) - 1
print(is_palindrome(word, start, end))
