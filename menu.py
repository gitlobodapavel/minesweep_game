from tkinter import *
import game


def display():

    def easy():
        game.setup(9, 9, 10)

    def medium():
        game.setup(16, 16, 40)

    def hard():
        game.setup(16, 30, 90)

    root = Tk()
    b1 = Button(text='Easy',
                width=15, height=3)
    b1.config(command=easy)
    b1.pack()
    b2 = Button(text='Medium',
                width=15, height=3)
    b2.config(command=medium)
    b2.pack()

    b1 = Button(text='Hard',
                width=15, height=3)
    b1.config(command=hard)
    b1.pack()

    root.mainloop()