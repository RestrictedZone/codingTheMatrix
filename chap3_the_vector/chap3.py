# Chapter 2 The Field

#common
from plotting import plot

S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}
L = [[2,2],[3,2],[1.75,1],[2,1],[2.25,1],[2.5,1],[2.75,1],[3,1],[3.25,1]]


#Task 3.3.2
#plot(L, 4)

def add2(v,w):
  return[v[0]+w[0], v[1]+w[1]]

#Quiz 3.4.2


#Task 3.4.3
#plot([add2(v, [1,2])for v in L] + L, 8)

def scalar_vector_mult(alpha, v):
  return [ alpha*v[i] for i in range( len(v) ) ]

v=[3,2]
#plot( [ scalar_vector_mult(i/100.0, v) for i in range(101) ], 5 )

class Vec:
  def __init__(self, labels, function):
    self.D = labels
    self.f = function

def zero_vec(D):
  return Vec(D, {})

def setItem(v, d, val): 
  v.f[d] = val

def getItem(v, d):
  if d in v.f:
    return v.f[d]
  else
    return 0


    
v = Vec( {'A','B','C'}, {'A':1} )

