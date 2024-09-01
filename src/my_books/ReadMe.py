from utils import File, Log

from my_books.Book import Book
from my_books.DDC import DDC

log = Log('ReadMe')


class ReadMe:
    PATH = 'README.md'

    def build(self):
        lines = ['# Books']

        previous_dewey_prefix = None
        for book in Book.list_all():
            dewey_prefix = book.dewey_prefix
            if dewey_prefix != previous_dewey_prefix:
                ddc_details = DDC.get(dewey_prefix)
                lines.extend(['', f'## {dewey_prefix}', '', f'`{ddc_details}`', ''])
                previous_dewey_prefix = dewey_prefix
            lines.append(book.readme_line)

        File(self.PATH).write_lines(lines)
        log.info(f'Wrote {self.PATH}')
