QUESTION
---------
Sliding Friction
Sliding friction is contact force generated when an object moves over a surface. Few wooden blocks of different heights are put in a room. An experiment is to be carried over in which a ball has to roll up and down over a steps like structure. The experimenter wishes to find the maximum size of the steps structure present in the wooden block and he prefers to have a step up operation from left to right. Given the height of the wooden blocks arranged in the room, write a code to find the starting and ending position of the wooden blocks that can form a steps structure. When more than one steps structure of same maximum size is available consider the one that comes first from left to right.

Example 1

Heights = 5 6 3 5 7 8 9 1 2
Longest step up structure from left to right is
3 5 7 8 9
and positions are from 3 to 7
Heights = 12 13 1 5 4 7 8 10 10 11
Longest step up structure from left to right is
4 7 8 10
and positions are from 5 to 8

Input Format
First line contains the number of wooden blocks, n
Next line contains the height of the wooden blocks separated by a space

Output Format
Print the starting and ending positions of the wooden blocks that can form a step structure of maximum size separated by a space



SOLUTION
--------
n=int(input())
l=[]
m=list(map(int,input().strip().split()))
check=0
start=0
end=0
for i in range(n-1):
    if(m[i]<m[i+1]):
        check+=1
        if(check==1):
         start=i+1
    else:
        end=i+1
        l.append((check, start, end))
        check=0
z=(sorted(l, key=lambda x:x[0]))
d=z[-1][1]
d1=z[-1][2]
print(d, d1)
