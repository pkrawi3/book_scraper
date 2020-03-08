from flask import Flask, url_for, request
import json
from tinydb import TinyDB, Query
import scraper

# initiate flask app
app = Flask(__name__)

# initiate database to use
authors = TinyDB('50_authors.json')
author_query = Query()
books = TinyDB('200_books.json')
book_query = Query()

"""
Basic API Welcome: Ensures it is live
"""
@app.route('/')
def api_root():
    return 'Welcome'

"""
API Requests to be made for Authors
"""
@app.route('/authors', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def api_authors():
    if request.method == 'GET':
        query_parameters = request.args
        name = query_parameters.get('name')
        queried_author = authors.search(author_query.name == name)
        return queried_author[0]

    elif request.method == 'POST':
        query_parameters = request.args
        name = query_parameters.get('name')
        queried_author = authors.update(author_query.name == name)
        return queried_author[0]

    elif request.method == 'PUT':
        query_parameters = request.args
        name = query_parameters.get('name')
        queried_author = authors.insert()
        return "Added: {}".format(queried_author[0])

    elif request.method == 'DELETE':
        query_parameters = request.args
        name = query_parameters.get('name')
        authors.remove(author_query.name == name)
        return "Removed {}".format(name)

"""
API Requests to be made for Books
"""
@app.route('/books', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def api_books():
    if request.method == 'GET':
        query_parameters = request.args
        title = query_parameters.get('title')
        author = query_parameters.get('author')

        if title:
            queried_book = books.search(book_query.title == title)
            return queried_book[0]
        if author:
            queried_book = books.search(book_query.author == author)
            return queried_book[0]

    elif request.method == 'POST':
        query_parameters = request.args
        name = query_parameters.get('name')
        queried_author = authors.search(author_query.name == name)
        return queried_author[0]

    elif request.method == 'PUT':
        query_parameters = request.args
        name = query_parameters.get('name')
        queried_author = authors.search(author_query.name == name)
        return queried_author[0]

    elif request.method == 'DELETE':
        query_parameters = request.args
        title = query_parameters.get('title')
        books.remove(book_query.title == title)
        return "Removed {}".format(title)

if __name__ == '__main__':
    app.run()