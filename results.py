from tkinter import *
import menu
import sqlite3_connect_db
import game


def show():

    def display_menu():
        root.destroy()
        menu.display()

    def print_stat():
        sqlite3_connect_db.cursor.execute("SELECT * FROM results WHERE user = ? ", (game.username,))
        rows = sqlite3_connect_db.cursor.fetchall()
        for row in rows:
            l1 = Label(text=str('user: ' + str(row[0]) + ', level: ' + str(row[1] + ', time: ' + row[2] + ' sec')),
                       font="Arial 16")
            l1.pack()

    root = Tk()
    b3 = Button(text='MENU',
                width=15, height=3)
    b3.config(command=display_menu)
    b3.pack()
    print_stat()
    root.mainloop()


if __name__ == '__main__':
    pass
else:
    pass