import random
import os
import json
import pandas as pd
import numpy as np
from IPython.display import display
from datetime import *
import pickle

print('Start')
pd.options.mode.chained_assignment = None 

class Piece():
        def __init__(self, name, color, pic,force=0, val = 0):
            self.name = name
            self.color = color
            self.force = force
            self.pic = pic
            self.x = True
            self.y = True
            self.n = 0
            self.val = val
            self.safe = True
        
        def __repr__(self):
            return self.pic
        
        def pos(self):
            return self.x,self.y

vide = Piece('vide','0',' __ ',0)

def choose_b(piece):
    selection = ["N", "Q", "R", "B"]
    c = input('Choose your Piece "N", "Q", "R", "B"   : ') 
    while c not in selection:
        print("Error !!")
        c = input('Choose your Piece "N", "Q", "R", "B"   : ')
    
    if c == "N":
        piece  = Piece('N','B','♞',3)
    elif c == "Q":
        piece = Piece('Q','B','♛',5)
    elif c == "B":
        piece = Piece('B','B','♝',3)  
    elif c == "R":
        piece = Piece('R','B','♜',3)
    return piece

def choose_w(piece):
    selection = ["N", "Q", "R", "B"]
    c = input('Choose your Piece "N", "Q", "R", "B"   : ') 
    while c not in selection:
        print("Error !!")
        c = input('Choose your Piece "N", "Q", "R", "B"   : ')
    
    if c == "N":
        piece  = Piece('N','W','♘',3)
    elif c == "Q":
        piece =  Piece('Q','W','♕',5)
    elif c == "B":
        piece = Piece('B','W','♗',3) 
    elif c == "R":
        piece = Piece('R','W','♖',3)
    return piece


def transforme(piece,c):
    if piece.color == 'B':
        if c == "N":
            piece.name = 'N'
            piece.pic  = '♞'
        elif c == "Q":
            piece.name = 'Q'
            piece.pic = '♛'
        elif c == "B":
            piece.name = 'B'
            piece.pic = '♝'  
        elif c == "R":
            piece.name = 'R'
            piece.pic = '♜'
        return piece
    else:
        if c == "N":
            piece.name = 'N'
            piece.pic  = '♘'
        elif c == "Q":
            piece.name = 'Q'
            piece.pic = '♕'
        elif c == "B":
            piece.name = 'B'
            piece.pic = '♗'  
        elif c == "R":
            piece.name = 'R'
            piece.pic = '♖'
        return piece


def run():
    #Création des pièche blanches
    Nw1, Nw2 = Piece('N','W','♘',3,9), Piece('N','W','♘',3,10)
    Rw1, Rw2 = Piece('R','W','♖',3,11), Piece('R','W','♖',3,12)
    Bw1, Bw2 = Piece('B','W','♗',3,13), Piece('B','W','♗',3,14)     
    Qw, Kw =  Piece('Q','W','♕',5,15),Piece('K','W','♔',4,16)
    
    Pw1, Pw2, Pw3, Pw4 = Piece('P','W','♙',1 ,1),Piece('P','W','♙',1,2),Piece('P','W','♙',1,3),Piece('P','W','♙',1,4)
    Pw5, Pw6, Pw7, Pw8 = Piece('P','W','♙',1,5),Piece('P','W','♙',1,6),Piece('P','W','♙',1,7),Piece('P','W','♙',1,8)
    
    
    #Création des pièce noires
    Nb1, Nb2 = Piece('N','B','♞',3,25), Piece('N','B','♞',3,26)
    Rb1, Rb2 = Piece('R','B','♜',3,27), Piece('R','B','♜',3,28)
    Bb1, Bb2 = Piece('B','B','♝',3,29), Piece('B','B','♝',3,30)   
    Qb, Kb =  Piece('Q','B','♛',5,31),Piece('K','B','♚',4,32)

    Pb1, Pb2, Pb3, Pb4 = Piece('P','B','♟',1,17), Piece('P','B','♟',1,18), Piece('P','B','♟',1,19), Piece('P','B','♟',1,20)
    Pb5, Pb6, Pb7, Pb8 = Piece('P','B','♟',1,21), Piece('P','B','♟',1,22), Piece('P','B','♟',1,23), Piece('P','B','♟',1,24)  
    
    lw = [Pw1, Pw2, Pw3, Pw4, Pw5, Pw6, Pw7, Pw8]
    lb = [Pb1, Pb2, Pb3, Pb4, Pb5, Pb6, Pb7, Pb8]
    
    #Création de la table
    Tableau = [[ Piece('vide','0','   __ ',0) for i in range(8)] for u in range(8)]
    
    
    #Posiotionnement des pions blanc et noir
    for i in range(8): Tableau[1][i], Tableau[-2][i]= lb[i],lw[i]


    #Posiotionnement des autres pièces blanc et noir
    Tableau[0][0],Tableau[0][-1],Tableau[-1][0],Tableau[-1][-1] = Rb1, Rb2, Rw1, Rw2 #Tours
    Tableau[0][1],Tableau[0][-2],Tableau[-1][1],Tableau[-1][-2] = Nb1, Nb2, Nw1, Nw2 #Cavaliers
    Tableau[0][2],Tableau[0][-3],Tableau[-1][2],Tableau[-1][-3] = Bb1, Bb2, Bw1, Bw2 #Fous
    Tableau[0][3],Tableau[0][-4],Tableau[-1][3],Tableau[-1][-4] = Qb, Kb, Qw, Kw #Roi et Damme

    #Fonction qui affiche la partie
    P = pd.DataFrame(Tableau)
    for i in P:
        for u in range(len(P[i])):
            P[i][u].x = i
            P[i][u].y = u
    return P

def affiche(partie):
    partie.columns = ['A','B','C','D','E','F','G','H']
    partie.index += 1 
    display(partie)
    partie.columns = [0,1,2,3,4,5,6,7]
    partie.index += -1
    return partie

def convert_input(player): #Convertie l'entrée en int
    n = 0
    if player == 'A' or player == '1':
        n = 0
    elif player == 'B' or player == '2':
        n = 1
    elif player == 'C' or player == '3':
        n = 2
    elif player == 'D' or player == '4':
        n = 3
    elif player == 'E' or player == '5':
        n = 4
    elif player == 'F' or player == '6':
        n = 5
    elif player == 'G' or player == '7':
        n = 6
    elif player == 'H' or player == '8':
        n = 7
    return n

def entree(): #Vérification de l'entrée, str en sortie
    lettres = "ABCDEFGH"
    Nombres = "12345678"
    in_player = input('A vous de jouer !>>  Position Destination (ex:B1 A3) : ')
    while (len(in_player) != 5 or in_player[2]!= ' ' or in_player[1] not in Nombres or in_player[-1] not in Nombres 
           or in_player[0] not in lettres or in_player[-2] not in lettres):
        if in_player == 'exit':
            print('exit')
            return True
        in_player = input('Erreur de saisie ! A vous de jouer ! >> Position Destination (ex:B1 A3) : ')
    return in_player


def convert_commande():#Vérification globale de l'entrée et convertion en int pout utilisation dans le tableau
    P = entree()
    if P == True:
        return 0,0,0,0
    a,b,c,d =convert_input(P[0]), convert_input(P[1]), convert_input(P[3]), convert_input(P[4])
    return a,b,c,d

def correct_mouve(n, partie):#Vérification de la validité du mouvement
    if n == 0:
        print('\nLes Blancs jouent')
        a,b,c,d = convert_commande()
        if a == b == c == d == 0:
            return 0,0,0,0,0
        if good_mouve_pièce(a,b,c,d, partie) == True and partie[a][b].color == 'W':
            n = n + 1
            return a,b,c,d,n
        else:
            print(good_mouve_pièce(a,b,c,d, partie) == True, partie[a][b].color == 'W')
            print((partie[a][b].name == 'B' or partie[a][b].name == 'Q') 
                  and (partie[c][d].color != partie[a][b].color or partie[c][d].name == vide.name))
            while good_mouve_pièce(a,b,c,d, partie) != True or partie[a][b].color != 'W':
                print('\nErreur ! Les Blancs jouent')
                a,b,c,d = convert_commande()
                if a == b == c == d == 0:
                    return 0,0,0,0,0
            n = n + 1
            return a,b,c,d,n
    elif n != 0:
        print('\nLes noirs jouent')
        a,b,c,d = convert_commande()
        if a == b == c == d == 0:
            return 0,0,0,0,0
        if good_mouve_pièce(a,b,c,d, partie) == True and partie[a][b].color == 'B':
            n = n - 1
            return a,b,c,d,n
        else:
            while good_mouve_pièce(a,b,c,d,partie) != True or partie[a][b].color != 'B':
                affiche(partie)
                print('\nErreur ! Les noir jouent')
                a,b,c,d = convert_commande()
                if a == b == c == d == 0:
                    return 0,0,0,0,0
            n = n - 1
            return a,b,c,d,n
    else : return a,b,c,d,n

def good_mouve_pièce(x1,y1,x2,y2,partie):
    vide = Piece('vide','0',' __ ',0)
    #Pions Blancs
    if partie[x1][y1].color == 'W' and partie[x1][y1].name == 'P':
        if x1 == x2 and  partie[x2][y2].name == vide.name and y1 == y2 + 1: 
            #if y2 == 0 :
             #   partie[x1][y1] = choose_w(partie[x1][y1])
            return True
        elif x1 == x2 and y1 == 6 and y2 == 4 and partie[x2][y2].name == vide.name and partie[x1][5].name == vide.name: 
            #if y2 == 0 :
            #    partie[x1][y1] = choose_w(partie[x1][y1])
            return True 
        elif y2 == y1 - 1 and (x2 == x1 + 1 or x2 == x1 - 1) and partie[x2][y2].color == 'B': 
            return True
                #if y2 == 0 :
                 #   partie[x1][y1] = choose_w(partie[x1][y1])
        try :
            if partie[x2][y2+1].name == 'P' and  partie[x2][y2].name == vide.name and partie[x2][y2+1].color == 'B' and y2 == y1 - 1:
                partie[x2][y2+1] = vide
                return True
        except KeyError:
            return False 

        
    #Pions Noirs
    elif partie[x1][y1].color == 'B' and partie[x1][y1].name == 'P' :
        if x1 == x2 and  partie[x2][y2].name == vide.name and y1 == y2 - 1: 
            return True
            #if y2 == 7:
             #partie[x1][y1] = choose_b(partie[x1][y1])
        elif x1 == x2 and y1 == 1 and y2 == 3 and partie[x2][y2].name == vide.name and partie[x1][2].name == vide.name: 
           # if y2 == 7:
            #    partie[x1][y1] = choose_b(partie[x1][y1])
            return True 
        elif y2 == y1 + 1 and (x2 == x1 + 1 or x2 == x1 - 1):
            if partie[x2][y2].color == 'W': 
                #if y2 == 7:
                 #   partie[x1][y1] = choose_b(partie[x1][y1])
                return True
        try :
            if partie[x1][y2-1].name == 'P' and  partie[x2][y2].name == vide.name and partie[x1][y2-1].color == 'W' and y2 == y1 +1:
                partie[x1][y2-1] = vide
                return True
        except KeyError:
            return False
    

    
    #Tours Blancs
    elif partie[x1][y1].name == 'R' and (partie[x1][y1].color != partie[x2][y2].color or partie[x2][y2].name == vide.name):
        if x1 == x2:
            if y2 < y1:
                i = y1 - 1
                while i > y2:
                    if partie[x1][i].name != vide.name: return False
                    i = i-1
                return True
            if y2 > y1:
                i = y1 + 1
                while i < y2:
                    if partie[x1][i].name != vide.name: return False
                    i = i+1
                return True
        elif y1 == y2:
            if x2 < x1:
                i = x1 - 1
                while i > x2:
                    if partie[i][y1].name != vide.name: return False
                    i = i-1
                return True
            if x2 > x1:
                i = x1 + 1
                while i < x2:
                    if partie[i][y1].name != vide.name: return False
                    i = i+1
                return True
    
    
    #Queen Rock
    elif partie[x1][y1].name == 'Q' and (partie[x1][y1].color != partie[x2][y2].color 
                                         or partie[x2][y2].name == vide.name):
        if x1 == x2:
            if y2 < y1:
                i = y1 - 1
                while i > y2:
                    if partie[x1][i].name != vide.name: return False
                    i = i-1
                return True
            if y2 > y1:
                i = y1 + 1
                while i < y2:
                    if partie[x1][i].name != vide.name: return False
                    i = i+1
                return True
        elif y1 == y2:
            if x2 < x1:
                i = x1 - 1
                while i > x2:
                    if partie[i][y1].name != vide.name: return False
                    i = i-1
                return True
            if x2 > x1:
                i = x1 + 1
                while i < x2:
                    if partie[i][y1].name != vide.name: return False
                    i = i+1
                return True
        
        #Queen Fou
        elif x1 != x2:
            if (y2 - y1)/(x2 - x1) == 1:
                if x1 < x2:
                    i,j = x1 +1,y1+1
                    while i < x2 :
                        if partie[i][j].name != vide.name: 
                            return False
                        i,j = i+1,j+1
                    return True
                if x1 > x2:
                    i,j = x1 - 1,y1 - 1
                    while i > x2 :
                        if partie[i][j].name != vide.name:
                            return False
                        i,j = i-1,j-1
                    return True

            
            elif (y2 - y1)/(x2 - x1) == -1:
                if x1 < x2:
                    i,j = x1 +1,y1-1
                    while i < x2 :
                        if partie[i][j].name != vide.name: return False
                        i,j = i+1,j-1
                    return True
                if x1 > x2:
                    i,j = x1 - 1,y1 + 1
                    while i > x2 :
                        if partie[i][j].name != vide.name: return False
                        i,j = i-1,j+1
                    return True
        
    
    #Roi
    elif partie[x1][y1].name == 'K' and (partie[x2][y2].color != partie[x1][y1].color 
                                         or partie[x2][y2].name == vide.name):
        if x1 == x2 + 1 or x1 == x2 - 1:
            if y1 == y2 or y1 == y2 - 1 or y1 == y2 + 1: return True
            else : return False
        elif x1 == x2:
            if y1 == y2 - 1 or y1 == y2 + 1: return True
        
        
        #Rock Black
        elif partie[x1][y1].color == "B":
            if x2 == 6 and y2 == 0 and partie[7][0].name == 'R': #small Rock
                if  partie[5][0].name == partie[6][0].name == vide.name:
                    partie[5][0] = partie[7][0]
                    partie[7][0] = vide
                    return True
            if x2 == 2 and y2 == 0 and partie[0][0].name == 'R': #big Rock
                if partie[3][0].name == partie[2][0].name == partie[1][0].name == vide.name:
                    partie[3][0] = partie[0][0]
                    partie[0][0] = vide
                    return True
        
        #Rock White        
        elif partie[x1][y1].color == "W":
            if x2 == 6 and y2 == 7 and partie[7][7].name == 'R': #small Rock
                if partie[5][7].name == partie[6][7].name == vide.name:
                    partie[5][7] = partie[7][7]
                    partie[7][7] = vide
                    return True
            
            if x2 == 2 and y2 == 7 and partie[0][0].name == 'R': #big Rock
                if partie[3][7].name == partie[2][7].name == partie[1][7].name == vide.name:
                    partie[3][7] = partie[0][7]
                    partie[0][7] = vide
                    return True
    
    #Cavalier
    elif partie[x1][y1].name == 'N' and (partie[x2][y2].color != partie[x1][y1].color 
                                         or partie[x2][y2].name == vide.name):
        if x1 == x2 - 1 or x1 == x2 + 1:
            if y1 == y2 - 2 or y1 == y2 + 2: 
                return True
        elif y1 == y2 - 1 or y1 == y2 + 1:
            if x1 == x2 - 2 or x1 == x2 + 2: 
                return True
    
    
    #Fou 
    elif partie[x1][y1].name == 'B' and x1 != x2 and(partie[x2][y2].color != partie[x1][y1].color or partie[x2][y2].name == vide.name):
        if (y2 - y1)/(x2 - x1) == 1:
            if x1 < x2:
                i,j = x1 +1,y1+1
                while i < x2 :
                    if partie[i][j].name != vide.name: 
                        return False
                    i,j = i+1,j+1
                return True
            elif x1 > x2:
                i,j = x1 - 1,y1 - 1
                while i > x2 :
                    if partie[i][j].name != vide.name:
                        return False
                    i,j = i-1,j-1
                return True

        elif (y2 - y1)/(x2 - x1) == -1:
            if x1 < x2:
                i,j = x1 +1,y1-1
                while i < x2 :
                    if partie[i][j].name != vide.name: return False
                    i,j = i+1,j-1
                return True
            elif x1 > x2:
                i,j = x1 - 1,y1 + 1
                while i > x2 :
                    if partie[i][j].name != vide.name: return False
                    i,j = i-1,j+1
                return True
    return False


def mouve(player): #Qelles est le mouvement joué ?
    selection = ["N", "Q", "R", "B", "K"]
    lettres = "ABCDEFGH"
    Nombres = "12345678"
    x = y = 0
    if 'x' in player:
        x = convert_input(player.split('x')[1][0])
        y = convert_input(player.split('x')[1][1])
    
    elif player[0] in selection:
            x = convert_input(player[1].upper())
            y = convert_input(player[2].upper())
    elif player[0] in lettres.lower():
        x = convert_input(player[0].upper())
        y = convert_input(player[1].upper())
    return x,y

def deck_chess(partie):
    deck = []
    deck_w = []
    deck_b = []
    b = w = 0
    for i in range(8):
        for u in range(8):
                if partie[i][u].color != '0':
                    partie[i][u].safe = True
                    deck.append(partie[i][u])
                    partie[i][u].x = int(i)
                    partie[i][u].y = int(u)
                    if partie[i][u].color == 'B':
                        b += 1
                        deck_b.append(partie[i][u])
                    elif partie[i][u].color == 'W':
                        w += 1
                        deck_w.append(partie[i][u])
    return deck, w, b, deck_w, deck_b

def where(player, deck,n, partie, T=True): #Quelle pièce est jouée ?
    selection = ["N", "Q", "R", "B", "K"]
    lettres = "ABCDEFGH"
    Nombres = "12345678"
    
    if n % 2 == 0:
        C = "B"
    else: C = 'W'
        
    if '#' in player:
        return 9,9,9,9


############################################    #Recherche des pions#   ###############################################
   
    if len(player) == 2:
        for i in deck:
            if i.name == 'P' and i.color == C and good_mouve_pièce(i.x, i.y,mouve(player)[0],mouve(player)[1],partie) == True:
                if T != True:
                    i = transforme(i,T)
                    return i.x, i.y,mouve(player)[0],mouve(player)[1]
                else: 
                    return i.x, i.y,mouve(player)[0],mouve(player)[1]
    elif player[0] in lettres.lower() and '=' not in player:
        if len(player) == 3 and '+' in player:
            p = player.split('+')[0]
            return where(p, deck,n, partie, T=True)

        elif 'x' in player:
            v = convert_input(player.split('x')[0].upper())
            p = player.split('x')[1][:2]
            for i in deck:
                if (i.name == 'P' and i.x == v and good_mouve_pièce(i.x, i.y,mouve(p)[0],mouve(p)[1],partie) == True 
                    and i.color == C):
                    if T != True:
                        i = transforme(i,T)
                    return i.x, i.y,mouve(p)[0],mouve(p)[1]

                
############################################    #Recherche des des autres pièces#   ###################################
    
    elif player[0] in selection and '=' not in player:
        for i in deck:
            if player[0] == i.name and i.color == C:
                o = player.split('x')
                if 'x' in player and o[0][-1] not in lettres.lower():                        
                    p = player.split('x')[1][:2] 
                    if good_mouve_pièce(i.x, i.y,mouve(p)[0],mouve(p)[1],partie) == True and i.color == C:
                        return i.x, i.y,mouve(p)[0],mouve(p)[1]
                elif o[0][-1] in lettres.lower() and i.x == convert_input(o[0][-1].upper()):
                    p = player.split('x')[1][:2] 
                    if  good_mouve_pièce(i.x, i.y,mouve(p)[0],mouve(p)[1],partie) == True and i.color == C:
                        return i.x, i.y,mouve(p)[0],mouve(p)[1]
                elif 'x' not in player:
                    p = player.split(player[0])[1][:2]
                    if p[1] in lettres.lower() and p[0] in lettres.lower():
                        p = player.split(player[0])[1][1:3]
                        o = player.split(player[0])[1][0]
                        if (i.color == C and good_mouve_pièce(i.x, i.y, mouve(p)[0],mouve(p)[1],partie) == True 
                            and i.x == convert_input(o.upper())):
                            return i.x, i.y,mouve(p)[0],mouve(p)[1]

                    elif i.color == C and good_mouve_pièce(i.x, i.y,mouve(p)[0],mouve(p)[1], partie) == True:
                        return i.x, i.y,mouve(p)[0],mouve(p)[1]

                    

############################################         #Rock#        ####################################################
    
    elif player == "O-O":
        for i in deck:
            if i.name == 'K' and i.color == C and i.color == 'B':
                if good_mouve_pièce(i.x,i.y,6,0,partie) == True and i.color == C:
                    return i.x, i.y, 6, 0 
            elif i.name == 'K' and i.color == C and i.color == 'W':
                if good_mouve_pièce(i.x,i.y,6,7,partie) == True and i.color == C:
                    return i.x, i.y, 6, 7
    
    elif player == 'O-O-O':
        for i in deck:
            if i.name == 'K' and i.color == 'B' and i.color == C:
                if good_mouve_pièce(i.x,i.y,2,0,partie) == True and i.color == C:
                    return 4,0,2,0   
            elif i.name == 'K' and i.color == 'W' and i.color == C:
                if good_mouve_pièce(i.x,i.y,2,7,partie) == True and i.color == C:
                    return 4,7,2,7
                
############################################         #RPion transformation#        ####################################
                
    
    elif "=" in player:
        p = player.split('=')
        return where(p[0], deck,n,partie, T=p[1][0])
    
    else : return 0,0,0,0
    return 0,0,0,0


def predict(partie,a,b,c,d,list_mouve,df_f,n):
     
    partie_predict = partie.copy()
    
    partie_predict[c][d] = partie_predict[a][b]
    partie_predict[c][d].x = c
    partie_predict[c][d].y = d
    partie_predict[a][b] = vide
    
    deck_p = deck_chess(partie_predict)
    df_f.loc[n,'p_Nb_w'] = deck_p[1]
    df_f.loc[n,'p_Nb_b'] = deck_p[2]
    
    warning_w = warning_b = area_w = area_b = 0
    kill = 0
    liberté = 0
    
    for piece in deck_p[0]:
        for u in list_mouve:            
            if good_mouve_pièce(piece.x, piece.y, u[0], u[1], partie_predict):
                if piece.val == partie_predict[c][d].val: # Zone de liberté future
                    liberté += 1
                    
                    if partie_predict[u[0]][u[1]].name != vide.name: # Nombre de kill future possible
                        kill += 1        
                    
                if u[0] == c and u[1]  == d and piece.x != c : # La case est-elle sure ? 0:Oui 1:Non
                    df_f.loc[n,'p_warning_position'] = 1
                    
                
                if piece.color == 'W': # Zone des pièces Blanches
                    area_w += 1
                    
                    if partie_predict[u[0]][u[1]].name != vide.name: # Nombre de pièces Noires en danger
                        warning_b += 1
                        
            
                if piece.color == 'B': # Zone des Pièces Noires
                    area_b += 1              
                    
                    if partie_predict[u[0]][u[1]].name != vide.name: # Nombre de pièces Blanches en danger
                        warning_w += 1
  

                if partie_predict[u[0]][u[1]].name == 'K' and piece.color == partie_predict[c][d].color: #Echech au Roi
                    df_f.loc[n,'p_Chess_bad'] = 1
           
        
                if partie_predict[u[0]][u[1]].name == 'K' and piece.color != partie_predict[c][d].color: #Echec au roi adverse
                    df_f.loc[n,'p_Chess_good'] = 1
 

    df_f.loc[n,'p_Step'] = liberté #Ok
    df_f.loc[n,'p_Will_Kill'] = kill
    
    
    for p in deck_p[0]: # Quelles sont les pièce sur le terrain
        df_f.loc[n,f"p{p.val}"] = p.x*10 +p.y

    df_f.loc[n,'p_Area_w'] = area_w
    df_f.loc[n,'p_Area_b'] = area_b
    df_f.loc[n,'p_Warning_w'] = warning_w
    df_f.loc[n,'p_Warning_b'] = warning_b  
    
    partie_predict[c][d].x = a
    partie_predict[c][d].y = b
    
    
def features(partie, deck,list_mouve,a,b,c,d,n_coup):
    

    partie_test = partie.copy()
    chess_features = np.array(['val', # Id de la pièce #OK
                               'n',   # Nombre de coup depuis le dévut de la partie #OK
                               'coup',# I mage de la pièce #OK
                               'Coordonées', # Coordonnées initiales de la pièce #OK
                               'Destination', # Coordonées de destination #OK
                               'Step',    # Zode de liberté de la pièce #OK
                               'Will_Kill', # Le coups élimine une pièce 1:Oui, 0: NON #OK
                               'Safe_position', # Les coordonée actuelle sont-ils surs ? 0:oui, 1:NON #OK
          '1',"2","3",'4',"5","6","7","8","9","10","11","12","13","14","15","16", #Position des pièces noire
          "17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32", #Position des pièce blanche
                               'Chess_bad', # Le roi est-il en echec ? 1: oui; 0:Non #OK
                               'Chess_good', # Le roi adverse est-il en echec ? 1: oui; 0:Non #OK
                               'Warning_w', # Nombre de pièce blance menacée  #OK
                               'Warning_b', # Nombre de pièce noire menacée  #OK
                               'Area_w', # Nombre de coups jouable Blanc #OK
                               'Area_b', # Nombre de coups jouable noir #OK
                               'Nb_w', # Nombre pièce noire #OK
                               'Nb_b', # Nombre blanche noire #OK
                               'Color', # Couleur de la pièce 0: Blanc, 1:Noir #OK
                               'Play_target', # Le coup jouable est-il joué ? #OK 
                               
                               'p_Step', # Zode de liberté prédite de la pièce #OK
                               'p_Will_Kill', # Le coups prédit pourra-t-il éliminé une pièce 1:Oui, 0: NON #OK
                               'p_warning_position', # La case est-elle sure ? 0:Oui 1:Non #OK
                               'p_Chess_bad', 
                               'p_Chess_good', 
          'p1',"p2","p3",'p4',"p5","p6","p7","p8","p9","p10","p11","p12","p13","p14","p15","p16",
          "p17","p18","p19","p20","p21","p22","p23","p24","p25","p26","p27","p28","p29","p30","p31","p32",
                               'p_Warning_w', # Nombre de pièces Noires en danger #OK
                               'p_Warning_b', # Nombre de pièces Blanches en danger #OK
                               'p_Area_w', # Zone future des pièces Blanches #OK
                               'p_Area_b',# Zone future des pièces Noires #OK
                               'p_Nb_w', # Nombre futur pièce blanches #OK
                               'p_Nb_b' # Nombre future des pièces noires #OK
         ])
       
    n = 0
    df_f = pd.DataFrame(columns=chess_features)


    for piece in deck[0]:        
        for u in list_mouve:         
            # Vérification des coups possibls
            if good_mouve_pièce(piece.x, piece.y,u[0],u[1], partie_test):
                df_f.loc[n,'val'] = piece.val
                
                df_f.loc[n,'coup'] = n_coup # Coup depuis le début de la partie
                
                df_f.loc[n,'n'] = piece #Pièce jouable
                
                df_f.loc[n,'Nb_w'] = deck[1]  #Nombre de pièce blanche
                
                df_f.loc[n,'Nb_b'] = deck[2]  #Nombre de pièce noire
                
                df_f.loc[n,'Coordonées'] = piece.x*10 +piece.y # Coordonnée de la pièce
                
                df_f.loc[n,'Destination'] = u[0]*10 + u[1] # Coordoné de destination de la pièce
                                                  
                if piece.color == 'B':
                    df_f.loc[n,'Color'] = 1                  
                
                if piece.x == a and piece.y == b and u[0] == c and u[1] == d: # Le mouvement est-il celui joué ?
                    df_f.loc[n,'Play_target'] = 1
                    
                if piece.color == 'W':                    # Quelle est la couleur de la pièce joué
                    df_f.loc[n,'Color'] = 0   
                    
                if partie[u[0]][u[1]].name != vide.name:  # Est-ce un mouvement kill ?
                    df_f.loc[n,'Will_Kill'] = 1
                    partie[u[0]][u[1]].safe = False
                    
                    if partie[u[0]][u[1]].name == 'K' and partie[u[0]][u[1]].color != piece.color :# Est-ce le roi ?
                        df_f.loc[n,'Chess_good'] = 1
                    
                    if partie[u[0]][u[1]].name == 'K' and partie[u[0]][u[1]].color == piece.color :# Est-ce le roi ?
                        df_f.loc[n,'Chess_bad'] = 1                
                
                if n_coup % 2 == 0 and piece.color == 'B':
                    predict(partie_test,piece.x, piece.y,u[0],u[1],list_mouve,df_f,n)
                
                elif n_coup % 2 != 0 and piece.color == 'W':
                    predict(partie_test,piece.x, piece.y,u[0],u[1],list_mouve,df_f,n)
                
                n +=1
   

    df_f = df_f.fillna(0)
    
    for p in deck[0]: # Quelles sont les pièce sur le terrain et leur coordonées
        df_f[f"{p.val}"] = p.x*10 +p.y
        df_f.loc[:,'Step'][df_f.val == p.val] =  len(df_f[df_f['val'] == p.val]) #Nombre de coup jouable par la pièce
        if p.safe == False:
            df_f.loc[:,'Safe_position'][df_f.val == p.val] = 1 # Les pièce sont-elle en sécurité sur leur case ?
            
    df_f['Area_w'] = len(df_f[df_f.Color == 0])
    df_f['Area_b'] = len(df_f[df_f.Color == 1])
    df_f['Warning_w'] = df_f[df_f.Color == 0]['Safe_position'].sum()
    df_f['Warning_b'] = df_f[df_f.Color == 1]['Safe_position'].sum()
    
    
    if n_coup % 2 == 0: # Sauvegarde du dataframe sur les pieces noires
        df_f = df_f[df_f.Color == 1]
                
    elif n_coup % 2 != 0 and piece.color == 'W': # Sauvegarde du dataframe sur les pieces blanches
        df_f = df_f[df_f.Color == 0]
 

    return df_f


vide = Piece('vide','0',' __ ',0)

list_mouve = []
for i in range(8):
    for u in range(8):
        list_mouve.append((u,i))

def main(l):   
    partie = run()
    n = 0
    chess_features = np.array(['val','n','coup','Coordonées','Destination','Step','Will_Kill','Safe_position',
          '1',"2","3",'4',"5","6","7","8","9","10","11","12","13","14","15","16",
          "17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32",
         'Chess_bad', 'Chess_good', 'Warning_w','Warning_b','Area_w','Area_b','Nb_w','Nb_b',
          'Color','Play_target',
            'p_Step','p_Will_Kill','p_warning_position','p_Chess_bad', 'p_Chess_good', 
          'p1',"p2","p3",'p4',"p5","p6","p7","p8","p9","p10","p11","p12","p13","p14","p15","p16",
          "p17","p18","p19","p20","p21","p22","p23","p24","p25","p26","p27","p28","p29","p30","p31","p32",
         'p_Warning_w','p_Warning_b','p_Area_w','p_Area_b','p_Nb_w','p_Nb_b'
         ])
    df_mouve = pd.DataFrame(columns=chess_features) 
    
    for i in l:
        if n <= len(l):
            deck = deck_chess(partie)
            a,b,c,d = where(i, deck[0],n,partie)
            if n%2 == 0:
                dff = features(partie,deck,list_mouve,a,b,c,d,n)
                #print(a,b,c,d), print(n, len(deck))      
                df_mouve = pd.concat([df_mouve,dff],axis=0)

        if a == b == c == d == 9:
            return df_mouve.reset_index()
        
        
        """display(df_mouve[df_mouve['coup']== n][['val','n','coup','Coordonées','Destination','Step','Will_Kill','Safe_position',
             'Warning_w','Warning_b','Area_w','Area_b',
            'p_Step','p_Will_Kill','p_warning_position', 
             'p_Warning_w','p_Warning_b','p_Area_w','p_Area_b','Play_target',]])"""
        #affiche(partie)
        n += 1
        
        if a == b == c == d == 0:
            print('error')
            return df_mouve.reset_index()
               
        good_mouve_pièce(a, b, c, d, partie)
        partie[c][d]=partie[a][b]
        partie[c][d].x = c
        partie[c][d].y = d
        partie[a][b] = vide
    return df_mouve.reset_index()


with open("chess_data", 'rb') as f:
    data = pickle.load(f)

m = list(data[0])[:1000]
t0 = datetime.now()
n = 0
d = main(m[90])
for i in range(1,len(m)):
    print(datetime.now()-t0)
    d = pd.concat([d,main(m[i])],axis=0)
    n += 1
    d.to_csv('data_save1.1.csv', index=False)
    print(n)
