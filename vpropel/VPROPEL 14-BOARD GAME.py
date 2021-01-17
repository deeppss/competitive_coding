QUESTION
Given a size the board, p, initial cell of the coin in the board, a list of movements and a winning cell in the board, write a code to check if the coin reaches the winning cell from initial cell by these movements. If the winning position is reached then print Win and print Loss otherwise.

Input Format

Dimension of the board, p
Initial cell of the coin m,n separated by a space
Number of moves, num1
Next num1 lines contain the movements l-left, r-right, u-up and d-down
Winning cell of the coin m1, n1 separated by a space

Output Format
Print Win or Loss

SOLUTION
p=int(input())
m,n=map(int,input().strip().split())
num1=int(input())
lst=[]
for i in range(num1):
    lst.append(str(input()))
m1,n1=map(int,input().strip().split())
for z in lst:
 if(z=='l'):
     if(n>0):
        n=n-1
     else:
         pass
 elif(z=='r'):
     if(n<p-1):
         n=n+1
     else:
         pass
 elif(z=='u'):
     if(m<p-1):
         m=m+1
     else:
         pass
 elif(z=='d'):
     if(m>0):
         m=m-1
     else:
         pass
if(m==m1 and n==n1):
    print('Win')
else:
    print('Loss')
