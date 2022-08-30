# A text editor which only writes how to write a linked list
from tkinter import Tk, Text, Scrollbar

def counter(func):
    def helper(*args, **kwargs):
        res = func(*args, **kwargs)
        helper.i = (helper.i + 1) % len(sentence)
        return res
    helper.i = 0
    return helper

@counter
def force(*args):
    text_widget.delete('end-2c')
    text_widget.insert('end', sentence[force.i])

sentence = """# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

"""

root = Tk()
root.geometry("600x400")
root.title("reverse_linked_list.py")

sb = Scrollbar(root, orient='vertical')
sb.pack(side="right", fill='y')

text_widget = Text(root, yscrollcommand=sb.set)
text_widget.pack(expand=True)

root.bind("<Key>", force)
root.mainloop()

# Future work
# - fix bug: backspace and delete don't work properly
# - find alternative method to block insertion of characters