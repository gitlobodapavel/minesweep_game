from tkinter import *
from tkinter import messagebox
import random


def grid(c, grid_height, grid_width, square_size):
    for i in range(grid_width):
        for j in range(grid_height):
            c.create_rectangle(i * square_size, j * square_size,
                               i * square_size + square_size,
                               j * square_size + square_size, fill='gray')


def setup(grid_height, grid_width, mines_num, square_size=50):
    root = Tk()  # Основное окно программы
    root.title("Minesweep")
    c = Canvas(root, width=grid_width * square_size,
               height=grid_height * square_size)  # Задаем область на которой будем рисовать
    c.pack()

    GRID_SIZE = grid_height

    def check_mines(neighbors):
        return len(mines.intersection(neighbors))

    def generate_neighbors(square):
        """ Возвращает клетки соседствующие с square """
        # Левая верхняя клетка
        if square == 1:
            data = {grid_height + 1, 2, grid_height + 2}
            print('left top')
        # Правая нижняя
        elif square == (grid_height * grid_width):
            data = {square - GRID_SIZE, square - 1, square - GRID_SIZE - 1}
            print('right bottom')
        # Левая нижняя
        elif square == grid_height:
            data = {grid_height - 1, grid_height * 2, grid_height * 2 - 1}
            print('left bottom')
        # Верхняя правая
        elif square == (grid_height * grid_width) - grid_height + 1:
            data = {square + 1, square - grid_height, square - grid_height + 1}
            print('right top')
        # Клетка в левом ряду
        elif square < grid_height:
            data = {square + 1, square - 1, square + GRID_SIZE,
                    square + GRID_SIZE - 1, square + GRID_SIZE + 1}
            print('left row')
        # Клетка в правом ряду
        elif square > (grid_height * grid_width) - grid_height:
            data = {square + 1, square - 1, square - GRID_SIZE,
                    square - GRID_SIZE - 1, square - GRID_SIZE + 1}
            print('right row')
        # Клетка в нижнем ряду
        elif square % grid_height == 0:
            data = {square + GRID_SIZE, square - GRID_SIZE, square - 1,
                    square + GRID_SIZE - 1, square - GRID_SIZE - 1}
            print('bottom row')
        # Клетка в верхнем ряду
        elif square % grid_height == 1:
            data = {square + GRID_SIZE, square - GRID_SIZE, square + 1,
                    square + GRID_SIZE + 1, square - GRID_SIZE + 1}
            print('top row')
        # Любая другая клетка
        else:
            data = {square - 1, square + 1, square - GRID_SIZE, square + GRID_SIZE,
                    square - GRID_SIZE - 1, square - GRID_SIZE + 1,
                    square + GRID_SIZE + 1, square + GRID_SIZE - 1}
            print('another')
        return data

    def print_neighbors(ids):
        neighbors = generate_neighbors(ids)
        around = check_mines(neighbors)
        if around:
            # мины есть, рисуем
            x1, y1, x2, y2 = c.coords(ids)
            c.create_text(x1 + square_size / 2,
                          y1 + square_size / 2,
                          text=str(around), font="Arial {}".format(int(square_size / 2)), fill='yellow')
        else:
            pass
            # print('MINES: ' + str(check_mines(neighbors)))

    # events
    def click(event):
        ids = c.find_withtag(CURRENT)[0]  # Определяем по какой клетке кликнули
        if ids not in mines:
            print_neighbors(ids)
        if ids in mines:
            c.itemconfig(CURRENT, fill="red")  # Если кликнули по клетке с миной - красим ее в красный цвет
            messagebox.showwarning(title='Oops!', message='Game Over !')
            root.destroy()
            return 0

        elif ids not in clicked:
            c.itemconfig(CURRENT, fill="green")  # Иначе красим в зеленый
        c.update()

    def mark_grid(event):
        ids = c.find_withtag(CURRENT)[0]
        # Если мы не кликали по клетке - красим ее в желтый цвет, иначе - в серый
        if ids not in clicked:
            clicked.add(ids)
            x1, y1, x2, y2 = c.coords(ids)
            c.itemconfig(CURRENT, fill='yellow')
        else:
            clicked.remove(ids)
            c.itemconfig(CURRENT, fill="gray")

    # Функция для обозначения мин
    def mark_mine(event):
        ids = c.find_withtag(CURRENT)[0]
        # Если мы не кликали по клетке - красим ее в желтый цвет, иначе - в серый
        if ids not in clicked:
            clicked.add(ids)
            x1, y1, x2, y2 = c.coords(ids)
            c.itemconfig(CURRENT, fill="orange")
        else:
            clicked.remove(ids)
            c.itemconfig(CURRENT, fill="gray")

    c.bind("<Button-1>", click)
    c.bind("<Button-3>", mark_mine)
    c.bind("<MouseWheel>", mark_grid)

    grid(c, grid_height, grid_width, square_size)

    mines = set(random.sample(range(1, grid_height*grid_width + 1), mines_num))  # Генерируем мины в случайных позициях
    clicked = set()  # Создаем сет для клеточек, по которым мы кликнули

    root.mainloop()


if __name__ == '__main__':
    pass
else:
    pass