# Доколин Георгий ИУ7-22Б
# Подключение библиотек
from tkinter import messagebox as mb
from math import sqrt


# Функция отрисовки элементов на холст
def paint_all(canvas, arr_1, arr_2, arr_3):
    canvas.delete('all')
    with open('circles.txt', 'r') as file:
        for i in file:
            arr = list(map(float, i.split()))
            print(arr)
            s_1 = str(arr[0]) + ' ' + str(arr[1]) + ' ' + str(arr[2]) + ' ' + str(arr[3]) + ' ' + str(arr[4]) + ' ' + str(arr[5])
            s_2 = str(arr_1[0]) + ' ' + str(arr_1[1]) + ' ' + str(arr_2[0]) + ' ' + str(arr_2[1]) + ' ' + str(arr_3[0]) + ' ' + str(arr_3[1])
            if s_1 != s_2:
                canvas.create_polygon([arr[0], arr[1]], [arr[2], arr[3]], [arr[4], arr[5]], fill="yellow", outline="yellow")
            else:
                canvas.create_polygon([arr_1[0], arr_1[1]], [arr_2[0], arr_2[1]], [arr_3[0], arr_3[1]], fill="red", outline="red")


# Функция для чтения данных из файла в массив
def read_to_arr(name):
    with open(name, 'r') as file:
        arr = []
        len_arr_circles = len(list(file))
        file.seek(0)
        for i in range(len_arr_circles):
            arr.append(list(map(float, file.readline().split())))
        return arr


# Функция проверки окружности на условие минимальной разности
def check_triangle(canvas):
    arr_circles = read_to_arr('circles.txt')
    mini = float('inf')
    arr_1 = [arr_circles[0][0], arr_circles[0][1]]
    arr_2 = [arr_circles[0][2], arr_circles[0][3]]
    arr_3 = [arr_circles[0][4], arr_circles[0][5]]
    for i in arr_circles:
        len_1 = sqrt((i[0] - i[2]) ** 2 + (i[1] - i[3]) ** 2)
        len_2 = sqrt((i[0] - i[4]) ** 2 + (i[1] - i[5]) ** 2)
        len_3 = sqrt((i[2] - i[4]) ** 2 + (i[3] - i[5]) ** 2)
        p = (len_1 + len_2 + len_3) / 2
        s = sqrt(p * (p - len_1) * (p - len_2) * (p - len_3))
        if s < mini:
            mini = s
            arr_1 = [i[0], i[1]]
            arr_2 = [i[2], i[3]]
            arr_3 = [i[4], i[5]]
    paint_all(canvas, arr_1, arr_2, arr_3)


# Функция добавления окружности
def add_circle(arr_1, arr_2, arr_3, canvas):
    try:
        with open("circles.txt", "a+") as file:
            print(arr_1, arr_2, arr_3)
            print(str(arr_1[0]) + ' ' + str(arr_1[1]) + ' ' + str(arr_2[0]) + ' ' + str(arr_2[1]) + str(arr_3[0]) + ' ' + str(arr_3[1]) + '\n')
            file.write(str(arr_1[0]) + ' ' + str(arr_1[1]) + ' ' + str(arr_2[0]) + ' ' + str(arr_2[1]) + ' ' + str(arr_3[0]) + ' ' + str(arr_3[1]) + '\n')
    except ValueError:
        mb.showerror("Ошибка", "Должно быть введено число большее 0")
    check_triangle(canvas)


# Функция очистки текстовых файлов
def clean_txt_file(name):
    with open(name, 'a') as file:
        file.truncate(0)
        file.close()


# Функция очистки всего
def clear(canvas):
    clean_txt_file('circles.txt')
    clean_txt_file('dots.txt')
    clean_txt_file('circles_mouse.txt')
    canvas.delete('all')
