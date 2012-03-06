# -*- coding: cp1250 -*-
from __future__ import division
from Tkinter import *
import tkMessageBox

"""
self.zid = True
self.premik = False
self.zmaga = False
self.ovira = False
"""

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

class Krog:
    
    def __init__(self, canvas, x, y, col):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.col = col

    def narisi(self):
        self.index = self.canvas.create_oval((self.x*pw, self.y*ph, (self.x+1)*ph, (self.y+1)*pw), fill=self.col)
        
    def nastavi(self, x, y):
        self.x = x
        self.y = y

    def predtla(self, x, y):
        if(p[self.x + x][self.y + y].oime == "lava"):
            p[self.x + x][self.y + y].stage -= 10
        else:
            p[self.x + x][self.y + y] = Tla(canvas, self.x + x, self.y + y, barve["tla"])
            p[self.x + x][self.y + y].update()

    
    def premakni(self,x,y):
        if(p[self.x + x][self.y + y].zid == False and p[self.x + x][self.y + y].premik == False):
            self.x += x
            self.y += y

        elif(((p[self.x + x][self.y + y].premik == True) or (p[self.x + x][self.y + y].oime == "lava" and p[self.x + x][self.y + y].stage > 10)) and p[self.x + 2*x][self.y + 2*y].zid == False):

                if(p[self.x + 2*x][self.y + 2*y].blok_na() == True):
                    self.predtla(x, y)
                    self.x += x
                    self.y += y
            

    def update(self):
        self.canvas.delete(self.index)
        self.narisi()
        global_update()

    def nsupdate(self):
        self.canvas.delete(self.index)
        self.narisi()

class Zid:
    def __init__(self, canvas, x, y, barva):
        self.barva = barva
        self.canvas = canvas
        self.x = x
        self.y = y
        self.zid = True
        self.premik = False
        self.zmaga = False
        self.ovira = False
        self.oime = ""

    def narisi(self):
        self.index = self.canvas.create_rectangle(self.x*pw, self.y*ph, self.x*pw + pw, self.y*ph + ph, fill=self.barva, outline=barve["outline"])
        
    def update(self):
        self.canvas.delete(self.index)
        self.narisi()

class Tla:
    def __init__(self, canvas, x, y, barva):
        self.barva = barva
        self.canvas = canvas
        self.x = x
        self.y = y
        self.tla = True
        self.zid = False
        self.premik = False
        self.zmaga = False
        self.oime = "tla"
        self.ovira = False
        self.index = 0

    def narisi(self):
        self.index = self.canvas.create_rectangle(self.x*pw, self.y*ph, self.x*pw + pw, self.y*ph + ph, fill=self.barva, outline=barve["outline"])

    def update(self):
        self.canvas.delete(self.index)
        self.narisi()

    def izbrisi(self):
        self.canvas.delete(self.index)
        del(self)

    def blok_na(self):
        global p
        p[self.x][self.y] = Blok(self.canvas, self.x, self.y, barve["blok"])
        p[self.x][self.y].update()
        self.izbrisi()
        return True

class Lava:
    def __init__(self, canvas, x, y, barva):
        self.barva = barva
        self.osnovna = barva
        self.canvas = canvas
        self.x = x
        self.y = y
        self.tla = True
        self.zid = False
        self.premik = False
        self.zmaga = False
        self.oime = "lava"
        self.cover = 0
        self.ovira = True
        self.index = 0
        self.stage = 0

    def narisi(self):
        self.index = self.canvas.create_rectangle(self.x*pw, self.y*ph, self.x*pw + pw, self.y*ph + ph, fill=self.barva, outline=barve["outline"])

    def update(self):
        self.canvas.delete(self.index)
        if(self.stage > 10):
            self.premik = True
        else:
            self.premik = False
        self.narisi()

    def izbrisi(self):
        self.canvas.delete(self.index)
        del(self)

    def blok_na(self):
        if self.stage < 11:
            self.stage += 10
        elif self.stage > 10:
            return False
        return True

class Voda:
    def __init__(self, canvas, x, y, barva):
        self.barva = barva
        self.canvas = canvas
        self.x = x
        self.y = y
        self.tla = True
        self.zid = False
        self.premik = False
        self.zmaga = False
        self.oime = "voda"
        self.ovira = True
        self.index = 0

    def narisi(self):
        self.index = self.canvas.create_rectangle(self.x*pw, self.y*ph, self.x*pw + pw, self.y*ph + ph, fill=self.barva, outline=barve["outline"])

    def update(self):
        self.canvas.delete(self.index)
        self.narisi()

    def izbrisi(self):
        self.canvas.delete(self.index)
        del(self)

    def blok_na(self):
        global p 
        p[self.x][self.y] = Tla(canvas, self.x, self.y, barve["tla"])
        p[self.x][self.y].update()
        self.izbrisi()
        return True

class Zmaga():

    def __init__(self, canvas, x, y, barva):
        self.barva = barva
        self.canvas = canvas
        self.x = x
        self.y = y
        self.tla = True
        self.zid = False
        self.premik = False
        self.ovira = False
        self.zmaga = True
        self.oime = ""
       
        self.index = 0

    def narisi(self):
        self.index = self.canvas.create_rectangle(self.x*pw, self.y*ph, self.x*pw + pw, self.y*ph + ph, fill=self.barva, outline=barve["outline"])

    def update(self):
        self.canvas.delete(self.index)
        self.narisi()

    def izbrisi(self):
        self.canvas.delete(self.index)
        del(self)

class Blok:
    def __init__(self, canvas, x, y, barva):
        self.barva = barva
        self.canvas = canvas
        self.x = x
        self.y = y
        self.tla = False
        self.zid = True
        self.premik = True
        self.zmaga = False
        self.ovira = False
        self.oime = ""
        self.index = 0

    def narisi(self):
        self.index = self.canvas.create_rectangle(self.x*pw, self.y*ph, self.x*pw + pw, self.y*ph + ph, fill=self.barva, outline=barve["outline"])

    def update(self):
        self.canvas.delete(self.index)
        self.narisi()   



def global_update():
    for a in list_lava:
#        print(a.ovira)
        if a.stage >= 1:
            a.ovira = False
            a.stage -= 1
            if a.stage > 9:
                a.barva = barve["blok"]
            else:
                a.barva = rgb_to_hex((50 + (10 - a.stage) * (205 / 10), 0, 0))
            a.update()
            player.nsupdate()
#            print("==lavastage-=1, stage={0}".format(a.stage))
        elif a.stage <= 0:
            a.stage = 0
            a.ovira = True
            a.barva = barve["lava"]
            a.update()
            player.nsupdate()
#            print("==lavastage=0, stage={0}, ".format(a.stage))

    if player.x == zmx and player.y == zmy:
        print("YAAAAYY!")
        if tkMessageBox.askquestion("Zmaga!", "Zelite nadaljevati?", icon="info"):
            lvlno += 1
        
    
    if p[zmx][zmy].zmaga != True or p[player.x][player.y].ovira == True:
        print("Idiot!")
        tkMessageBox.showinfo("Poraz", "Si popolnoma nesposeben!")
        root.destroy()    

def readLevel(ime):

    p = []
    with open(ime) as f:
        for i in range(len(f.readline().strip())):
            p.append([])

    with open(ime) as f:
        for a in f:
            a = a.strip()
            for i in range(len(a)):
                if(a == 'O'):
                    p[i].append("O")
                p[i].append(a[i])
    return p

def key(event):
    if event.keysym == "Escape":
        root.destroy()
    else:
        if event.keysym == "Up":
            if player.y > 0:
                player.premakni(0, -1)
                player.update()
        elif event.keysym == "Down":
            if player.y < hei - 1:
                player.premakni(0, 1)
                player.update()
        elif event.keysym == "Left":
            if player.x > 0:
                player.premakni(-1, 0)
                player.update()
        elif event.keysym == "Right":
            if player.x < wid - 1:
                player.premakni(1, 0)
                player.update()
         


######################
#       MAIN         #
######################

zmx = 0
zmy = 0
list_lava = []

lvlno = 1

p = readLevel("lvl" + str(lvlno) + ".txt")

if len(p) > 30 or len(p[0]) > 30:
    if len(p) > 30:
        pw = 900 / int(len(p))
    if len(p[0]) > 30:
        ph = 900 / int(len(p[0]))

root = Tk()
ph = 30
pw = 30

wid = len(p)
hei = len(p[0])

max_width = 1000
max_height = 1000

if(pw * len(p) > max_width or ph * len(p[0]) > max_height):
    pw = ph = min(max_width//len(p), max_height//len(p[0]))

width = pw * wid
height = ph * hei
canvas = Canvas(root, width=width, height=height, bg="white")
canvas.pack()



barve = {"tla":rgb_to_hex((130,130,130)), "zid":"black", "blok":"yellow", "voda":"blue", "lava":"red", "player":"green", "zmaga":"pink", "outline":"black"}

player = Krog(canvas, 0, 0, barve["player"])

for x in range(len(p)):
    for y in range(len(p[0])):
        if p[x][y] == " ":
            p[x][y] = Tla(canvas, x, y, barve["tla"])
            p[x][y].narisi()
        elif p[x][y] == "#":
            p[x][y] = Zid(canvas, x, y, barve["zid"])
            p[x][y].narisi()
        elif p[x][y] == "X":
            p[x][y] = Blok(canvas, x, y, barve["blok"])
            p[x][y].narisi()
        elif p[x][y] == "V":
            p[x][y] = Voda(canvas, x, y, barve["voda"])
            p[x][y].narisi()
        elif p[x][y] == "L":
            p[x][y] = Lava(canvas, x, y, barve["lava"])
            p[x][y].narisi()
            list_lava.append(p[x][y])
        elif p[x][y] == "+":
            p[x][y] = Zmaga(canvas, x, y, barve["zmaga"])
            zmx = x
            zmy = y
            p[x][y].narisi()
        elif p[x][y] == "O":
            p[x][y] = Tla(canvas, x, y, barve["tla"])
            p[x][y].narisi()
            player.nastavi(x,y)
            player.narisi()

root.bind_all("<Key>", key)

root.focus_force()
root.mainloop()
