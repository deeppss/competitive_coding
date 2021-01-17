Question 
---------
A multiplication is said to be unique when the digits of the multiplicand, multiplier and product are different and digits from 1 to 9 are present in it.
For example, 4*1963 = 7852 is unique multiplication as all the nine digits from 1 to 9 are present in it and the digits in the multiplicand, multiplier and product are different.
Given the multiplicand and the multiplier, write a code to check if it is a unique multiplication. Print Yes for unique multiplication and No otherwise

Solution
---------
n=int(input())
m=int(input())
e=n*m
e=str(e)
m=str(m)
n=str(n)
a=([n[i:i+1] for i in range(0, len(n),1)]) #these satements are used to split each number induvidualy
b=([m[i:i+1] for i in range(0, len(m),1)]) #I can also do list(map(int, m)) to get the same result
c=([e[i:i+1] for i in range(0, len(e),1)])
d=a+b+c
q=len(d)
w=len(set(d))
if(q==w):
    print("Yes")
else:
    print("No")
