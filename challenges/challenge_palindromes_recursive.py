def is_palindrome_recursive(word, low_index, high_index):
    # https://machadodev.github.io/Recursion/
    if word == '':
        return False
    while high_index > low_index:
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return False
    return True
