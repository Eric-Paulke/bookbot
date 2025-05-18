def get_book_text(dir):
    with open(dir) as f:
        text = f.read()
    return text

def count_words(text):
    list_words = get_book_text(text).split()
    return len(list_words)

def count_characters(text):
    char_count ={}
    text_lower = get_book_text(text).lower()
    for char in text_lower:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    return char_count
