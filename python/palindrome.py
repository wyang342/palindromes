def palindrome(word):
    word = word.lower()
    word_reversed = word[::-1]
    if (word == word_reversed):
        return True
    else:
        return False
