from plotting import plot

def scalar_vector_mult(alpha, v): return [alpha*v[i] for i in range(len(v))]
def add2(v1,v2): return [sum(v) for v in zip(v1,v2)]

# defined by Task 3.3.2
L = [[2,2],[3,2],[1.75,1],[2,1],[2.25,1],[2.5,1],[2.75,1],[3,1],[3.25,1]]

def Task332():
    plot(L, 4)

def Task343():
    mov = [add2(v,[1,2]) for v in L]
    print(mov)
    plot(mov, 4)

def Task354():
    pts1 = [scalar_vector_mult(0.5, v) for v in L]
    pts2 = [scalar_vector_mult(-0.5, v) for v in L]
    "help(list): __add__ overloading"
    pts = [x for x in pts1 + pts2]
    print(pts)
    plot(pts, 4)

def Task369():
    def segment(pt1, pt2): return [add2(scalar_vector_mult(t/100,pt1),scalar_vector_mult(1-(t/100),pt2)) for t in range(100)]
    pts = segment([3.5,3],[0.5,1])
    print(pts)
    plot(pts, 6)
