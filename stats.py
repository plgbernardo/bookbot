def char_count(text):
    words = {}

    for i in text:
        char = i.lower()

        if char in words:
            words[char] += 1
        else:
            words[char] = 1

    return words

def word_count(title):
    return len(title.split())
