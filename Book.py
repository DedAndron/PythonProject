class Book:
    def __init__(self, title: str, author: str, year: int, pages: int):
        self.title = title
        self.author = author
        if year<2027:
            self.year = year
        else:
            raise ValueError('The year cannot be less than 2027')
        if pages > 0:
            self.pages = pages
        else:
            self.pages = 0
    def __str__(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'pages': self.pages
        }
    def __repr__(self):
        return f'{self.title} by {self.author} on {self.year} with {self.pages} pages'
    def __len__(self):
        return f'{self.title} have {self.pages} pages'
    def __eq__(self, book):
        if book.title == self.title and book.author == self.author:
            return 'They titles and authors are the same'
        else:
            return 'They titles and authors are not the same'
    def __lt__(self, book):
        if book.pages < self.pages:
            return f'{self.title} has more pages'
        else:
            return f'{book.title} has more pages'
    def __add__(self, book):
        return f'{self.title} and {book.title} together have {self.pages + book.pages} pages'
    def __contains__(self, word):
        if word in self.title:
            return f'The word "{word}" is in the title'
        else:
            return f'The word "{word}" is not in the title'
    def __bool__(self):
        if self.pages > 0:
            return f'{self.title} is not empty'
        else:
            return f'{self.title} is empty'