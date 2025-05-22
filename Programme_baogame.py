
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
    

jeu = [[1]*8 for i in range(0,4)]
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
    if clic_y > 240 and clic_y < 340 and clic_x > 140:
        jeu[li][co-1] = jeu[li][co-1] + jeu[li][co]    
        jeu[li][co] = jeu[li][co]-jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li][co - 1],text = str(jeu[li][co - 1]))
    if clic_x > 0 and clic_x < 140 and clic_y > 240 and clic_y < 340:
        jeu[li+1][co] = jeu[li+1][co] + jeu[li][co]
        jeu[li][co] = jeu[li][co] - jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li+1][co],text = str(jeu[li+1][co]))
    if clic_y > 340 and clic_y < 440 and clic_x < 740:
        jeu[li][co+1] = jeu[li][co+1] + jeu[li][co]    
        jeu[li][co] = jeu[li][co]-jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li][co + 1],text = str(jeu[li][co + 1]))
    if clic_x > 740 and clic_x < 840 and clic_y > 340 and clic_y < 440:
        jeu[li-1][co] = jeu[li-1][co] + jeu[li][co]
        jeu[li][co] = jeu[li][co] - jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li-1][co],text = str(jeu[li-1][co]))
    if clic_y > 140 and clic_y < 240 and clic_x < 740:
        jeu[li][co+1] = jeu[li][co+1] + jeu[li][co]    
        jeu[li][co] = jeu[li][co]-jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li][co + 1],text = str(jeu[li][co + 1]))
    if clic_x > 740 and clic_x < 840 and clic_y > 140 and clic_y < 240:
        jeu[li-1][co] = jeu[li-1][co] + jeu[li][co]
        jeu[li][co] = jeu[li][co] - jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li-1][co],text = str(jeu[li-1][co]))
    if clic_y > 0 and clic_y < 140 and clic_x > 140:
        jeu[li][co-1] = jeu[li][co-1] + jeu[li][co]    
        jeu[li][co] = jeu[li][co]-jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li][co - 1],text = str(jeu[li][co - 1]))
    if clic_x > 0 and clic_x < 140 and clic_y > 0 and clic_y < 140:
        jeu[li+1][co] = jeu[li+1][co] + jeu[li][co]
        jeu[li][co] = jeu[li][co] - jeu[li][co]
        can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
        can.itemconfig(tableau[li+1][co],text = str(jeu[li+1][co]))


    
    
    
    
    
can.bind('<Button-1>', adgr)
    
    
    






fen.mainloop()



