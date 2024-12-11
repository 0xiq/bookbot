def main():
    book_path = "./books/frankenstein.txt"
    book = scan(book_path)
    num_words = count_words(book)
    num_chars = count_chars(book)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    count_alphabet_chars(num_chars)
    print("--- End report ---")


def scan(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    count = 0
    words = book.split()
    for w in words:
        count += 1
    return count

def count_chars(book):
    chars = {}
    for c in book:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def count_alphabet_chars(chars):
    new_chars = {}
    for c in chars:
        if c.isalpha():
            new_chars[c] = chars [c]
            print(f"The {c} character was found {new_chars[c]} times")

main()
