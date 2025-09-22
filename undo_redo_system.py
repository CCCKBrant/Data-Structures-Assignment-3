# Import the Node class you created in node.py
from node import Node
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None
# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value
    
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None
        
    def print_stack(self):
        current = self.top
        if not current:
            print("Stack is empty")
        while current:
            print(f"- {current.value}")
            current = current.next

def run_undo_redo():
    my_undo_stack = Stack()
    my_redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            my_undo_stack.push(action)
            my_redo_stack = Stack()
            

            print(f"Action performed: {action}")
        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            action = my_undo_stack.pop()
            if action:
                my_redo_stack.push(action)
                print(f"Undid: {action}")
            else:
                print("Nothing to undo.")
            
            

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            action = my_redo_stack.pop()
            if action:
                my_undo_stack.push(action)
                print(f"Redid: {action}")
            else:
                print("Nothing to redo.")
            


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            my_undo_stack.print_stack()
            
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            my_redo_stack.print_stack()
            
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()