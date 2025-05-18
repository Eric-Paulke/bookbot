from stats import count_words, count_characters
def main():
    print(f"{count_words("books/frankenstein.txt")} words found in the document")
    print (count_characters("books/frankenstein.txt"))
main()
