
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
tableau = [[]*8 for i in range(0,4)]
#print (tableau[0][0])


for j in range (4):
    for i in range (len(jeu[0])):
        valcer = can.create_text(i*100 + 40,j*100 + 40, text = str(jeu[j][i]))
        print (j, i)
        tableau[j][i].append(valcer)
        print (tableau[j][i])

def adgr(event):
    global tableau
    clic_x = event.x
    clic_y = event.y 
    
    li = clic_x // 100 
    co = clic_y // 100 
        
    jeu[li][co] = 0
    jeu[li][co+1] = jeu[li][co+1] + 1
    can.itemconfig(tableau[li][co],text = str(jeu[li][co]))
    can.itemconfig(tableau[li][co + 1],text = str(jeu[li][co + 1]))

    
    
    
    
    
fen.bind('<Button-1>', adgr)
    
    
    






fen.mainloop()



