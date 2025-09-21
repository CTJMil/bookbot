import sys
from stats import get_wordcount, get_char_count, sort_char_count

def main():
    try:
        book_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    wordcount = get_wordcount(book_path)
    charcount = get_char_count(book_path)
    sorted_char_count = sort_char_count(charcount)
    # print(f"{wordcount} words found in the document")
    # print(sorted_char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")

    for item in sorted_char_count:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")

    print("============= END ===============")
main()
