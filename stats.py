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

def sort_on(d):
    return d["num"]


def sort_charactercount(text):
    list_of_char = []
    dic_of_char = count_characters(text)
    for char in dic_of_char: 
        small_dic = {}
        small_dic = {"char":char,"num":dic_of_char[char]}
        if char.isalpha():
            list_of_char.append(small_dic)
    list_of_char.sort(reverse=True, key=sort_on) 
    return list_of_char
