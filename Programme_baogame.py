
from tkinter import *
from tkinter import messagebox
import time

fen = Tk()

fen.geometry("820x600")
can = Canvas(fen, width=820, height=500)
can.grid()
can.pack()
can.create_rectangle (10,10,810,410)
can.create_text (150, 450, text = "Player 1 : ", font = 200)
can.create_text (550, 450, text = "Player 2 : ", font = 200)
graines_j1 = can.create_text(150,480, text = "0", font = 150)
graines_j2 = can.create_text(550,480, text = "0", font = 150)

x = 110 
y = 110
while x < 820 : 
    can.create_line (x,10,x,410)
    can.create_line (10,y,810,y)
    x = x + 100
    y = y + 100
can.create_line (10, 210, 810, 210, width = 3)
can.create_line (10, 10, 810, 10, width = 3)
can.create_line (10, 410, 810, 410, width = 3)
can.create_line (810, 10, 810, 410, width = 3)
can.create_line (10, 10, 10, 410, width = 3)
cx = 20
cy = 20
z = 20
while z < 420:
    while cx < 820 : 
        can.create_oval (cx,z,cx + 80,z + 80)
        cx = cx + 100
        cy = cy + 100
    z = z + 100
    cx = 20
    cy = 20
    

jeu =[[".."]*8 for i in range(4)]
print (jeu)
tableau = [[None]*8 for i in range(0,4)]
#print (tableau[0][0])


for j in range (4):
    for i in range (len(jeu[0])):
        valcer = can.create_text(i*100 + 60,j*100 + 55, text = str(jeu[j][i]), font = 150)
        #valcer1 = can.create_oval(i*100 + 30, j*100 + 30, i*100 + 50, j*100 + 50)
        print (j, i)
        tableau[j][i] = valcer
        print (tableau[j][i])


nbr_graine_mangees_j1 = 0
nbr_graine_mangees_j2 = 0
prm_tour = 1
Aquiletour = 2
breakboucle = 2
def adgr(event):
    global tableau, nbr_graine_mangees_j1, nbr_graine_mangees_j2, dern_li, prm_tour, Aquiletour, breakboucle
    def centre_case(ligne, colonne) :
        x = colonne * 100 + 60
        y = ligne * 100 + 60
        return x,y
    clic_x = event.x
    clic_y = event.y 
    
    co = clic_x // 100 
    li = clic_y // 100 
    if breakboucle == 1:
        if dern_li == 3 or dern_li == 2:
            if li == 3 or li == 2:
                messagebox.askokcancel("Mauvais joueur", "Ce n'est pas à vous de jouer.")
                return
            else :
                breakboucle = 2
        if dern_li == 0 or dern_li == 1:
            if li == 0 or li == 1:
                messagebox.askokcancel("Mauvais joueur", "Ce n'est pas à vous de jouer.")
                return
            else :
                breakboucle = 2
    if prm_tour == 2:
        if li == 2 or li == 3:
            messagebox.askokcancel("Mauvais joueur", "Ce n'est pas à vous de jouer.")
            return
        if li == 0:
            messagebox.askokcancel("coup illégal", "Vous ne pouvez pas commencer à jouer sur cette rangée, veuillez choisir un emplacement sur la 3ème rangée.")
            return
        if li == 1:
            prm_tour = 3
            Aquiletour = 1
    if prm_tour == 1: #premier coup du joueur 1
        if li == 0 or li == 1: #si on clique en premier sur les trous du joueur 2
            messagebox.askokcancel("Mauvais joueur", "Ce n'est pas à vous de commencer.")
            return
        if li == 3: #Si on clique sur la ligne du bas (interdit)
            messagebox.askokcancel("coup illégal", "Vous ne pouvez pas commencer à jouer sur cette rangée, veuillez choisir un emplacement sur la 3ème rangée.")
            return
        if li == 2: #si coup légal
            prm_tour = 2
            

    '''if Aquiletour == 2:
        if dern_li == 1 or dern_li == 0:
            if li == 1 or li == 0:
                messagebox.askokcancel("Mauvais joueur", "C'est au joueur 1 de jouer.")
                return
            if li == 2 or li == 3:
                Aquiletour = 3        
    if Aquiletour == 1:
        if dern_li == 3 or dern_li == 2:
            if li == 3 or li == 2:
                messagebox.askokcancel("Mauvais joueur", "C'est au joueur 2 de jouer.")
                return
            if li == 1 or li == 0:
                Aquiletour = 2'''
    
    while True :
        
        dern_li = li
        dern_co = co
        
        
        if len(jeu[li][co]) == 0:
            messagebox.askokcancel("Case vide", "Vous avez cliqué sur une case vide")
            return
                
        if clic_y > 240 and clic_y < 340: #3ème rangée
            
            if len(jeu[li][co]) <= co: #si nmbr de graine plus petit que nmbr de trou suivants
                val = len(jeu[li][co])
                for k in range(1, val+1): # + 1 trous suivants
                
                    jeu[li][co-k] = "."  + jeu[li][co-k]
                    nombre = len(jeu[li][co-k])
                    can.itemconfig(tableau[li][co-k], text = "." * nombre)
                    jeu[li][co] = ""
                    can.itemconfig(tableau[li][co],text = jeu[li][co])
                    x1, y1 = centre_case(li, co)
                    x2, y2 = centre_case(li, co-k)
                    
                    can.create_line(x1, y1, x2, y2, fill="blue")
                    can.update()
                dern_co = co-val
                dern_li = li
                
            
            else: #si besoin de distribuer dans la rangée du dessous
                if co == 0: #juste la ligne du dessous
                    val = len(jeu[li][co])
                    for h in range(0, val):
                        
                        jeu[li+1][h] = jeu[li+1][h] + "."
                        nombre = len(jeu[li+1][h])
                        can.itemconfig(tableau[li+1][h], text="."*nombre)
                        jeu[li][co] = ""
                        can.itemconfig(tableau[li][co],text = jeu[li][co])
                        x1, y1 = centre_case(li, co)
                        x2, y2 = centre_case(li+1, co+h)
                    
                        can.create_line(x1, y1, x2, y2, fill="blue")
                        can.update()
                    dern_li = li + 1
                    
                    dern_co = co + val -1
                    
                    
                
                elif co > 0:
                    #les trous suivants + la ligne du dssous
                    val = len(jeu[li][co])
                    
                    for g in range(1, co+1):
                        
                        jeu[li][co-g] = jeu[li][co-g] + "."
                        nombre = len(jeu[li][co-g]) 
                        can.itemconfig(tableau[li][co - g],text = "."*nombre)
                        x1, y1 = centre_case(li, co)
                        x2, y2 = centre_case(li, co-g)
                        
                        can.create_line(x1, y1, x2, y2, fill="blue")
                        can.update()
                    for h in range(0, val-co):
                        
                        jeu[li+1][h] = jeu[li+1][h] + "." 
                        nombre = len(jeu[li+1][h]) 
                        can.itemconfig(tableau[li+1][h], text = "."*nombre)
                        x1, y1 = centre_case(li, co)
                        x2, y2 = centre_case(li+1,h)
                        
                        can.create_line(x1, y1, x2, y2, fill="blue")
                        can.update()
                    jeu[li][co] = ""
                    can.itemconfig(tableau[li][co],text = jeu[li][co])
                    dern_li = li + 1
                    dern_co = val-co-1
                
            #déplacement_gr(clic_x, clic_y, dern_co, dern_li)        
        
                    
        if clic_y > 340 and clic_y < 440: #4ème rangée
            if len(jeu[li][co]) <= 7-co: #si nmbr de graine plus petit que nmbr de trou --> distribuer que sur rangée
                val = len(jeu[li][co])
                for k in range(1, val+1):
                    
                    jeu[li][co+k] = "."  + jeu[li][co+k] 
                    nombre = len(jeu[li][co+k])
                    can.itemconfig(tableau[li][co + k],text = "."*nombre)
                    jeu[li][co] = ""
                    can.itemconfig(tableau[li][co],text = jeu[li][co])
                    x1, y1 = centre_case(li, co)
                    x2, y2 = centre_case(li, co+k)
                    
                    can.create_line(x1, y1, x2, y2, fill="blue")
                    can.update()
                dern_co = co + val
                
            else:
                val = len(jeu[li][co])
                if co == 7: #distribuer ligne du dessus
                    for h in range(0, val):
                        
                        jeu[li-1][7-h] = jeu[li-1][7-h] + "."
                        nombre = len(jeu[li-1][7-h])
                        can.itemconfig(tableau[li-1][7-h], text="."*nombre)
                        jeu[li][co] = ""
                        can.itemconfig(tableau[li][co],text = jeu[li][co])
                        x1, y1 = centre_case(li, co)
                        x2, y2 = centre_case(li-1, co-h)
                        
                        can.create_line(x1, y1, x2, y2, fill="blue")
                        can.update()
                    dern_li = li - 1
                    dern_co = 7-val+1
                    
                else: #distribuer ligne du dessus + trou qui restent
                    val = len(jeu[li][co])
                    
                    for g in range(1, 7-co+1):
                        
                        jeu[li][co+g] = jeu[li][co+g] + "."
                        nombre = len(jeu[li][co+g])
                        can.itemconfig(tableau[li][co + g],text = "."*nombre)
                        x1, y1 = centre_case(li, co)
                        x2, y2 = centre_case(li, co+g)
                        
                        can.create_line(x1, y1, x2, y2, fill="blue")
                        can.update()
                    for h in range(0, val-(7-co)):
                        
                        jeu[li-1][7-h] = jeu[li-1][7-h] + "."
                        nombre = len(jeu[li-1][7-h])
                        can.itemconfig(tableau[li-1][7-h], text = "."*nombre)
                        x1, y1 = centre_case(li, co)
                        x2, y2 = centre_case(li-1, 7-h)
                        
                        can.create_line(x1, y1, x2, y2, fill="blue")
                        can.update()
                    jeu[li][co] = ""
                    can.itemconfig(tableau[li][co],text = jeu[li][co])
                    dern_li = li - 1
                    dern_co = 7- (val - (7-co) - 1)
                    
                    
        if clic_y > 40 and clic_y < 140: #1ère rangée
            if len(jeu[li][co]) <= co: #si nmbr de graine plus petit que nmbr de trou suivants
                val = len(jeu[li][co])
                for k in range(1, val+1): # + 1 trous suivants
                
                    jeu[li][co-k] = "."  + jeu[li][co-k]
                    nombre = len(jeu[li][co-k])
                    can.itemconfig(tableau[li][co-k], text = "." * nombre)
                    jeu[li][co] = ""
                    can.itemconfig(tableau[li][co],text = jeu[li][co])
                dern_co = co-val
            
            else: #si besoin de distribuer dans la rangée du dessous
                if co == 0: #juste la ligne du dessous
                    val = len(jeu[li][co])
                    for h in range(0, val):
                        
                        jeu[li+1][h] = jeu[li+1][h] + "."
                        nombre = len(jeu[li+1][h])
                        can.itemconfig(tableau[li+1][h], text="."*nombre)
                        jeu[li][co] = ""
                        can.itemconfig(tableau[li][co],text = jeu[li][co])
                    dern_li = li + 1
                    
                    dern_co = co + val -1
                    
                    
                
                elif co > 0:
                    #les trous suivants + la ligne du dssous
                    val = len(jeu[li][co])
                    for g in range(1, co+1):
                        
                        jeu[li][co-g] = jeu[li][co-g] + "."
                        nombre = len(jeu[li][co-g]) 
                        can.itemconfig(tableau[li][co - g],text = "."*nombre)
                    for h in range(0, val-co):
                        
                        jeu[li+1][h] = jeu[li+1][h] + "." 
                        nombre = len(jeu[li+1][h]) 
                        can.itemconfig(tableau[li+1][h], text = "."*nombre)
                        
                    jeu[li][co] = ""
                    can.itemconfig(tableau[li][co],text = jeu[li][co])
                    dern_li = li + 1
                    dern_co = val-co-1
                    
                    
        if clic_y > 140 and clic_y < 240: #2ème rangée
            if len(jeu[li][co]) <= 7-co: #si nmbr de graine plus petit que nmbr de trou --> distribuer que sur rangée
                val = len(jeu[li][co])
                for k in range(1, val+1):
                    
                    jeu[li][co+k] = "."  + jeu[li][co+k] 
                    nombre = len(jeu[li][co+k])
                    can.itemconfig(tableau[li][co + k],text = "."*nombre)
                    jeu[li][co] = ""
                    can.itemconfig(tableau[li][co],text = jeu[li][co])
                dern_co = co + val
                
            else:
                val = len(jeu[li][co])
                if co == 7: #distribuer ligne du dessus
                    for h in range(0, val):
                        
                        jeu[li-1][7-h] = jeu[li-1][7-h] + "."
                        nombre = len(jeu[li-1][7-h])
                        can.itemconfig(tableau[li-1][7-h], text="."*nombre)
                        jeu[li][co] = ""
                        can.itemconfig(tableau[li][co],text = jeu[li][co])
                    dern_li = li - 1
                    dern_co = 7-val+1
                    
                else: #distribuer ligne du dessus + trou qui restent
                    val = len(jeu[li][co])
                    for g in range(1, 7-co+1):
                        
                        jeu[li][co+g] = jeu[li][co+g] + "."
                        nombre = len(jeu[li][co+g])
                        can.itemconfig(tableau[li][co + g],text = "."*nombre)
                    for h in range(0, val-(7-co)):
                        
                        jeu[li-1][7-h] = jeu[li-1][7-h] + "."
                        nombre = len(jeu[li-1][7-h])
                        can.itemconfig(tableau[li-1][7-h], text = "."*nombre)
                        
                    jeu[li][co] = ""
                    can.itemconfig(tableau[li][co],text = jeu[li][co])
                    dern_li = li - 1
                    dern_co = 7- (val - (7-co) - 1)
        
        if len(jeu[dern_li][dern_co]) == 1: #si dernière graine attérit dans une case vide
            if dern_li == 2: #joueur 1 prend les graines de l'adversaire
                
                
                
                total = nbr_graine_mangees_j1 + len(jeu[dern_li-1][dern_co]) #la cagnotte totale devient l'addition des graines capturées et des graines venant d'être capturées
                can.itemconfig(graines_j1, text = str(total))#afficher le total des graines capturés par le joueur 1
                nbr_graine_mangees_j1 = total #le nombre de graines dans la cagnotte devient le nouveau point de départ
                jeu[dern_li-1][dern_co] = ""
                can.itemconfig(tableau[dern_li-1][dern_co],text = jeu[dern_li-1][dern_co])
                if total == 32:
                    messagebox.askokcancel("Fin de la partie", "Le joueur 1 remporte la partie!!")
                    return
                
            elif dern_li == 1: #joueur 2
                total = nbr_graine_mangees_j2 + len(jeu[dern_li+1][dern_co]) #la cagnotte totale devient l'addition des graines capturées et des graines venant d'être capturées
                can.itemconfig(graines_j2, text = str(total))#afficher le total des graines capturés par le joueur 2
                nbr_graine_mangees_j2 = total 
                if total == 32:
                    messagebox.askokcancel("Fin de la partie", "Le joueur 2 remporte la partie!!")
                    return
                
                jeu[dern_li+1][dern_co] = ""
                can.itemconfig(tableau[dern_li+1][dern_co],text = jeu[dern_li+1][dern_co])
            breakboucle = 1
            break
        
            
        if len(jeu[dern_li][dern_co]) > 1:
            li = dern_li
            co = dern_co
            clic_x = co * 100 + 50
            
        if dern_li == 3:
            clic_y = 350
        if dern_li == 2:
            clic_y = 250
        if dern_li == 1:
            clic_y = 150
        if dern_li == 0:
            clic_y = 50
        can.update
        
        
        
                
    
            
            
            
    
        

    
    
    
    
    
can.bind('<Button-1>', adgr)

fen.mainloop()

