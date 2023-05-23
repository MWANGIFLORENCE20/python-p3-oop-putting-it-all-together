#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand=brand
        self.condition = 'New'
        if not isinstance(size,int):
            print("size must be an integer")
        else:
            self.size=size

    def repair(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'
        
shoe=Shoe("Adidas",9)
print(shoe.brand)
print(shoe.size)
shoe.repair()