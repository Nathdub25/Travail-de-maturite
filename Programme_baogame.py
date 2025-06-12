
from tkinter import *
import time

fen = Tk()

fen.geometry("820x600")
can = Canvas(fen, width=820, height=420)
can.grid()
can.create_rectangle (10,10,810,410)
x = 110 
y = 110
while x < 820 : 
    can.create_line (x,10,x,410)
    can.create_line (10,y,810,y)
    x = x + 100
    y = y + 100
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
    

jeu =[[2]*8 for i in range(4)]
print (jeu)
tableau = [[None]*8 for i in range(0,4)]
#print (tableau[0][0])


for j in range (4):
    for i in range (len(jeu[0])):
        valcer = can.create_text(i*100 + 40,j*100 + 40, text = str(jeu[j][i]))
        print (j, i)
        tableau[j][i] = valcer
        print (tableau[j][i])

def adgr(event):
    global tableau
    clic_x = event.x
    clic_y = event.y 
    
    co = clic_x // 100 
    li = clic_y // 100 

    while True :
        
        dern_li = li
        dern_co = co
        if clic_y > 240 and clic_y < 340: #3ème rangée
            if jeu[li][co] <= co: #si nmbr de graine plus petit que nmbr de trou suivants
                val = jeu[li][co]
                for k in range(1, val+1): # + 1 trous suivants
                
                    jeu[li][co-k] = 1  + jeu[li][co-k] 
                    can.itemconfig(tableau[li][co - k],text = str(jeu[li][co - k]))
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                dern_co = co-val
            
            else: #si besoin de distribuer dans la rangée du dessous
                if co == 0: #juste la ligne du dessous
                    val = jeu[li][co]
                    for h in range(0, val):
                        jeu[li+1][h] = jeu[li+1][h] + 1
                        can.itemconfig(tableau[li+1][h], text=str(jeu[li+1][h]))
                        jeu[li][co] = 0
                        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    dern_li = li + 1
                    print (co,val)
                    dern_co = co + val -1
                    print (dern_co)
                    
                
                elif co > 0:
                    #les trous suivants + la ligne du dssous
                    val = jeu[li][co]
                    for g in range(1, co+1):
                        jeu[li][co-g] = jeu[li][co-g] + 1
                        can.itemconfig(tableau[li][co - g],text = str(jeu[li][co - g]))
                    for h in range(0, val-co):
                        
                        jeu[li+1][h] = jeu[li+1][h] + 1
                        can.itemconfig(tableau[li+1][h], text = str(jeu[li+1][h]))
                        
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    dern_li = li + 1
                    dern_co = val-co-1
                
                    
        
                    
        if clic_y > 340 and clic_y < 440: #4ème rangée
            if jeu[li][co] <= 7-co: #si nmbr de graine plus petit que nmbr de trou --> distribuer que sur rangée
                val = jeu[li][co]
                for k in range(1, val+1):
                    jeu[li][co+k] = 1  + jeu[li][co+k] 
                    can.itemconfig(tableau[li][co + k],text = str(jeu[li][co + k]))
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                dern_co = co + val
                print (co, val)
            else:
                val = jeu[li][co]
                if co == 7: #distribuer ligne du dessus
                    for h in range(0, val):
                        jeu[li-1][7-h] = jeu[li-1][7-h] + 1
                        can.itemconfig(tableau[li-1][7-h], text=str(jeu[li-1][7-h]))
                        jeu[li][co] = 0
                        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    dern_li = li - 1
                    dern_co = 7-val+1
                    
                else: #distribuer ligne du dessus + trou qui restent
                    val = jeu[li][co]
                    for g in range(1, 7-co+1):
                        jeu[li][co+g] = jeu[li][co+g] + 1
                        can.itemconfig(tableau[li][co + g],text = str(jeu[li][co + g]))
                    for h in range(0, val-(7-co)):
                        jeu[li-1][7-h] = jeu[li-1][7-h] + 1
                        can.itemconfig(tableau[li-1][7-h], text = str(jeu[li-1][7-h]))
                        
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    dern_li = li - 1
                    dern_co = 7- (val - (7-co) - 1)
                    
                    
        if clic_y > 40 and clic_y < 140: #1ère rangée
            if jeu[li][co] <= co:
                val = jeu[li][co]
                for k in range(1, val+1):
                    jeu[li][co-k] = 1  + jeu[li][co-k] 
                    can.itemconfig(tableau[li][co - k],text = str(jeu[li][co - k]))
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                dern_co = co-val
            
            if jeu[li][co] > co:
                if co == 0:
                    val = jeu[li][co]
                    for h in range(0, val):
                        jeu[li+1][h] = jeu[li+1][h] + 1
                        can.itemconfig(tableau[li+1][h], text=str(jeu[li+1][h]))
                        jeu[li][co] = 0
                        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    dern_li = li + 1
                    print (co,val)
                    dern_co = co + val -1
                    print (dern_co)
                else:
                    val = jeu[li][co]
                    for g in range(1, co+1):
                        jeu[li][co-g] = jeu[li][co-g] + 1
                        can.itemconfig(tableau[li][co - g],text = str(jeu[li][co - g]))
                    for h in range(0, val-co):
                        
                        jeu[li+1][h] = jeu[li+1][h] + 1
                        can.itemconfig(tableau[li+1][h], text = str(jeu[li+1][h]))
                        
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    dern_li = li + 1
                    dern_co = val-co-1
                    
                    
        if clic_y > 140 and clic_y < 240: #2ème rangée
            if jeu[li][co] <= 7-co:
                val = jeu[li][co]
                for k in range(1, val+1):
                    jeu[li][co+k] = 1  + jeu[li][co+k] 
                    can.itemconfig(tableau[li][co + k],text = str(jeu[li][co + k]))
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                dern_co = co + val
                
            if jeu[li][co] > 7-co:
                if co == 7:
                    val = jeu[li][co]
                    for h in range(0, val):
                        jeu[li-1][7-h] = jeu[li-1][7-h] + 1
                        can.itemconfig(tableau[li-1][7-h], text=str(jeu[li-1][7-h]))
                        jeu[li][co] = 0
                        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    dern_li = li - 1
                    dern_co = 7-val+1
                else:
                    val = jeu[li][co]
                    for g in range(1, 7-co+1):
                        jeu[li][co+g] = jeu[li][co+g] + 1
                        can.itemconfig(tableau[li][co + g],text = str(jeu[li][co + g]))
                    for h in range(0, val-(7-co)):
                        
                            jeu[li-1][7-h] = jeu[li-1][7-h] + 1
                            can.itemconfig(tableau[li-1][7-h], text = str(jeu[li-1][7-h]))
                        
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                    dern_li = li - 1
                    dern_co = 7- (val - (7-co) - 1)
        if jeu[dern_li][dern_co] == 1:
            break
        elif jeu[dern_li][dern_co] > 1:
            li = dern_li
            co = dern_co
            print(jeu)
            print (li, co)
        if dern_li == 3:
            clic_y = 350
        if dern_li == 2:
            clic_y = 250
        if dern_li == 1:
            clic_y = 150
        if dern_li == 0:
            clic_y = 50
    print (jeu)
            
            
            
    
        

    
    
    
    
    
can.bind('<Button-1>', adgr)
    
    
    






fen.mainloop()



