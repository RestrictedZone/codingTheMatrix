# Chapter 2 The Field

#common
from plotting import plot
from GF2 import one
from image import color2gray
from image import file2image
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

#2-3
#def solve1(a,b,c): return (c-b)/a
#print solve1(10+5j, 5, 20)

#2-4
#plot(S, 4)

#P.48 2.4.2 Task 2.4.3 
#plot({1+2j+z for z in S}.union(S), 4) # add original set use union function

#P.50 2.4.3 Task 2.4.7
#half
#plot({(1+2j+z)/2 for z in S}.union(S), 4) # add original set use union function
#180 degree
#plot({-(1+2j+z) for z in S}.union(S), 4) # add original set use union function

#P.52 2.4.5 Task 2.4.8
#90 degree
#plot({-1/2j*(1+2j+z) for z in S}.union(S), 4) # add original set use union function

#P.52 2.4.5 Task 2.4.10
data = file2image('img01.png')
data = color2gray(data)     # if occur error, make comment in "image.py" at line 98 
#pts = [[x + y * 1j for x, pixel in enumerate(row) if pixel < 120] for y, row in enumerate(data)]
#pts1 = sum(pts, [])
#plot(pts1, 200, 1)
pts = [[x + y * 1j for x, pixel in enumerate(row) if pixel < 120] for y, row in enumerate(reversed(data))]
pts1 = sum(pts, [])
plot(pts1, 200, 1)
