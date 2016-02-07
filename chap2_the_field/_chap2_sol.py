from plotting import plot
from math import e, pi
from image import *

S={2+2j,3+2j,1.75+1j,2+1j,2.25+1j,2.5+1j,2.75+1j,3+1j,3.25+1j}

def Task241():
    plot(S, 4)
    print("plot(S, 4)...")

def Task243():
    plot({1+2j+z for z in S}, 4)
    print("plot({1+2j+z for z in S}, 4)...")

def Task247():
    plot({z/2 for z in S}, 4)
    print("plot({z/2 for z in S}, 4)...")

def Task248():
    plot({z*(-1j)/2 for z in S},4)
    print("plot({z*(-1j)/2 for z in S},4)...")

def Task249():
    plot({z*(-1j)/2 +2 -1j for z in S}, 4)
    print("plot({z*(-1j)/2 +2 -1j for z in S}, 4)...")

def Task2410():
    data = color2gray((file2image('img01.png')))
    row = len(data[0])
    col = len(data)
    pts = {x+y*1j for x in range(row) for y in range(col) if data[col-y-1][x]<120}
    plot(pts, max(row, col), 1)

def Task2411():
    def f(z):
        avg = sum(z)/len(z)
        return {x-avg for x in z}
    plot(f(S), 4)

def Task2412():
    data = color2gray((file2image('img01.png')))
    row = len(data[0])
    col = len(data)
    pts = {(x+y*1j)*(-1j) for x in range(row) for y in range(col) if data[col-y-1][x]<120}
    plot(pts, max(row, col), 1)

def Task2417():
    """
    How do i know math modules?
    >>> import math
    >>> help(math)
    """
    n=20
    w=e**(2*pi*1j/n)
    pts={w**(x) for x in range(n)}
    print(pts)
    plot(pts, 4)

def Task2418():
    pts={x*e**(pi/4*1j) for x in S}
    plot(pts, 4)

def Task2419():
    data = color2gray((file2image('img01.png')))
    row = len(data[0])
    col = len(data)
    pts = {(x+y*1j)*e**(pi/4*1j) for x in range(row) for y in range(col) if data[col-y-1][x]<120}
    plot(pts, max(row, col), 1)

def Task2420():
    data = color2gray((file2image('img01.png')))
    row = len(data[0])
    col = len(data)
    pts = {(x+y*1j)*e**(pi/4*1j) for x in range(row) for y in range(col) if data[col-y-1][x]<120}
    avg = sum(pts)/len(pts)
    pts2 = {(z-avg)/2 for z in pts}
    plot(pts2, max(row, col), 1)
