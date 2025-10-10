
from tkinter import *
from tkinter import messagebox
import time
import tkinter.font as tkFont

fen = Tk()
font50 = tkFont.Font(family="Times", size=50)
fen.geometry("820x600")
can = Canvas(fen, width=820, height=500)
can.grid()
can.pack()
can.create_rectangle (10,10,810,410)
#affiche les compteurs de graines des joueurs 1 et 2, dans leur couleur correspondante
p1= can.create_text (150, 450, text = "Player 1, compteur de graines : ",fill ="red", font = ("Times", 15) )
p2 = can.create_text (650, 450, text = "Player 2, compteur de graines : ",fill = "blue", font= ("Times", 15) )
graines_j1 = can.create_text(150,480, text = "0", font = 150)
graines_j2 = can.create_text(650,480, text = "0", font = 150)

x = 110 
y = 110
#dessine les lignes et colonnes du jeu
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
#dessine les trous de chaque case
while z < 420:
    while cx < 820 : 
        can.create_oval (cx,z,cx + 80,z + 80)
        cx = cx + 100
        cy = cy + 100
    z = z + 100
    cx = 20
    cy = 20
    

jeu =[[".."]*8 for i in range(4)] #détermination de la valeur des cases de la matrice de "..", soit deux graines
print (jeu)
tableau = [[None]*8 for i in range(0,4)] # transfère des valeurs dans une matrice vide, étant enregistrées
#la matrice "jeu" contient donc deux graines par case, 4 rangées et 8 trous par rangée, pouvant être modifié

#dessine et rajoute une couleur bleu pour les graines se situant dans les 2 lignes du haut (joueur 2)
for j in range (0,2): 
    for i in range (len(jeu[0])):
        valcer = can.create_text(i*100 + 60,j*100 + 55, text = str(jeu[j][i]),fill="blue" ,font = ("Times", 25)) #affichage des graines visuellement
        tableau[j][i] = valcer
#dessine et rajoute une couleur rouge pour les graines se situant dans les 2 lignes du bas (joueur 1)
for j in range (2,4): 
    for i in range (len(jeu[0])):
        valcer = can.create_text(i*100 + 60,j*100 + 55, text = str(jeu[j][i]),fill="red" ,font = ("Times", 25)) #affichage des graines visuellement
        #(servait à comprendre quand ça ne marchait pas)
        '''print (j, i)        
        print (j, i)
        tableau[j][i] = valcer
        print (tableau[j][i])'''
#indique le joueur qui doit commencer
messagebox.askokcancel(" ","Joueur 1, c'est à vous de commencer")

nbr_graine_mangees_j1 = 0
nbr_graine_mangees_j2 = 0
prm_tour = 1
Aquiletour = 2
breakboucle = 2
def adgr(event):
    global tableau, nbr_graine_mangees_j1, nbr_graine_mangees_j2, dern_li, prm_tour, Aquiletour, breakboucle
    global dx,dy, Deplacegraine
    
    
    def centre_case(ligne, colonne) :
        x = colonne * 100 + 60 #cordonnées x = la colonne corespondante * 100 + 60
        y = ligne * 100 + 60 #pareil por y
        return x,y
    clic_x = event.x #cordonnées de x = cordonnées x du clic
    clic_y = event.y #idem pour y
    
    co = clic_x // 100 #numéro de colonne correspondant à x
    li = clic_y // 100 #idem pour y
    #vérifie que c'est au bon joueur de jouer 
    if breakboucle == 1: 
        if dern_li == 3 or dern_li == 2:
            if li == 3 or li == 2:#si c'est au joueur 1 mais que le joueur 2 joue
                messagebox.askokcancel("Mauvais joueur", "Ce n'est pas à vous de jouer.")
                return
            else :
                breakboucle = 2 #si c'est au joueur 1 et que le joueur 1 joue --> sort de la boucle
        if dern_li == 0 or dern_li == 1: #idem pour le joueur 2
            if li == 0 or li == 1:
                messagebox.askokcancel("Mauvais joueur", "Ce n'est pas à vous de jouer.")
                return
            else :
                
                breakboucle = 2
    if prm_tour == 2: #premier coup joueur 2 --> idem que pour le joueur 1 (voir prm_tour = 1)
        can.itemconfig(p2, font = ("Times", 15))
        can.itemconfig(p1, font = ("Times", 15, "bold"))
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
        can.itemconfig(p2, font = ("Times", 15))
        can.itemconfig(p1, font = ("Times", 15, "bold"))
        if li == 0 or li == 1: #si on clique en premier sur les trous du joueur 2
            messagebox.askokcancel("Mauvais joueur", "Ce n'est pas à vous de commencer.")
            return
        if li == 3: #Si on clique sur la ligne du bas (interdit)
            messagebox.askokcancel("coup illégal", "Vous ne pouvez pas commencer à jouer sur cette rangée, veuillez choisir un emplacement sur la 3ème rangée.")
            return
        if li == 2: #si coup légal
            prm_tour = 2
            


    
    x = event.x
    y = event.y
    
    while True :
    
        
        
        '''print ("coords :", can.coords(valcer))
        #can.coords(valcer, x, y)'''
        fen.update()
        #attend 1.5 secondes entre chaque déplacement
        time.sleep(1.5)
        #Les cordonnées du dernier trou deviennent les cordonnées du premier trou pour chaque tour
        dern_li = li
        dern_co = co
        
        #Si on clique sur une case vide (pour éviter confusion)
        if len(jeu[li][co]) == 0:
            messagebox.askokcancel("Case vide", "Vous avez cliqué sur une case vide")
            return
                
        if clic_y > 240 and clic_y < 340: #3ème rangée
            
            
            if len(jeu[li][co]) <= co: #si nmbr de graine plus petit que nmbr de trou suivants
                val = len(jeu[li][co])
                
                
                
                
                for k in range(1, val+1): # + 1 aux trous suivants
                
                    jeu[li][co-k] = "."  + jeu[li][co-k] #affiche visuellement l'ajout
                    nombre = len(jeu[li][co-k])#nombre de  graines dans une case (nombre)
                    can.itemconfig(tableau[li][co-k], text = "." * nombre) #enlève les "." du trou et remplace dans la matrice par "." (texte)*nombre (nombre)-->autant de graines que de nombre
                    jeu[li][co] = "" #vide le trou de départ
                    can.itemconfig(tableau[li][co],text = jeu[li][co]) #remplace dans la matrice la valeur de départ par " " (vide)
                    x1, y1 = centre_case(li, co)#détermination du centre des cases 
                    x2, y2 = centre_case(li, co-k)
                    
                    
                    can.update()
                #détermination de la valeur du dernier trou    
                dern_co = co-val
                dern_li = li
                
            
            else: #si besoin de distribuer dans la rangée du dessous
                if co == 0: #ajoute + 1 dans les trous de juste la ligne du dessous
                    val = len(jeu[li][co])
                    for h in range(0, val): #même principe
                        
                        jeu[li+1][h] = jeu[li+1][h] + "."
                        nombre = len(jeu[li+1][h])
                        can.itemconfig(tableau[li+1][h], text="."*nombre)
                        jeu[li][co] = ""
                        can.itemconfig(tableau[li][co],text = jeu[li][co])
                        x1, y1 = centre_case(li, co)
                        x2, y2 = centre_case(li+1, co+h)
                    
                        
                        can.update()
                    dern_li = li + 1
                    
                    dern_co = co + val -1
                    
                    
                
                elif co > 0: #si on doit distribuer les graines sur la même ligne et la ligne du dessous
                    #les trous suivants + la ligne du dessous
                    val = len(jeu[li][co])
                    
                    for g in range(1, co+1): #correspond à la même ligne (même principe)
                        
                        jeu[li][co-g] = jeu[li][co-g] + "."
                        nombre = len(jeu[li][co-g]) 
                        can.itemconfig(tableau[li][co - g],text = "."*nombre)
                        x1, y1 = centre_case(li, co)
                        x2, y2 = centre_case(li, co-g)
                        
                        
                        can.update()
                    for h in range(0, val-co):
                        #correspond à la ligne du dessous (même principe, avec les graines qui restent)
                        jeu[li+1][h] = jeu[li+1][h] + "." 
                        nombre = len(jeu[li+1][h]) 
                        can.itemconfig(tableau[li+1][h], text = "."*nombre)
                        x1, y1 = centre_case(li, co)
                        x2, y2 = centre_case(li+1,h)
                        
                        
                        can.update()
                    #vide le trou de départ dans tous les cas
                    jeu[li][co] = ""
                    can.itemconfig(tableau[li][co],text = jeu[li][co])
                    dern_li = li + 1
                    dern_co = val-co-1
                
                    
        
                    
        if clic_y > 340 and clic_y < 440: #4ème rangée (même principe que pour la 3ème rangée)
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
                        
                        
                        can.update()
                    dern_li = li - 1
                    dern_co = 7-val+1
                    
                else: #distribuer ligne + ligne du dessus
                    val = len(jeu[li][co])
                    
                    for g in range(1, 7-co+1):
                        
                        jeu[li][co+g] = jeu[li][co+g] + "."
                        nombre = len(jeu[li][co+g])
                        can.itemconfig(tableau[li][co + g],text = "."*nombre)
                        x1, y1 = centre_case(li, co)
                        x2, y2 = centre_case(li, co+g)
                        
                        
                        
                        can.update()
                    for h in range(0, val-(7-co)):
                        
                        jeu[li-1][7-h] = jeu[li-1][7-h] + "."
                        nombre = len(jeu[li-1][7-h])
                        can.itemconfig(tableau[li-1][7-h], text = "."*nombre)
                        x1, y1 = centre_case(li, co)
                        x2, y2 = centre_case(li-1, 7-h)
                        
                        
                        can.update()
                    jeu[li][co] = ""
                    can.itemconfig(tableau[li][co],text = jeu[li][co])
                    dern_li = li - 1
                    dern_co = 7- (val - (7-co) - 1)
                    
                    
        if clic_y > 40 and clic_y < 140: #1ère rangée (même principe que pour joueur 1)
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
            if dern_li == 2: #si la case vide se situe sur la rangée du haut (joueur 1)
                
                
                
                total = nbr_graine_mangees_j1 + len(jeu[dern_li-1][dern_co]) #la cagnotte totale devient l'addition des graines capturées et des graines venant d'être capturées
                can.itemconfig(graines_j1, text = str(total))#afficher le total des graines capturés par le joueur 1
                nbr_graine_mangees_j1 = total #le nombre de graines dans la cagnotte devient le nouveau point de départ
                
                time.sleep(0.9)
                jeu[dern_li-1][dern_co] = ""#vider la case ou les graines ont été prises
                
                can.itemconfig(tableau[dern_li-1][dern_co],text = str(jeu[dern_li-1][dern_co]))#remplacer la case ou les graines ont été prises par " " (vide)
                if total == 32: #si joueur 1 a capturé toutes les graines
                    messagebox.askokcancel("Fin de la partie", "Le joueur 1 remporte la partie!!")
                    return
                
            elif dern_li == 1: #joueur 2 (même principe que pour joueur 1)
                total = nbr_graine_mangees_j2 + len(jeu[dern_li+1][dern_co]) #la cagnotte totale devient l'addition des graines capturées et des graines venant d'être capturées
                can.itemconfig(graines_j2, text = str(total))#afficher le total des graines capturés par le joueur 2
                nbr_graine_mangees_j2 = total 
                if total == 32:
                    messagebox.askokcancel("Fin de la partie", "Le joueur 2 remporte la partie!!")
                    return
                time.sleep(0.9)
                jeu[dern_li+1][dern_co] = ""
                can.itemconfig(tableau[dern_li+1][dern_co],text = jeu[dern_li+1][dern_co])
            breakboucle = 1
            break
        
        #détermine les valeurs des nouvelles cordonnées en fonction des dernières cases
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

