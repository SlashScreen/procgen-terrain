#mapgenutils.py

import math

class genmap:
    def __init__(self, termap,terimg,d):
        self.d = d
        self.mp = termap
        self.img = terimg
 #       self.px = self.img.load()
        
    def render(self):
        #creates a new image for itself based on mp
 #       temp = self.img
 #       temppx = temp.load()
        for x in range(self.d):
            for y in range(self.d):
                if self.mp[x][y] == "r":
                    print("r")
                    self.img.putpixel((x,y),(255,255,255))
                elif self.mp[x][y] == "#":
                    print("#")
                    self.img.putpixel((x,y),(135,135,135))
                else:
                    print("g")
                    self.img.putpixel((x,y),(0,0,0))
 #       print(temppx)
 #       self.img = temp
 #       temp.show()
        self.img.show()
                    
    def crop(self,d):
        #crops to dimensions d
        if d > self.d:
            raise("Can't crop bigger than it was")
        delta = self.d-d
        for x in range(delta):
            for y in range(delta):
                del self.mp[d+delta][d+delta]
        self.render()
        
    def drawRect(self,x1,y1,x2,y2,mat):
        for x in range(x1,x2):
            for y in range(y1,y2):
                #print(str(x)+","+str(y))
                self.mp[x][y] = mat
        self.render()
        #Draws a rectangle with material mat
    def drawCircle(self,x,y,r,mat):
        for a in range(360):
            self.mp[x+int(math.cos(a)*r)][y+int(math.sin(a)*r)] = mat
        self.render()
        #draws a circle with material mat and radius r

    def showimg(self):
        self.img.show()
        
