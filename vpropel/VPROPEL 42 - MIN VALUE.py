QUESTION
Minimum Value Expression
Given three integers a,b,c ≥ 0, write a C++ program to find the minimum value that may be obtained by expression with only binary operators +, - and *. Use all the three integers for finding minimum value. For example when a= 2, b =1 c = 3 minimum value is -5

Input Format

First line contains the value of a

Next line contains the value of b

Next line contains the value of c

Output Format

Print the minimum value that can be obtained


SOLUTION
a=int(input())
b=int(input())
c=int(input())
l=[a,b,c]
m=min(a,b,c)
l.remove(m)
l=sorted(l)
f1=m-(l[0]*l[1])
f2=m-l[0]-l[1]
print(min(f1,f2))
