import sys
from stats import get_text_count, get_char_dict, get_sorted_dict

def get_file_text(path):
    with open(path) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_file_text(file_path)
    text_count = get_text_count(book_text)
    char_dict = get_char_dict(book_text)
    sorted_dict = get_sorted_dict(char_dict)
    print_output(file_path, text_count, sorted_dict)

def print_output(file_path, text_count, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {text_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_dict:
        print(f"{dict['char']}: {dict['count']}")
    print("============= END ===============")

main()