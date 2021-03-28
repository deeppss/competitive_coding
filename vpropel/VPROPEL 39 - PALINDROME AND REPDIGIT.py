QUESTION
Palindrome and Repdigit
Given a range of integers, write a C/C++ program to identify numbers which are not palindromes and whose cube root is a repdigit. A repdigit is a number which is composed of same digit. For example, tthe numbers between 10 and 99999 (inclusive) that are satisfying the conditions are 10648, 35937 and 85184 and their corressponding cube roots which are repdigits are 22, 33 and 44.

Boundary conditions

Upper bound of range of values can be 1013

Input Format

First line contains the lower bound value of the range, l

Next line contains the upper bound value of the range, u

Output Format

In one line print the number ‘n’ which is not a palidrome and its cube root which is a repdigit separated by a tab

Print in ascending order of n

SOLUTION
def check(n):
    if str(n) == str(n)[0] * len(str(n)):
        return True
    else:
        return False
def notpalindrome(n):
   n=str(n)
   if n!=n[::-1]:
       return True
   else:
       return False
l=int(input())
u=int(input())
for i in range(l,u+1):
    z=pow(i,3)
    if check(i) and z>l and z<u and notpalindrome(z):
        print(z,end="   ")
        print(i)
