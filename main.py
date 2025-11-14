from stats import get_num_words, get_num_chars, get_sorted_characters
import sys
import os

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        book_text = get_book_text(book_path)
    except Exception:
        print("Invalid path to book, quitting")
        sys.exit(1)

    book_bots_string = "============ BOOKBOT ============"
    word_count_string = "----------- Word Count ----------"
    character_count_string = "--------- Character Count -------"
    end_string = "============= END ==============="

    analyzing_string = f"Analyzing book found at {book_path}..."
    
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    sorted_characters = get_sorted_characters(num_chars)

    print(book_bots_string)
    print(analyzing_string)
    print(word_count_string)
    print(f"Found {num_words} total words")
    print(character_count_string)

    for character_num_pair in sorted_characters:
        if not character_num_pair["char"].isalpha():
            continue
        print(f'{character_num_pair["char"]}: {character_num_pair["num"]}')
    print(end_string)
    #print(get_book_text(book_path))

main()