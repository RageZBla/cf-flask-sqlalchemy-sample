import os
from flask import Flask, render_template, request, redirect, url_for
from cfenv import AppEnv

from sqlalchemy.ext.declarative import declarative_base
# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

env = AppEnv()
app = Flask(env.name)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# create declarative_base instance
Base = declarative_base()

# we create the class Book and extend it from the Base Class.
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))

def getDataseUrl():
    # Grab service in VCAP_SERVICES called database, change the name as appropriate
    database = env.get_service(name='database') 
    raw_url = database.credentials['uri']
    # Remove anything after the question mark
    url = raw_url.split('?')[0]
    return url

# Connect to Database and create database session
engine = create_engine(getDataseUrl())
Base.metadata.bind = engine

# creates a tables
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

# landing page that will display all the books in our database
# This function operate on the Read operation.
@app.route('/')
@app.route('/books')
def showBooks():
    books = session.query(Book).all()
    return render_template("books.html", books=books)


# This will let us Create a new book and save it in our database
@app.route('/books/new/', methods=['GET', 'POST'])
def newBook():
    if request.method == 'POST':
        newBook = Book(title=request.form['name'], author=request.form['author'], genre=request.form['genre'])
        session.add(newBook)
        session.commit()
        return redirect(url_for('showBooks'))
    else:
        return render_template('newBook.html')


# This will let us Update our books and save it in our database
@app.route("/books/<int:book_id>/edit/", methods=['GET', 'POST'])
def editBook(book_id):
    editedBook = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedBook.title = request.form['name']
            return redirect(url_for('showBooks'))
    else:
        return render_template('editBook.html', book=editedBook)


# This will let us Delete our book
@app.route('/books/<int:book_id>/delete/', methods=['GET', 'POST'])
def deleteBook(book_id):
    bookToDelete = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        session.delete(bookToDelete)
        session.commit()
        return redirect(url_for('showBooks', book_id=book_id))
    else:
        return render_template('deleteBook.html', book=bookToDelete)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=env.port)
