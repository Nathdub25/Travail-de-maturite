
from tkinter import *

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
    

jeu = [[2]*8 for i in range(0,4)]
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

    
    if clic_y > 240 and clic_y < 340:
    
        if jeu[li][co] <= co:
            val = jeu[li][co]
            for k in range(1, val+1):
                jeu[li][co-k] = 1  + jeu[li][co-k] 
                can.itemconfig(tableau[li][co - k],text = str(jeu[li][co - k]))
                jeu[li][co] = 0
                can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
            
        if jeu[li][co] > co:
            if co == 0:
                val = jeu[li][co]
                for h in range(0, val):
                    jeu[li+1][h] = jeu[li+1][h] + 1
                    can.itemconfig(tableau[li+1][h], text=str(jeu[li+1][h]))
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
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
                    
    if clic_y > 340 and clic_y < 440:
        if jeu[li][co] <= 7-co:
            val = jeu[li][co]
            for k in range(1, val+1):
                jeu[li][co+k] = 1  + jeu[li][co+k] 
                can.itemconfig(tableau[li][co + k],text = str(jeu[li][co + k]))
                jeu[li][co] = 0
                can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        if jeu[li][co] > 7-co:
            val = jeu[li][co]
            if co == 7:
                for h in range(0, val):
                    jeu[li-1][7-h] = jeu[li-1][7-h] + 1
                    can.itemconfig(tableau[li-1][7-h], text=str(jeu[li-1][7-h]))
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
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
                    
    if clic_y > 40 and clic_y < 140:
        if jeu[li][co] <= co:
            val = jeu[li][co]
            for k in range(1, val+1):
                jeu[li][co-k] = 1  + jeu[li][co-k] 
                can.itemconfig(tableau[li][co - k],text = str(jeu[li][co - k]))
                jeu[li][co] = 0
                can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
            
        if jeu[li][co] > co:
            if co == 0:
                val = jeu[li][co]
                for h in range(0, val):
                    jeu[li+1][h] = jeu[li+1][h] + 1
                    can.itemconfig(tableau[li+1][h], text=str(jeu[li+1][h]))
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
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
                    
    if clic_y > 140 and clic_y < 240:
        if jeu[li][co] <= 7-co:
            val = jeu[li][co]
            for k in range(1, val+1):
                jeu[li][co+k] = 1  + jeu[li][co+k] 
                can.itemconfig(tableau[li][co + k],text = str(jeu[li][co + k]))
                jeu[li][co] = 0
                can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
                
        if jeu[li][co] > 7-co:
            if co == 7:
                val = jeu[li][co]
                for h in range(0, val):
                    jeu[li-1][7-h] = jeu[li-1][7-h] + 1
                    can.itemconfig(tableau[li-1][7-h], text=str(jeu[li-1][7-h]))
                    jeu[li][co] = 0
                    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
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
                    
    
        

    
    
    
    
    
can.bind('<Button-1>', adgr)
    
    
    






fen.mainloop()



