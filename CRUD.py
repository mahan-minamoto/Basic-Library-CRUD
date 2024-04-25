class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, book):
        self.books.remove(book)
    def add_member(self, member):
        self.members.append(member)
    def remove_member(self, member):
        self.members.remove(member)
    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
    def display_members(self):
        for member in self.members:
            print(f"Name: {member.name}, Member ID: {member.member_id}")
library = Library()
book1 = Book("Python Crash Course", "Eric Matthes", "9781593279288")
book2 = Book("Clean Code", "Robert C. Martin", "9780132350884")
library.add_book(book1)
library.add_book(book2)
member1 = Member("John Doe", "12345")
member2 = Member("Jane Smith", "67890")
library.add_member(member1)
library.add_member(member2)
library.display_books()
library.display_members()