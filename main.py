from stats import count_words, count_characters, sort_charactercount
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(sys.argv[1])
        print("---------- Word Count ----------")
        print(f"Found {count_words(sys.argv[1])} total words")
        print("--------- Character Count -------")
        for char_dic in sort_charactercount(sys.argv[1]):
            print(f"{char_dic["char"]}: {char_dic["num"]}")
        print("============= END ===============")
main()