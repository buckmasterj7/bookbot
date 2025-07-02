def get_word_count(book_text):
    num_words = book_text.split()
    word_count = len(num_words)
    return word_count

def get_character_count(book_text):
    book_text_lower = book_text.lower()
    character_count = {}
    for text in book_text_lower:
        if text in character_count:
            character_count[text] += 1
        else:
            character_count[text] = 1
    return character_count
