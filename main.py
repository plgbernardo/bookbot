def main():
    book_name = "frankenstein"
    book_path = "books/" + book_name + ".txt"
    
    title = get_book(book_path)
    sumary(book_name, word_count(title), char_count(title))

def sumary(b_name, w_count, dict):
    print(f"\n--- Begin report of {b_name} ---")
    print(f"{w_count} words found in the document\n")

    dict_to_list = [(key, value) for key, value in dict.items()]
    dict_to_list.sort(reverse=True, key=lambda x: x[1])
    
    for i, j in dict_to_list:
        if i.isalpha():
            print(f"The '{i}' character was found {j} times")

    print(f"\n--- End report ---\n")

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

def get_book(title):
    with open(title) as f:
        return f.read()

main()