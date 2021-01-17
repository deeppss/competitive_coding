QUESTION
Fibanocci Increment Mixed String
Increment mixed string is an operation which operates on two strings S1 and S2 of same length to generate a new string S3. The letters in odd position of S3 is one more than the corressponding letter in S1 and the letters in even position of S3 is one more than the corressponding letter in S2. For example, if S1 = ‘amey’ and S2 = ‘dhft’ then S3 = ‘bifu’. For letter ‘z’, letter ‘a’ is one more than it.


Fibanocci increment mixed string is operation which operates on the last two strings in the series. Given two strings, S1 and S2 write a code to generate the nth element using Fibanocci increment mixed string operation. The given strings S1 and S2 are the first two elements in the Fibanocci increment mixed string series. Third element in the series is found by applying increment mixed string operation for first two elements.


If S1 = ‘amey’ and S2 = ‘dhft’ then the first five elements in the series are as follows:

amey
dhft
bifu
ejgv
ckgw


Input Format
First line contains the string S1
Next line contains the string S2
Next line contains the value of n

Output Format
Print the nth element in the Fibanocci increment mixed string series


SOLUTION
import string
a=string.ascii_letters
s1=list(str(input()))
s2=list(str(input()))
master=[]
master.append("".join(s1))
master.append("".join(s2))
n=int(input())
l=[]
l1=[]
NUM=31
t=0
for fibo in range(n):
 if(t<n-2):
  l=[]
  l1=[]
  l3=[]
  s1=master[t]
  s2=master[t+1]
  t+=1
  for p in range(len(s1)):
   for i in s1:
       k=((ord(i)&NUM)-1)
       l.append(a[k+1])

   for j in s2:
        z=((ord(j)&NUM)-1)
        l1.append(a[z+1])
   break
  starts1=0
  starts2=1
  for boi in range(len(s1)):
     if(len(l3)%2==0):
        l3.append(l[starts1])
        starts1+=2
     else:
        l3.append(l1[starts2])
        starts2 += 2
  l3="".join(l3)
  master.append(l3)
print(master[-1])
