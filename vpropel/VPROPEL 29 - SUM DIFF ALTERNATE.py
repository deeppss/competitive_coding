s=str(input())
l1=[]
l2=[]
for i in range(len(s)):
  if i%2==0:
    l1.append(s[i])
  else:
    l2.append(s[i])
 print(abs(sum(l1)-sum(l2)))     
