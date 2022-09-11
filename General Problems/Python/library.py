class Page:
    def __init__(self, number: int, content: str):
        self._number = number
        self._content = content

    @property
    def number(self):
        return self._number

    @property
    def content(self):
        return self._content


class Book:
    def __init__(self, title: str, size: int, pages: list):
        self._title = title
        self._size = size
        self._pages = pages

    @property
    def title(self):
        return self._title

    @property
    def size(self):
        return self._size

    @property
    def pages(self):
        return self._pages

    def read_page(self, number: int):
        try:
            print(self.pages[number - 1].content)
        except:
            print('The book does not this page.')

    def read_book(self):
        for page in self.pages:
            print(page.content)


class Library:
    def __init__(self, name: str, books: list):
        self._name = name
        self._books = books

    @property
    def name(self):
        return self._name

    @property
    def books(self):
        return self._books

    def find_book(self, title: str) -> Book or None:
        for book in books:
            if book.title == title:
                return book
        print(f'The book {title} does not exist in our colletion.')


if __name__ == '__main__':

    first_book_size = 25
    first_book_pages = [Page(index + 1, content) for index, content in enumerate(['Harry does something, blah blah blah.' for _ in range(first_book_size)])]
    first_book = Book('Harry Potter ... I think', first_book_size, first_book_pages)

    second_book_size = 50
    second_book_pages = [Page(index + 1, content) for index, content in enumerate(['Nice and Steady.' for _ in range(second_book_size)])]
    second_book = Book('All is good in the world', second_book_size, second_book_pages)

    books = [first_book, second_book]
    our_library = Library('Our Library', books)

    our_library.find_book('Harry Potter ... I think').read_book()
    our_library.find_book('All is good in the world').read_book()
