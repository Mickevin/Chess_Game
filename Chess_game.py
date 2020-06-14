from PIL import ImageTk, Image
from tkinter import *
from run import *
import webbrowser


class playing():
    def __init__(self):
        self.n= 0
        pass
    
    def play(self,x,y):
        a.append((x,y))
        if len(a)%2 == 0:
            x1 = a[:-3:-1][1][0]
            y1 = a[:-3:-1][1][1]

            x2 = a[:-3:-1][0][0]
            y2 = a[:-3:-1][0][1]
            print(x1,y1,x2,y2)
            if good_mouve_pièce(x1, y1, x2, y2, partie):
                if coups.n%2 == 0 and partie[x1][y1].color == 'W':
                    good_mouve_pièce(x1, y1, x2, y2, partie, T=True)
                    partie[x2][y2] = partie[x1][y1]
                    partie[x1][y1] = vide
                    coups.n +=1
                    deck = deck_chess(partie)
                    jeu(deck)
                    window.update()
                    
                if coups.n%2 != 0 and partie[x1][y1].color == 'B':
                    good_mouve_pièce(x1, y1, x2, y2, partie, T=True)
                    partie[x2][y2] = partie[x1][y1]
                    partie[x1][y1] = vide
                    coups.n +=1
                    deck = deck_chess(partie)
                    jeu(deck)
                    window.update()

def open_web():
    webbrowser.open_new('https://github.com/Mickevin')

def affiche_c(x,y):
    
    def coordonee():
        coups.play(x,y)
    return coordonee


def canvas_g(x,y):
    canvas = Canvas(chess_grid,height = 1, width=1)
    canvas.grid(row=y, column=x)
    
    if x%2 == 0:
        if y%2 == 0: Button(canvas, command=affiche_c(x,y), bg='black', image=space).pack()
        else: Button(canvas, command=affiche_c(x,y), bg='white', image=space).pack()
    
    else:
        if y%2 != 0: Button(canvas, command=affiche_c(x,y), bg='black', image=space).pack()
        else: Button(canvas, command=affiche_c(x,y), bg='white', image=space).pack()
            
            

def position(x,y, piece, grid):
    canvas = Canvas(chess_grid)
    canvas.grid(row=y, column=x)
    
    if x%2 == 0:
        if y%2 == 0: grid[x][y] = Button(canvas, bg='black', command=affiche_c(x,y), image=piece.img)
        else: grid[x][y] = Button(canvas, bg='white', command=affiche_c(x,y), image=piece.img)
    
    else:
        if y%2 != 0: grid[x][y] = Button(canvas, bg='black', command=affiche_c(x,y), image=piece.img)
        else: grid[x][y] = Button(canvas, bg='white', command=affiche_c(x,y), image=piece.img)
    
    grid[x][y].pack()
    return grid[x][y]


# Créer une fenètre
window = Tk()
space = ImageTk.PhotoImage(Image.open("chess/Space.png").resize([70,60]))
fond = ImageTk.PhotoImage(Image.open("chess/Space.png").resize([100,90]))

# Modifier le nom d'une fenètre
window.title("Chess Game")

window.geometry("1000x800")
#
window.minsize(480,360)
#
window.iconbitmap("chess.ico")
#
window.config(background="#7446EB")


a = [(0,0),(0,0)]
coups = playing()
partie = run()
deck = deck_chess(partie)


for i in deck[0]:
    i.img = ImageTk.PhotoImage(i.img)

    
frame = Frame(window,bg = "#7446EB")
frame.pack(expand=True)
Button(frame, text='GitHub', command=open_web).pack()

title_label = Label(frame,text= "Welcome to the Chess Game", font=('Helvetica', 20), bg ="#7446EB", fg = 'white') 
title_label.pack(expand=True)

chess_grid = Frame(window,bg = "#7446EB")


def jeu(deck):
    grid = [[canvas_g(x,y) for x in range(8)] for y in range(8)]
    [position(piece.x,piece.y,piece, grid) for piece in deck[0]]


jeu(deck)
chess_grid.pack(expand=True,ipady=60)
window.mainloop()