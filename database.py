books_db = {}
members_db = {}

def add_book(book):
    books_db[book.book_id] = book

def get_book(book_id):
    return books_db.get(book_id)

def delete_book(book_id):
    return books_db.pop(book_id, None)

def list_books():
    return list(books_db.values())

def add_member(member):
    members_db[member.member_id] = member

def get_member(member_id):
    return members_db.get(member_id)

def delete_member(member_id):
    return members_db.pop(member_id, None)

def list_members():
    return list(members_db.values())
