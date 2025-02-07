# Доколин Георгий ИУ7-22Б
# Подключение функций и библиотек
from tkinter import *
from tkinter import ttk
from logic import add_circle, clear, clean_txt_file
from math import sqrt


# Функция, которая создает новое окно с информацией
def new_window(text_tittle, text):
    window = Tk()
    window.title(text_tittle)
    window.geometry("500x300")
    label = ttk.Label(window, text=text)
    label.pack(anchor=CENTER, expand=1)


# Функция, которая отвечает за создание окружностей при помощи мыши
def create_circle_mouse(event, canvas):
    x, y = event.x, event.y
    with open("circles_mouse.txt", "a+") as file:
        file.write(str(x) + ' ' + str(y) + '\n')
        file.seek(0)
        arr = list(file)
        if len(arr) >= 3:
            arr_1, arr_2, arr_3 = list(map(int, arr[0].split())), list(map(int, arr[1].split())), list(map(int, arr[2].split()))
            add_circle(arr_1, arr_2, arr_3, canvas)
            file.truncate(0)


# Функция, которая отвечает за отрисовку всех элементов управления
def view(canvas, root):
    menu = Menu(root)
    root.config(menu=menu)
    description = Menu(menu, tearoff=0)
    description.add_command(label="О разработчике", command=lambda: new_window('О разработчике',
                                                                               'Доколин Георгий ИУ7-22Б'))
    description.add_command(label="О программе", command=lambda: new_window('О программе',
                                                                            'Программа для отрисовки окружностей '
                                                                            'и точек \nс опрделением окружности с '
                                                                            'минимальной разностью \nколичества '
                                                                            'внутренних и внешних точек'))
    menu.add_cascade(label="Описание", menu=description)

    # label_circle_pos_x = ttk.Label()
    # label_circle_pos_x['text'] = 'Circle position X: '
    # circle_position_x = ttk.Entry()
    # label_circle_pos_y = ttk.Label()
    # label_circle_pos_y['text'] = 'Circle position Y: '
    # circle_position_y = ttk.Entry()
    # label_circle_radius = ttk.Label()
    # label_circle_radius['text'] = 'Circle position: '
    # circle_radius = ttk.Entry()
    # label_dot_pos_x = ttk.Label()
    # label_dot_pos_x['text'] = 'Dot position X: '
    # btn_circle = ttk.Button(text="Click", command=lambda: add_circle(circle_position_x.get(), circle_position_y.get(),
    #                                                                  circle_radius.get(), canvas))
    # label_dot_pos_y = ttk.Label()
    # label_dot_pos_y['text'] = 'Dot position X: '
    # dot_position_x = ttk.Entry()
    # dot_position_y = ttk.Entry()
    # label_dot_pos_y = ttk.Label()
    # label_dot_pos_y['text'] = 'Dot position Y: '
    # btn_dot = ttk.Button(text="Click", command=lambda: add_dot(dot_position_x.get(), dot_position_y.get(), canvas))
    # btn_clear = ttk.Button(text="Clear", command=lambda: clear(canvas))
    # label_circle_pos_x.grid(row=1, column=0)
    # circle_position_x.grid(row=2, column=0)
    # label_circle_pos_y.grid(row=3, column=0)
    # circle_position_y.grid(row=4, column=0)
    # label_circle_radius.grid(row=5, column=0)
    # circle_radius.grid(row=6, column=0)
    # btn_circle.grid(row=7, column=0)
    # label_dot_pos_x.grid(row=2, column=1)
    # dot_position_x.grid(row=3, column=1)
    # label_dot_pos_y.grid(row=4, column=1)
    # dot_position_y.grid(row=5, column=1)
    # btn_dot.grid(row=6, column=1)
    # btn_clear.grid(row=2, column=2, rowspan=2, columnspan=2)
    canvas.pack()
    canvas.bind("<Button-1>", lambda event: create_circle_mouse(event, canvas))


# Функция, которая запускает все приложение
def main():
    clean_txt_file('circles.txt')
    clean_txt_file('circles_mouse.txt')
    root = Tk()
    canvas = Canvas(width=1200, height=700, bg='white')
    view(canvas, root)
    root.mainloop()


if __name__ == '__main__':
    main()
