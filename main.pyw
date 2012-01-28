try:
    # Python2
    from Tkinter import *
except ImportError:
    # Python3
    from tkinter import *

lastx = 0
lasty = 0
col = "red"


class Krog:
    
    def __init__(self, canvas, x, y, r, col):
        self.x = x
        self.y = y
        self.r = r
        self.canvas = canvas
        self.col = col

    def narisi(self):
        self.index = self.canvas.create_oval((self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r), fill=col)

    def premakni(self,x,y):
        self.x += x
        self.y += y

    def update(self):
        self.canvas.delete(self.index)
        self.narisi()
        

def key(event):
    """shows key or tk code for the key"""
    if event.keysym == 'Escape':
        root.destroy()
    if event.char == event.keysym:
        # normal number and letter characters
        print( 'Normal Key %r' % event.char )
    elif len(event.char) == 1:
        # charcters like []/.,><#$ also Return and ctrl/key
        print( 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
    else:
        # f1 to f12, shift keys, caps lock, Home, End, Delete ...
#        print( 'Special Key %r' % event.keysym )
        global player
        if event.keysym == 'Up':
            if player.y > (35 + player.r):
                player.premakni(0,-35)
                player.update()
        elif event.keysym == "Down":
            if player.y < (int(canvas.cget("height")) - 35):
                player.premakni(0,35)
                player.update()
        elif event.keysym == "Left":
            if player.x > (35 + player.r):
                player.premakni(-35,0)
                player.update()
        elif event.keysym == "Right":
            if player.x < (int(canvas.cget("width")) - 35):
                player.premakni(35,0)
                player.update()

def delete(event):
    canvas.delete("all")

root = Tk()

p = [[' ' for j in range(15)] for i in range(20)]
p[1][3] = "#"

rx = 1
ry = 1

print(len(p[0]))
width = 700
height = 525
canvas = Canvas(root, width=width, height=height, bg="lightskyblue")
canvas.pack()

player = Krog(canvas, 18, 18, 17, "red")
player.narisi()

##rect = canvas.create_rectangle(150, 50, 200, 200, fill="blue", outline="green")

for i in p:
    ry = 1
    for e in i:
        if e == " ":
            rect = canvas.create_rectangle(rx, ry, rx + 35, ry + 35)
            ry += 35
        elif e == "#":
            rect = canvas.create_rectangle(rx, ry, rx + 35, ry + 35, fill = "black")
            ry += 35
    rx += 35

root.bind_all("<Key>", key)

root.mainloop()
