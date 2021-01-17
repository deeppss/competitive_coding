QUESTION
Sum of First Few Consecutive Prime Numbers
Given a number 'n', write an algorithm and a code to check if it can be written as sum of first few prime numbers. Print Yes if 'n' can be written as first few prime numbers and No otherwise. For example, if n is 5 then print Yes as it can be written as 2+3, if n is 41 then print Yes as it can be written as 2 + 3 + 5 + 7 + 11 + 13 and if n is 11 then print 'No' as it cannot be written as sum of first few prime numbers.

Input Format
First line contains the number, n

Output Format
First line contains Yes if the number n can be written as sum of first few prime numbers and No otherwise

SOLUTION
import sys
n = int(input())
c = 0
d=0
sum=0
prime=[]
for num in range(1, 1000):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           prime.append(num)
for i in range(len(prime)-1):
        sum+=prime[i]
        if(sum==n):
            print('Yes')
            c+=1
            break
        else:
            pass
if(c==0):
    print('No')

