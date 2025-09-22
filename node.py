# Implement your Node class here
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None


#Design Memo:
#1. Why is a stack the right choice for undo/redo?
# Stack is the right choice for a undo/redo because it follows
# a last in, last out model which is what an undo/redo function
# follows. The last edit you made is usually the edit you want to
# undo. A queue class follows First in, First out, which makes
# no sense with an undo/redo function, because it will undo the 
# very first edit you made, not the last one that you actually 
# wanted to undo.

#2. Why is a queue better suited for the help desk?
# A queue class is better for a help desk function because
# it follows a first in, first out model which allows a help
# desk to help the first customer submitted into the queue. 
# If we used a stack class then it would help the last customer
# which would make a bunch of customers who been waiting really
# angry. 

#3. How do your implementations differ from Python's built-in lists?
# They differ because they offer a special tool that regular python lists
# can't offer. They store data in a certain order by which they can be utilized.
# Which allows us to use these classes in specific scenarios that will benefit us
# the most in how we store data. 


#Side Note: I used ChatGPT to help me figure out how to push an action from the undo stack
# and pop it from the redo stack. After I figured that out, I was able to do the peek at the
# next customer and return their name in help desk all by myself using what I learned from Chat
# GPT.