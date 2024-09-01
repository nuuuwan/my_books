from my_books import Book


def main():
    print()
    print('-' * 80)
    print()
    
    N = 10
    random_books = Book.list_random(N)
    for book in random_books:
        print(book.readme_line)
    
    print()
    print('-' * 80)
    print()
    

if __name__ == "__main__":
    main()
