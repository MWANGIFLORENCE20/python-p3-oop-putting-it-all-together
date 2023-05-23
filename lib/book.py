#!/usr/bin/env python3

 

class Book:

    def __init__(self,title,page_count):
        self.title=title

        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else:
            self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
book=Book("And Then There Were None",272)
print(book.title) 
print(book.page_count)
book.turn_page()     
    
    
        