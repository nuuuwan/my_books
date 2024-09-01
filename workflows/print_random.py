import random
from my_books import Book


def main():
    books = Book.list_all()
    random.shuffle(books)
    N = 10
    for book in books[:N]:
        print(book.readme_line)


if __name__ == "__main__":
    main()
