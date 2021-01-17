QUESTION
Ordered-Containment of a String
A String S2 is said to be order-contained in another string S1 if all the letters of S2 is present in S1 and order of occurrence of letters of S2 in S1 is same as in S2. For example, elephant contains ant, hat but not tap.

Given two strings S1 and S2, write a code to Print ‘Yes’ if S2 is order-contained in S1 and ‘No’ otherwise. All letters in the input will be lowercase in the given string with no spaces

Input Format
First line contains the string, S1
Second line contains the string, S2

Output Format
Print Yes if S2 is order-contained in S1 and Print No otherwise


SOLUTION
s1=str(input())
s2=str(input())
check=0
check1=0
t=0
for i in s1:
       if i==s2[t]:
            t+=1
            check+=1
       if(check==len(s2)):
         print('Yes')
         check1+=1
         break
if(check1==0):
    print('No')
