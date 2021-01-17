QUESTION
Search Fibanocci Number
Given an integer n, search for the set of all fibanocci numbers F = {f1∪f2∪f3∪...fn} where fi is the set of fibanocci numbers of length ‘i’ and present in the number ‘n’. A number in fi is formed by taking ‘i’ consecutive digits from ‘n’. For example, if the value of n is 121393 then f1 = {1, 2, 3}, f2 = {13, 21}, f3 = {}, f4 = {}, f5={} and f6={121393} hence F = {1, 2, 3, 13, 21, 121393}. If no fibanocci number is present then print None.

Input Format
First line contains a number, n

Output Format
Print all the fibanocci numbers present in n, in ascending order. Print one number in one line. If no fibanocci number is present then print None.


SOLUTION
def printFibonacciNumbers(n, lst):
    f1 = 0
    f2 = 1
    for x in range(1, n):
        lst.append(f2)
        next = f1 + f2
        f1 = f2
        f2 = next

lst=[]
lst3=[]
n=int(input())
m=str(n)
printFibonacciNumbers(1000, lst)
k=[]
for j in range(1,len(m)+1):
   k+=[m[i:i+j] for i in range(0,len(str(m)),1)]
c=0   
for p in k:
    if(int(p) in lst):
        lst3.append(int(p))
        c+=1
        
if(c==0):
    print('None')
z=sorted(list(set(lst3)))
for h in z:
    print(h)
