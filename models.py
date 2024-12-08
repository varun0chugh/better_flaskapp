class Book:
    def __init__(self, book_id: int, title: str, author: str, published_year: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.published_year = published_year

class Member:
    def __init__(self, member_id: int, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
