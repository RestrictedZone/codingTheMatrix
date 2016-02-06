# -*- coding: utf-8 -*-
from myutil import consolePrintWithLineNumber as c
'''
Created on 2015. 8. 12.
 
@author: Administrator
'''
'''
  ch02 필드
'''
# 46p
 
from math import e
from math import pi
 
from GF2 import one
from image import color2gray
from image import file2image
from plotting import plot    
 
 
c(1 + 3j)
c(1j)
 
c((1 + 3j) + (2 + 2j))
x = 1 + 3j
c(x ** 2)
c(x.real)
c(x.imag)
 
c(type(1 + 2j))    # class 'complex'...
 
# 47p
# ax + b = c
def solve1(a, b, c): return (c - b) / a
# 10x + 5 = 30
c(solve1(10, 5, 30))
# (10+5i)x+ 5 = 20
c(solve1(10 + 5j, 5, 20))
 
# 48p
 
# module six를 설치해야 한다. 
# > pip install six
# > pip install python-dateutil
# > pip install pyparsing
# 기타 여러 문제 해결 > https://wikidocs.net/1019
 
# matplotlib 사용법
# import matplotlib.pyplot as plt
# x = range(100)
# y = [ i * i for i in x]
# plt.plot(x, y)
# plt.show()
 
# 저자 사이트에서 plotting.py 파일 다운받기(matplotlib가 아니다.) > http://resources.codingthematrix.com/
# 익스플로러가 열린후, 스크립트가 적용이 안된다.???
# 작동이 되지 않는다면, plotting.py 파일안에 create_temp 함수에서 remove_at_exit(path) 부분을 주석처리한다.
# > exit 될때, 임시파일을 삭제하는 부분인데, 파일이 삭제되는 시점이 너무 빨라서, 웹브라우저가 가동했지만 정작 파일읃 찾지 못하기 때문.
S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
# plot(S, 4)    # 웹브라우저로 출력, plot 함수는 전체 실행할 때마다 계속 브라우저를 호출하므로, 테스트 후 주석처리 함. 
 
# 49p
c(abs(3 + 4j))
c(abs(1 + 1j))
c((3 + 4j).conjugate())    # 공액 복소수(z.real - z.imag)
 
# 50p
S1 = {1 + 2j + z for z in S}
c(S1)
# plot(S1, 4)
 
S2 = {-2 - 2j + z for z in S}
# plot(S2, 4)
 
# 51p
# 52p
S3 = {z / 2 for z in S}
# plot(S3, 4)
S4 = {z * 2 for z in S}
# plot(S4, 4)
'''
  <번역오류?>
  마찬가지로, 각 복소수를 2배 하는 것은 점들을 원점과 서로에게 더 가까워지게 한다.
  > 마찬가지로, 각 복소수를 2배 하는 것은 점들을 원점과 서로에게 더 멀어지게 한다.
'''
  
# 53p
S1 = {z * -1 for z in S}
# plot(S1, 4)
 
# 90도 회전한 이미지가 책과 다르다;;;
S1 = {z * 1j for z in S}
# plot(S1, 4)
 
# 54p
  # Task2.4.8
S1 = {z * 1j / 2 for z in S}
# plot(S1, 4)
  # Task2.4.9
S1 = {(z * 1j) / 2 + 2 - 1j for z in S}
# plot(S1, 4)
  # Task2.4.10
  # 밝기가 아니라 색상이다. RGB : (183,183,183)
  # color2gray의 리턴값(밝은 정도) 중에 120보다 작은 값을 가진 픽셀만 추린다.
data = file2image('img01.png')
data = color2gray(data)
pts = [[x + y * 1j for x, pixel in enumerate(row) if pixel < 120] for y, row in enumerate(data)]
pts1 = sum(pts, [])
# plot(pts1, 200, 1)    # 200은 스케일, 1은 점의 굵기
  # > 이미지가 반대로 나온다...x, y가 뒤바뀐듯.
  # file2image 함수 결과값에서부터 반대로 나온다.
  # 리스트를 컴프리헨션 할때, 마지막값부터 읽어보자. reversed 이용
pts = [[x + y * 1j for x, pixel in enumerate(row) if pixel < 120] for y, row in enumerate(reversed(data))]
pts1 = sum(pts, [])
# plot(pts1, 200, 1)
 
# 55p
  # Task2.4.11 복소수의 중심을 구한다. 그러고나서 원점으로 평행이동
def f(zlist):
  x_min = 0
  x_max = 0
  y_min = 0
  y_max = 0
  for z in zlist:
    x = z.real
    y = z.imag
    if(x_min >= x):
      x_min = x
    if(x >= x_max):
      x_max = x
    if(y_min >= y):
      y_min = y
    if(y > y_max):
      y_max = y
  x_center = x_max - x_min
  y_center = y_max - y_min
 
  # 그림의 중심에 해당하는 복소수z1의 반대방향-z1/2을 더한다.
  # 그냥 -z1을 더하면, 반대쪽 원점을 중심으로 대칭이동이 된다.   
  return [z - x_center / 2 - y_center / 2 * 1j for z in zlist]
 
pts2 = f(pts1)
# plot(pts2, 200, 1)
   
# plot([z * 1j / 2 for z in pts1], 200, 1)
 
# 56p 오타?? 아래 그림의 z1,z2사이의 각도가 pi/4이 아닌 pi/8이다.
 
# 57p
  # Task2.4.17
n = 6
w = e ** (2 * pi * 1j / n)
list = [w ** x for x in range(0, n)]
c(list)
# plot(list, 3, 3)  
   
# 58p
  # Task2.4.18
S1 = [z * e ** ((pi / 4) * 1j) for z in S]
# plot(S1, 4)
  # Task2.4.19
pts2 = [z * e ** ((pi / 4) * 1j) for z in pts1]
# plot(pts2, 200, 1)
 
# 61p
  # Task2.4.20(중심 평행이동, 회전, 스케일링)
pts2 = [z * e ** ((pi / 4) * 1j) * 0.5 for z in f(pts1)]
# plot(pts2, 200, 1) 
   
# 60p
# GF(2) 갈루아 필드 .... 무슨 소리지??
c(one * one)
c(one * 0)
c(one + 0)
c(one + one)
c(-one)
 
# 62p
'''
  P2.5.1 이걸 어떻게 알아???
  > 암호KEY의 가능성은 2**5 = 32가지이다. 이걸로 다 돌려보자
  복호화 알고리즘은 앞페이지의 방법을 역으로 이용한다.(다른 방법이 없다..-_-;;)
  암호문1 = KEY1 + 평문1
  평문1 = 암호문1 - KEY1
   
        복호화(32가지 KEY 적용)
           ↓
  암호문 Q1 ----> 평문 Q2 ---> 5개씩 자르고 -> 10진수 -> 알파벳  
'''
Q1 = '1010100100101010101111001000110101110101001001100111010'
# '01010' 을 10진수 숫자로 변환
def bin2dec(bin):  
  base = 2
  digits = 5
  return sum([int(bin[i]) * (base ** (digits - i - 1)) for i in range(digits)])
# 10진수 숫자를 2진수 5자리로 만들기(KEY 만들때 사용)
def dec2bin(num):
    digits = 5
    bStr = ""
    while num > 0 :
        bStr = str(num % 2) + bStr
        num = num >> 1
     
    # 자리수 맞춰주기
    while(len(bStr) < digits):
      bStr = '0' + bStr
    return bStr
# 10진수 숫자를 알파벳으로 변환
def dec2AZ(num):
  if num <= 25:
    return chr(num + 97)    # chr <-> ord 아스키코드표 기준
  elif num == 26:
    return ' '
  elif num > 26:    # KEY가 잘못된 경우, 예상 범위를  넘어서는 결과가 나오기도 한다. 이 경우 대체할 문자가 없으므로 *로 표시한다.
    return '*'
# 문자열 s를 n자리수로 잘라서 리스트로 만든다.
def chunks(s, n):
  list = []
  for start in range(0, len(s), n):
    list.append(s[start:start + n])
  return list
# 복호화 알고리즘
def decodeLogic(c, key):
  #  평문1 = 암호문1 - KEY1
  return abs(c - key)
def sol1():
  # 가능한 암호 55자리(11*5) 만들기. 32개
  keylist = []
  for i in range(32):
    s0 = dec2bin(i) * 11
    keylist.append(s0)
  # 복호화
  plainlist = []
  for key in keylist:
    s = ''
    for index, k in enumerate(key):
      s = s + str(decodeLogic(int(Q1[index]), int(k)))
    plainlist.append(s)
  # 결과를 5자리로 자르고
  chrunkslist = []
  for list in plainlist:
    chrunkslist.append(chunks(list, 5))
  # 문자로 변환
  resultlist = []
  for clist in chrunkslist:
    s2 = ''
    for bin in clist:
      s2 = s2 + dec2AZ(bin2dec(bin))
    resultlist.append(s2)
  return resultlist    
 
c(sol1())    # 32개 결과중에 답이 될 만한 것을 찾아보자. 답은 'eve is evil' 이다. 헉! 소름끼친다...  