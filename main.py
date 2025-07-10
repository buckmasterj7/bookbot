import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents    
    
from stats import get_word_count
from stats import get_character_count
from stats import get_sorted_character_list

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    characters = get_sorted_character_list(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in characters:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()

