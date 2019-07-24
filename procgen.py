import mapgenutils as gu


if __name__ == "__main__" :
    test = gu.genmap(350,4,1,waterheight = .2)
    test.drawCircle(10,10,6,"r")
    test.drawRect(15,15,25,25,"r")
    test.render()
    test.showimg()
