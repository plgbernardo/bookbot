from stats import char_count, word_count
import sys

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_name = sys.argv[1].split("/")[-1]
    book_path = sys.argv[1]
    
    title = get_book(book_path)
    sumary(book_name, word_count(title), char_count(title))

def sumary(b_name, w_count, dict):
    print(f"\n--- Begin report of {b_name} ---")
    print(f"{w_count} words found in the document\n")

    dict_to_list = [(key, value) for key, value in dict.items()]
    dict_to_list.sort(reverse=True, key=lambda x: x[1])
    
    for i, j in dict_to_list:
        if i.isalpha():
            print(f"{i}: {j}")

    print(f"\n--- End report ---\n")

def get_book(title):
    with open(title) as f:
        return f.read()

main()