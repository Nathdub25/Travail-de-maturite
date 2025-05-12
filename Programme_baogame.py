
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
    
#can.create_oval (40,40,60,60, activewidth = 5)

x = 50
y = 50
cx = 40
cy = 140    

def graineun(event) :
    global x,y,cx,cy
    if x == 750 and y == 150 :
        b = can.find_closest(x,y)
        can.coords(b,740,40,760,60)
        y = 50
        x = 750
        cx = 640
        cy = 40
    elif y == 150 :
        n = can.find_closest(x,y)
        can.coords(n,cx,cy,cx + 20,cy + 20)
        x = x + 100
        cx = cx + 100
    elif x == 50 and y == 50 :
        n = can.find_closest(x,y)
        can.coords(n,40,140,60,160)
        y = 150
        cx = 140
        cy = 140
    else :
        n = can.find_closest(x,y)
        can.coords(n,cx,cy,cx + 20,cy + 20)
        x = x - 100
        cx = cx - 100



graine2 = can.create_oval (40,240,60,260, activewidth = 5)
X = 50
Y = 250
CX = 140
CY = 240
def grainedeux(event) :
    global X,Y,CX,CY
    if X == 750 and Y == 350 :
        b = can.find_closest(X,Y)
        can.coords(b,740,240,760,260)
        Y = 250
        X = 750
        CX = 640
        CY = 240
    elif Y == 350 :
        n = can.find_closest(X,Y)
        can.coords(n,CX,CY,CX + 20,CY + 20)
        X = X + 100
        CX = CX + 100
    elif X == 50 and Y == 250 :
        n = can.find_closest(X,Y)
        can.coords(n,40,340,60,360)
        Y = 350
        CX = 140
        CY = 340
        X = 50
    else :
        n = can.find_closest(X,Y)
        can.coords(n,CX,CY,CX + 20,CY + 20)
        X = X - 100
        CX = CX - 100
    
fen.bind('<Button-3>', grainedeux)
L1 = [1,1,1,1,1,1,1,1]
tableau = []


#fen.bind('<Button-1>', graineun)
for i in range(len(L1)):
    un = can.create_text(i*100 + 40, 40, text = str(L1[i]))
    tableau.append(un)

def adgr(event):
    global tableau
    clic_x = event.x
    clic_y = event.y 
    num_case = clic_x // 100
    L1[num_case] = L1[num_case] + 1
    can.itemconfig(tableau[num_case],text = str(L1[num_case]))
    
fen.bind('<Button-1>', adgr)
    
    
    






fen.mainloop()



