# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 17:09:27 2019

Project: Library management system

@author: TOL1HC
"""

# import os
# import sys


class Book:
    count = 0
    isbn_list = []

    def __init__(self, isbn, title, subject=None, author=None, publisher=None, date=None, pages=None, copies=1):
        Book.count += 1
        self.isbn = isbn
        Book.isbn_list.append(isbn)
        self.title = title
        self.subject = subject
        self.author = author
        self.publisher = publisher
        self.date = date
        self.pages = pages
        self.copies = copies

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_title(self, title):
        self.title = title

    def set_subject(self, subject):
        self.subject = subject

    def set_author(self, author):
        self.author = author

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_date(self, date):
        self.date = date

    def set_pages(self, pages):
        self.pages = pages

    def set_copies(self, copies):
        self.copies = copies

    @property
    def show_bookinfo(self):
        print("-------------------------------------------------------------")
        print("Title: " + self.title)
        print("Authors: " + self.author)
        print("Published by: " + self.publisher + " - Published date: " + self.date)
        print("Pages: " + str(self.pages))
        print("Number of copies: " + str(self.copies))
        print("-------------------------------------------------------------")
        return 1

    def __repr__(self):
        return 'Book({}, {}, {}, {}, {}, {}, {})'.format(self.isbn, self.title, self.author, self.publisher, self.date, self.pages, self.copies)

    def __str__(self):
        return '{} - {} - {} - {} copies'.format(self.isbn, self.title, self.author, self.copies)

    def access_Book(self):
        pass

    def __delete__(self):
        print("Book " + self.title + "(" + self.isbn + ") was deleted from database")

