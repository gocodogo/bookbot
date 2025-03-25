from stats import get_num_words, get_num_characters
from stats import sort_dict
import sys


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    # books/frankenstein.txt

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_characters(text)

    # print(char_count)
    sorted_list = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    for entry in sorted_list:
        if entry['name'].isalpha():
            print(f"{entry['name']}: {entry['value']}")



    print("============= END ===============")



def get_book_text(path_to_file):
    book_content = ""
    with open(path_to_file) as f:
        book_content = f.read()
    return book_content
 
main()
