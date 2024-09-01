from utils import File, Log
from my_books.Book import Book

log = Log('ReadMe')


class ReadMe:
    PATH = 'README.md'

    def build(self):
        lines = ['# Books']

        previous_dewey_prefix = None
        for book in Book.list_all():
            dewer_prefix = book.dewey_prefix
            if dewer_prefix != previous_dewey_prefix:
                lines.extend(['', f'## {dewer_prefix}', ''])
                previous_dewey_prefix = dewer_prefix
            lines.append(book.readme_line)

        File(self.PATH).write_lines(lines)
        log.info(f'Wrote {self.PATH}')
