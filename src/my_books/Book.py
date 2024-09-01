import os
import random
from dataclasses import dataclass

from utils import CSVFile, Log

log = Log('Book')


@dataclass
class Book:
    title: str
    subtitle: str
    author: str
    dewey: str
    isbn: str
    width: float

    @property
    def dewey_prefix(self):
        dewey_clean = self.dewey.replace(' ', '').replace('/', '')
        dewey_i = int(float(dewey_clean))
        return f'{dewey_i:03d}'

    @property
    def readme_line(self):
        return f'* [{self.author}] {self.title}'

    @staticmethod
    def from_dict(d):
        return Book(
            d['Title'],
            d['Subtitle'],
            d['Author'],
            d['Dewey'],
            d['ISBN'],
            d['Width'],
        )

    DATA_PATH = os.path.join('data', 'NUWANS_BOOKS.clz.20220304.csv')

    @staticmethod
    def list_all():
        data_list = CSVFile(Book.DATA_PATH).read()
        book_list = [Book.from_dict(data) for data in data_list]
        book_list = Book.sort_list(book_list)

        n = len(book_list)
        log.info(f'Loaded {n} books from {Book.DATA_PATH}')
        return book_list

    @staticmethod
    def sort_list(books):
        return sorted(books, key=lambda b: (b.dewey, b.author, b.title))

    @staticmethod
    def list_random(n):
        books = Book.list_all()
        return Book.sort_list(random.sample(books, n))
