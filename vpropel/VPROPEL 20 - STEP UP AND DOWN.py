QUESTION
Count Move Up and Down
Ramu makes a travel to one his office in a hilly region by his car. Given the height of his current location above sea level every few minutes after he starts the travel, write a code to check the number of up moves and down moves. First move is always up move.

For example, if 12 points are given as follows 45, 60, 82, 72, 65, 32, 53, 84, 103, 110, 89, 95 then there are 3 up moves and 2 down moves as shown below:

Input Format
First line contains the number of current locations of Ramu, n
Next line contains ‘n’ height of locations separated by a space

Output Format
Print the number of Up moves and number of Down moves separated by a space

SOLUTION
n=int(input())
max=0
l1=[]
up=0
down=0
p=list(map(int,input().strip().split()))
for i in p:
    if(i>max):
        max=i
        l1.append('up')
    else:
        max=i
        l1.append('down')
for j in range(len(l1)):
    if(j!=len(l1)-1):
     if(l1[j]!=l1[j+1] and (l1[j]=='up' and l1[j+1]=='down')):
         up+=1
     elif(l1[j]!=l1[j+1] and (l1[j]=='down' and l1[j+1]=='up')):
         down+=1
     else:
         pass
    else:
        if(l1[j]=='up'):
           up+=1
        else:
           down+=1
print(up, end=' ')
print(down)
