#perlintest.py
import perlin

pn = perlin.PerlinNoiseFactory(2)
frameSize = 10
noise = {}
for i in range(frameSize):
    noise[i] = {}
    for j in range(frameSize):
        noise[i][j] = pn(i/frameSize,j/frameSize)
        print(pn(i/frameSize,j/frameSize))
