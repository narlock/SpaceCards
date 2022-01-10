# Card class
# Author: Anthony Narlock

class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def toString(self):
        print(self.front + " " + self.back)