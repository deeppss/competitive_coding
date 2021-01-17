QUESTION
Digit Mapping for Characters
Given a string S with distinct letter find a mapping for each letter in it such that the number formed by replacing the letter with the numbers is a largest possible perfect square with different digits.

A number is said to be perfect square if the number is square of an integer. For example, if the word given is ‘care’ then the following map shall be done for the characters:

c – 9
a – 8
r – 0
e – 1

The number 9801 is a perfect square since 992 is 9801.

Input Format
First line contains the string for which numbers are to be assigned for characters

Output Format
Print character of the string and the number mapped for it separated by a space


SOLUTION
import math
a=str(input())
n=len(a)
lst=[]
p=1
k=1
lst1=[]

for i in range(15):
  largest = list(str(pow(math.ceil(math.sqrt(pow(10, n))) - k, 2)))
  o=len(largest)
  p=len(set(largest))
  if(o==p):
      break
  else:
      k += 1

for i in range(n):
        print(a[i], end=" ")
        print(largest[i])
