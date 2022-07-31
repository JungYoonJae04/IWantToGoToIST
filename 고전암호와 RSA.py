#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Server: 초기 수열 생성 (등차수열) a*(n-1)d
import random                             
alist=[]                                 
for i in range(2): 
  y = random.randint(1,100)  
  alist.append(y)           
print(alist)
a1 = alist[0]
d2 = alist[1]


# In[ ]:


#Server: 수열을 암호화하여 Client로 송신
result = [a1, d2]
length = len(result) - 1
print(length)
from random import *
print("공개키 생성")
p = int(input("첫번째 소수를 입력하세요 : "))
q = int(input("두번째 소수를 입력하세요 : "))
n = p*q
a = 2
pin =  (p-1)*(q-1)
data = []
so = []
while a < pin:
  for i in range(1, pin + 1):
    if (pin % i == 0) & (a % i == 0):
      data.append(i)
      gcd = i

  if gcd == 1:
    so.append(a)
    a = a +1
  else:
    a = a +13
k = len(so)
i = randrange(k) 
e = so[i]
d = 1
while (e*d)%pin != 1:
  d = d + 1
if e == d:
  d = d + 1
  while (e*d)%pin != 1:
    d = d + 1
print("공개키 (n, e)")
print("개인키 (n, d)")
print("n의 값 ", n)
print("e의 값 ", e)
print("d의 값 ", d)
print("Φ(n)의 값", pin)
codef = []
num = 0
while num <= length :
  M = result[num]
  C = (M**e) % n
  codef.append(C)
  num = num + 1
print(codef)


# In[ ]:


#Client 암호화된 문자를 해독하여 2차 보안 수열값을 얻는다
#암호 복호화
n = int(input("n값을 입력하세요 : "))
d = int(input("d값을 입력하세요 : "))
decode = []
kal = 0
print(codef)
while kal <= length:
  C = codef[kal]
  M = (C**d) % n
  decode.append(int(M))
  kal = kal + 1
print(decode)
print("an = a + (n-1)xd 에서")
print("a =", decode[0])
print("d =", decode[1])


# In[ ]:


#Server: 문자를 암호화하여 Client에게 송신
s = input("Enter : ")
result = []
for i in s:
  result.append(ord(i))
print(result)
length = len(result) - 1
print(length)
#공개키, 개인키 생성
from random import *
print("공개키 생성")
p = int(input("첫번째 소수를 입력하세요 : "))
q = int(input("두번째 소수를 입력하세요 : "))
n = p*q
a = 2
pin =  (p-1)*(q-1)
data = []
so = []
while a < pin:
  for i in range(1, pin + 1):
    if (pin % i == 0) & (a % i == 0):
      data.append(i)
      gcd = i

  if gcd == 1:
    so.append(a)
    a = a +1
  else:
    a = a +13
k = len(so)
i = randrange(k) 
e = so[i]
d = 1
while (e*d)%pin != 1:
  d = d + 1
if e == d:
  d = d + 1
  while (e*d)%pin != 1:
    d = d + 1
print("공개키 (n, e)")
print("개인키 (n, d)")
print("n의 값 ", n)
print("e의 값 ", e)
print("d의 값 ", d)
print("Φ(n)의 값", pin)
code = []
original = []
num = 0
GH = 0
while num <= length :
  M = result[num]
  C = (M**e) % n
  original.append(C)
  GH = a1 + (C-1)*d2
  code.append(GH)
  num = num + 1
print(original)
print(code)


# In[ ]:


#Client: 수신받은 자료를 해독한다.
def free_print(a):
  sen1 = ""
  for i in a:
    sen1 = sen1 + i
  return sen1
#암호 복호화
print(a1, d2)
n = int(input("n값을 입력하세요 : "))
d = int(input("d값을 입력하세요 : "))
decode = []
kal = 0
C = 0
while kal <= length:
  last = code[kal]
  last1 = (last- a1)
  last2 = last1/d2
  C = int(last2 + 1)  
  M = (C**d) % n
  decode.append(chr(M))
  kal = kal + 1
print("해독결과")
print(free_print(decode))


# In[ ]:


#도청자: 공개키만을 이용하야 정보해독 
def free_print(a):
  sen1 = ""
  for i in a:
    sen1 = sen1 + i
  return sen1
K = []
def getPrimaryNum_Eratos(n): 
  nums = [True] * (n + 1) 
  for i in range(2, len(nums) // 2 + 1): 
    if nums[i] == True: 
      for j in range(i+i, n, i): 
        nums[j] = False 
  return [i for i in range(2, n) if nums[i] == True]
print("n 값을 입력하세요")
n = int(input()) 
print("e값을 입력해주세요")
e = int(input())
prime_nums = getPrimaryNum_Eratos(n + 1) 
# prime_nums_reverse = reversed(prime_nums) 
# print(prime_nums) 
if n in prime_nums: 
  print(n) 
else: 
  answers = [] 
  for prime_num in prime_nums: 
    if n % prime_num == 0:
       while(n % prime_num == 0): 
         answers.append(prime_num) 
         n = n // prime_num 
  for num in answers: K.append(num)
print("n 값을 입력하세요")
n = int(input()) 
print(K)
pin = (K[0]-1)*(K[1]-1)
print("Φ(n)의 값", pin)
d = 2 
while (e*d)%pin != 1:
  d = d + 1
print("d의 값 ", d)
decode = []
kal = 0
while kal <= length:
  C = code[kal]
  M = (C**d) % n
  decode.append(chr(M))
  kal = kal + 1
print(free_print(decode))

