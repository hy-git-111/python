import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count