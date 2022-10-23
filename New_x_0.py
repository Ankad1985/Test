from tkinter import *
import random
root = Tk()
root.title('Х - 0')
game_run = True               #запретить делать ходы когда уже выявлен победитель
field = []
cross_count = 0               #количество крестиков на поле


def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            bot_move()
            check_win('O')

#Проверка победы
def check_win(x_or_0):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], x_or_0)
        check_line(field[0][n], field[1][n], field[2][n], x_or_0)
    check_line(field[0][0], field[1][1], field[2][2], x_or_0)
    check_line(field[2][0], field[1][1], field[0][2], x_or_0)

def check_line(a1,a2,a3,x_or_0):
    if a1['text'] == x_or_0 and a2['text'] == x_or_0 and a3['text'] == x_or_0:
        a1['background'] = a2['background'] = a3['background'] = 'green'
        global game_run
        game_run = False

#Игра бота
def can_win(a1,a2,a3,x_or_0):
    res = False
    if a1['text'] == x_or_0 and a2['text'] == x_or_0 and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == x_or_0 and a2['text'] == ' ' and a3['text'] == x_or_0:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == x_or_0 and a3['text'] == x_or_0:
        a1['text'] = 'O'
        res = True
    return res

def bot_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

#Графический интерфейс                
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Ariel', 20, 'bold'),
                        background='white',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
root.mainloop()    
