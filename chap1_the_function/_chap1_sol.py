# -*- coding: utf-8 -*-

def Task151():
    print("60*24*7")
    print(60*24*7)

def Task152():
    print("2304811-2304811//47*47")
    print(2304811-2304811//47*47)

def Task154():
    x=-9
    y=1/2
    print(2**(y+1/2) if x+10<0 else 2**(y-1/2))

def Task155():
    print("{x*x for x in {1,2,3,4,5}}")
    print({x*x for x in {1,2,3,4,5}})

def Task156():
    print("{2**x for x in {0,1,2,3,4}}")
    print({2**x for x in {0,1,2,3,4}})

def Task157():
    print("{x*y for x in {1,2,3} for y in {5,7,11}}")
    print({x*y for x in {1,2,3} for y in {5,7,11}})

def Task158():
    print("{x*y for x in {1,2,4} for y in {8,16,32}}")
    print({x*y for x in {1,2,4} for y in {8,16,32}})

def Task159():
    S={1,2,3,4}
    T={3,4,5,6}
    print("{x for x in S if x in T}")
    print({x for x in S if x in T})

def Task1510():
    L=[20,10,15,75]
    avg=sum(L)/len(L)
    print(avg)

def Task1511():
    L1=['A','B','C']
    L2=[1,2,3]
    print([[x,y] for x in L1 for y in L2])

def Task1512():
    LofL=[[.25,.75,.1],[-1,0],[4,4,4,4]]
    print("sum([sum(x) for x in LofL])")
    print(sum([sum(x) for x in LofL]))

def Task1513():
    print("ValueError: (too many | need more) values to unpack")
    # [x,y,z]=[1,2]
    # [x,y,z]=[1,2,3,4]

def Task1514():
    S={-4,-2,1,2,5,0}
    print("[(i,j,k) for i in S for j in S for k in S if i+j+k==0]")
    print([(i,j,k) for i in S for j in S for k in S if i+j+k==0])

def Task1515():
    S={-4,-2,1,2,5,0}
    print("[(i,j,k) for i in S for j in S for k in S if i+j+k==0 and (i,j,k) != (0,0,0)]")
    print([(i,j,k) for i in S for j in S for k in S if i+j+k==0 and (i,j,k) != (0,0,0)])

def Task1516():
    S={-4,-2,1,2,5,0}
    print("{(i,j,k) for i in S for j in S for k in S if i+j+k==0 and (i,j,k) != (0,0,0)][0]")
    print([(i,j,k) for i in S for j in S for k in S if i+j+k==0 and (i,j,k) != (0,0,0)][0])

def Task1517():
    "!! caution: this output is not supported by python 2.x version."
    L=[5,5,5]
    print("L=[5,5,5]")
    print(len(L),"!=",len(list(set(L))))

def Task1518():
    print("{2*x+1 for x in range(50)}")
    print({2*x+1 for x in range(50)})

def Task1519():
    "!! caution: list(zip(...)) != [zip(...)]"
    L=['A','B','C','D','E']
    print(list(zip(range(5),L)))

def Task1520():
    L1=[10,25,40]
    L2=[1,15,20]
    print([x+y for (x,y) in zip(L1,L2)])

def Task1521():
    dlist = [{'James':'Sean','director':'Terence'},{'James':'Roger','director':'Lewis'},{'James':'Pierce','director':'Roger'}]
    k = 'James'
    print([v[k] for v in dlist])

def Task1522():
    dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
    k = 'Frodo'
    print([v[k] if k in v else 'NOT PRESENT' for v in dlist])

def Task1523():
    print({x:x**2 for x in range(100)})

def Task1524():
    D={'red','white','blue'}
    print({x:x for x in D})

def Task1525():
    "How to use digits?"
    base=10
    digits=set(range(base))
    print({x:[(x//base**2)%base,(x//base)%base,x%base] for x in range(1000)})

def Task1526():
    "FIXME: keyError:2 -> id2salary.add 2:0, any other solution?"
    id2salary = {0:1000.0,3:990,1:1200.50,2:0}
    names = ['Larry','Curly','','Moe']
    L = range(len(names))
    d = {names[x]:id2salary[x] for x in L}
    print(d)

def Task1528():
    print("def nextInts(L): return [x+1 for x in L]")

def Task1529():
    print("def cubes(L): return [x**3 for x in L]")

def Task1530():
    print("def dict2list(dct,keylist): return [dct[x] for x in keylist]")

def Task1531():
    print("def list2dict(L, keylist): return {x:y for (x,y) in zip(keylist,L)}")
    print("def list2dict(L, keylist): return {keylist[x]:L[x] for x in range(len(keylist))}")

def Task1532():
    print("def all_3_digit_numbers(base, digits): return set(range(len(digits)**3))")
