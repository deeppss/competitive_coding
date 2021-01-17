QUESTION
Smallest Divisible Number
Given an integer ‘n’ where n>=1, write a C code to check whether there exist a smallest number ‘S’, where S<=10^7 and S is divisible by all even numbers ‘m’ where 1<=m<=n.

For example, when n = 10, the smallest number divisible by all even numbers 2, 4, 6, 8 and 10 is 120. If no such number exist then print ‘No such number in range’.

Input Format
First line contains the number, n

Output Format
Print either the number that is divisible by all even numbers less than ‘n’ or print No such number in range

SOLUTION
import sys
n = int(input())
lst = []
d = 0
for i in range(1, n + 1):
    if (i % 2 == 0):
        lst.append(i)
def findlcm(num1, num2):
    if (num1 > num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while (rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2) / int(gcd))
    return lcm
num1 = lst[0]
num2 = lst[1]
lcm = findlcm(num1, num2)
for j in range(2, len(lst)):
    lcm = findlcm(lcm, lst[j])
if(lcm<=10000000):
 print(lcm)
else:
    print('No such number in range')
