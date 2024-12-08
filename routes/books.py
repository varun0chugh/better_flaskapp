from flask import Blueprint, jsonify, request
from models import Book
from database import books_db, add_book, get_book, delete_book, list_books
from helper.pagination import paginate
from helper.search import search

books_blueprint = Blueprint('books', __name__)

@books_blueprint.route('/', methods=['GET'])
def get_books():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    books = list_books()
    result = paginate(books, page, per_page)
    return jsonify(result), 200
@books_blueprint.route('/search', methods=['GET'])
def search_books():
    title = request.args.get('title', '').lower()
    author = request.args.get('author', '').lower()
    books = [vars(book) for book in list_books()]
    query = {"title": title, "author": author}
    resultss = search(books, query)
    return jsonify(resultss), 200
@books_blueprint.route('/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = get_book(book_id)
    if book:
        return jsonify(vars(book)), 200
    return jsonify({'message': 'Book not found'}), 404
@books_blueprint.route('/', methods=['POST'])
def add_new_book():
    data = request.json
    book = Book(book_id=len(books_db) + 1, title=data['title'], author=data['author'], published_year=data['published_year'])
    add_book(book)
    return jsonify(vars(book)), 201
@books_blueprint.route('/<int:book_id>', methods=['DELETE'])
def delete_book_by_id(book_id):
    book = delete_book(book_id)
    if book:
        return jsonify({'message': 'Book deleted'}), 200
    return jsonify({'message': 'Book not found'}), 404
