#mapgenutils.py

import math

class genmap:
    def __init__(self, termap,terimg,d):
        self.d = d
        self.mp = termap
        self.img = terimg
        
    def render(self):
        #creates a new image for itself based on mp

        for x in range(self.d): #Scanning across x
            for y in range(self.d): #Scan across y
                if self.mp[x][y] == "r": #If "river"
                    self.img.putpixel((x,y),(255,255,255))
                elif self.mp[x][y] == "#": #if "beach"
                    self.img.putpixel((x,y),(135,135,135))
                else: #if "ground"
                    self.img.putpixel((x,y),(0,0,0))

                    
    def crop(self,d):
        #crops to dimensions d
        if d > self.d:
            raise("Can't crop bigger than it was")
        delta = self.d-d #Find the difference
        for x in range(delta):
            for y in range(delta):
                del self.mp[d+delta][d+delta]
        self.render()
        
    def drawRect(self,x1,y1,x2,y2,mat):
        for x in range(x1,x2): #It will go from x range x1-x2 in the map
            for y in range(y1,y2): #Then for each x it will go from y1 t o y2, making a rectangle
                self.mp[x][y] = mat#Set color
        self.render() #Always render afterwards
        #Draws a rectangle with material mat
    def drawCircle(self,x,y,r,mat):
        for a in range(360): #For each degree in a circle
            for l in range(r): #go out from center for each unit in radius, should fill circle
                self.mp[x+int(math.cos(a)*l)][y+int(math.sin(a)*l)] = mat #Sets list at cosine and sine of angle and l to be material
        self.render()
        #draws a circle with material mat and radius r

    def showimg(self):
        self.img.show()
        
