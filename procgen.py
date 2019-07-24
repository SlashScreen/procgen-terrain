import noise
from PIL import Image
import mapgenutils as gu
import perlin

def gen_baseterrain(dimensions, heightmod, heightboost, genBeach = True, printh = False, waterheight = 0):

    ###GENERATE###
    pn = perlin.PerlinNoiseFactory(2,octaves = 6)
    termap = {}
    terimg = Image.new("RGB",(dimensions,dimensions))
    terpx = terimg.load()
    for x in range(dimensions):
        termap[x] = {}
        for y in range(dimensions):
            value = pn(x/dimensions,y/dimensions)*heightmod+heightboost
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

    gmp = gu.genmap(termap,terimg,dimensions)
    
    return gmp

if __name__ == "__main__" :
    test = gen_baseterrain(150,.5,1,waterheight = 1)
    test.drawCircle(10,10,6,"r")
    test.drawRect(15,15,25,25,"r")
    test.render()
    test.showimg()
