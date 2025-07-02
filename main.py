def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents    
    
from stats import get_word_count
from stats import get_character_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    print(f"{word_count} words found in the document")
    print(character_count)

main()
