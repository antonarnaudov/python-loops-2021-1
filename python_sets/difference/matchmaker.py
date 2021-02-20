import random
import time
from tkinter import Tk, Button, DISABLED


def show_symbol(x, y):
    global is_first
    global previousX
    global previousY

    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update_idletasks()

    if is_first:
        previousX = x
        previousY = y
        is_first = False

    elif previousX != x or previousY != y:
        if buttons[previousX, previousY]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[previousX, previousY]['text'] = ''
            buttons[x, y]['text'] = ''
        else:
            buttons[previousX, previousY]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED

        is_first = True


root = Tk()
root.title('Matchmaker')
root.resizable(width=False, height=False)

buttons = {}
is_first = True
previousX = 0
previousY = 0

button_symbols = {}
symbols = [
    u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708',
    u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u280B', u'\u280B',
    u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',
    u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728'
]

random.shuffle(symbols)

for col in range(6):
    for row in range(4):
        button = Button(command=lambda x=col, y=row: show_symbol(x, y), width=3, height=3)
        button.grid(column=col, row=row)
        buttons[col, row] = button
        button_symbols[col, row] = symbols.pop()

root.mainloop()
