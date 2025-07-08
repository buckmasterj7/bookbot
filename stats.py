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

def sort_on(items):
    return items["num"]

def get_sorted_character_list(character_count):
    characters = []
    for character in character_count:
        num = character_count[character]
        char_dict = {
            "char": character,
            "num" : num
        }
        characters.append(char_dict)
    characters.sort(reverse=True, key=sort_on)
    return characters


