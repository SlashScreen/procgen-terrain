#mapgenutils.py

import math
import perlin
from PIL import Image

class genmap:
    def __init__(self,dimensions, heightmod, heightboost, genBeach = True, printh = False, waterheight = 0):
        ###GENERATE###
        pn = perlin.PerlinNoiseFactory(2,octaves = 2)
        termap = {}
        terimg = Image.new("RGB",(dimensions,dimensions))
        terpx = terimg.load()
        for x in range(dimensions):
            termap[x] = {}
            for y in range(dimensions):
                value = pn(x/(dimensions/2),y/(dimensions/2))*heightmod+heightboost
                #print(value)
                i = ""
                p = (255,255,255)
                if value <= waterheight:
                    i = "r"
                    
                else:
                    i = "g"
                    p = (0,0,0)
                termap[x][y] = i
                terpx[x,y] = p

        #pseudocode
        #only blank and not blank
        #then replace edges with #

    #Idea: if more water than land, flip the water and land

        if genBeach:
            for x in range(dimensions-1):
                for y in range(dimensions-1):
                    if x > 0 and y > 0:
                        if termap[x][y] == "g" and termap[x+1][y] == "r":
                            termap[x][y] = "#"
                            terpx[x,y] = (135,135,135)
                        elif termap[x][y] == "g" and termap[x-1][y] == "r":
                            termap[x][y] = "#"
                            terpx[x,y] = (135,135,135)
                        elif termap[x][y] == "g" and termap[x][y+1] == "r":
                            termap[x][y] = "#"
                            terpx[x,y] = (135,135,135)
                        elif termap[x][y] == "g" and termap[x][y-1] == "r":
                            termap[x][y] = "#"
                            terpx[x,y] = (135,135,135)
                            #New apprach: scan around pixel, if next over is not equal to this ine, set to beach

        ###PRINT###
        if printh:
            for key,value in termap.items():
                out = ""
                for k,v in value.items():
                    out = out+str(v)
                print(out)

            terimg.show()

        self.mp = termap
        self.img = terimg
        self.d = dimensions
        
            
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


    #Pseudocode
    #River goes in a direction that changes slightly each step
    #each step draw a circle with slight size variation
    #make beach generator and all that stuff inside the class
