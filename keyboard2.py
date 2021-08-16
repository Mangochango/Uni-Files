from tkinter import *
from tkinter.ttk import *
import random

def append(ch, target, char_index, block_index, targets):

    #text_string.set(text_string.get() + ch)

    if target == ch:
        char_index += 1
        target = targets[char_index]
        text_string.set(target)
        return target

        if char_index > 5:
            char_index = 0
            block_index += 1
            targets = random.shuffle(targets)
            if block_index > 5:
                text_string.set("Completed Challenge")
        return char_index, block_index, targets


def clear1():
    text_string.set("")


board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

targets = "abcdef"


n = 6
char_index = 0
block_index = 0

target = targets[char_index]

print(target)
window = Tk()
window.title('Test')

frame_top = Frame(window)
frame_top.pack(fill="x", side=TOP)

text_string = StringVar()
text_string.initialize(target)
text = Label(frame_top, text="Test", justify=CENTER, textvariable=text_string)


#clear = Button(frame_top, text="Clear", command=lambda: clear1())
#clear.pack(side="right", fill="x", padx=8, pady=4)

text.pack(padx=8, pady=4)


frame_keys = Frame(window, relief=RAISED, borderwidth=2)
frame_keys.pack(fill="both", padx=10, pady=10)

keys1 = Frame(frame_keys)
keys1.pack()

keys2 = Frame(frame_keys)
keys2.pack()

keys3 = Frame(frame_keys)
keys3.pack()

rows = [keys1, keys2, keys3]
row_num = 0
for row in board:
    for ch in row:
        key_frame = Frame(rows[row_num], height=32, width=32)
        key_frame.pack_propagate(0)
        key_frame.pack(side="left")
        b = Button(key_frame, text=ch, command=lambda x=ch: append(x, target, char_index, block_index, targets))
        b.pack(side="left", padx=1, pady=1)
    row_num += 1
b.pack()

window.mainloop()

