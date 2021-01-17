QUESTION
Secondary Factorial
Factorial of an integer n,  denoted as n! is defined as the product of the first n natural numbers
n! = 1*2*3....*n
1! = 1 and 0! = 1

We define a secondary factorial of a number n, denoted by SF(n), as follows:

SF(n) = 1*3*5*....*n, if n is odd and
SF(n) = 2*4*6*....*n if n is even

If n is an odd number, SF(n) is defined as the product of all the odd numbers, starting from 1, till the number n. SF(5)= 1*3*5= 15.

If n is an even number, SF(n) is defined as the product of all the even numbers, starting from 2, till the number n. SF(6)=2*4*6=48.

Given a number k, write a code to compute SF(n), where k = n!.  For the given number k, If there is no number n such that  n! = k then, your code should print -1.

Illstration
Given k = 24 then 24 = 4! and
SF(4) = 2* 4 = 8.

Given k=25, there is no number n such that 25 = n!, then the out put should be -1.
Given k=6, 6=3!. SF(3)=1*3=3

Input Format
First line contains an integer, k

Ouput Format
Print SF(n) if there exists a number  n, such that k = n! and -1 otherwise



SOLUTION
l=[1,2,6,24,120,120,720,5040,40320,362880,362800,39916800,479001600]
odd=[]
even=[]
pro1=1
pro2=1
n=int(input())
if n not in l:
    print(-1)
else:
    for j in l:
        if(j==n):
            fact=(l.index(j)+1)
            break
    for p1 in range(1, fact+1):
        if p1%2==0:
            even.append(p1)
        else:
            odd.append(p1)
    if(fact%2==0):
        for j1 in even:
            pro1*=j1
        print(pro1)
    else:
        for j2 in odd:
            pro2*=j2
        print(pro2)
