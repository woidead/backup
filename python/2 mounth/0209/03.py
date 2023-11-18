class Publication:
    def __init__(self, name, date, pages, library, type):
        self.name = name
        self.date = date
        self.pages = pages
        self.library = library
        self.type = type
    def info(self):
        print(f'{self.name}, {self.date}, {self.pages}, {self.library}, {self.type}')    
    
class Book(Publication):
    def __init__(self, type = 'book'):
        self.type = type
class Market(Publication):
    def __init__(self, type = 'market'):
        self.type = type
class Newspaper(Publication):
    def __init__(self, type = 'newspaper'):
        self.type = type
book = Book()
pub = Publication('РиП', '02.08.2022', '20','news', 'Newspaper')
pub.info()
