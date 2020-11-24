from tkinter import *
import game
import results as statistic
import time


def display():

    def easy():
        game.level = 'Easy'
        game.start_time = time.time()
        game.setup(3, 4, 1)

    def medium():
        game.level = 'Medium'
        game.start_time = time.time()
        game.setup(16, 16, 40)

    def hard():
        game.level = 'Hard'
        game.start_time = time.time()
        game.setup(16, 30, 90)

    def results():
        root.destroy()
        statistic.show()

    root = Tk()
    b1 = Button(text='Easy',
                width=15, height=3)
    b1.config(command=easy)
    b1.pack()
    b2 = Button(text='Medium',
                width=15, height=3)
    b2.config(command=medium)
    b2.pack()

    b3 = Button(text='Hard',
                width=15, height=3)
    b3.config(command=hard)
    b3.pack()

    b4 = Button(text='Results',
                width=15, height=3)
    b4.config(command=results)
    b4.pack()

    root.mainloop()