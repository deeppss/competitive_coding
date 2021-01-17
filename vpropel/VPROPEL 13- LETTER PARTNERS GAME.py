QUESTION
Letter Partners Game
In a fun game, every letter in English alphabet has a partner. The first thirteen letters of the English alphabet are called pre-partners and the next thirteen letters are called post-partners. That is ‘a’ is the pre-partner and the corressponding post-partner is ‘n’, ‘b’ is the pre-partner and the corressponding post partner is ‘o’ ....‘m’ is the pre-partner and ‘z’ is the post-partner.

In this game, players will be asked to take a lot with a string ‘w’ and they are said to won the game if the following conditions are satisfied by the letters in ‘w’:
(i) The string may be mixed with pre-partners and post-partners but all pre-partners should have a post-partner
(ii) A pre-partner should come before it’s corressponding post-partner
(iii) For a pre-partner that is in position ‘i’ it’s post-partner

(a) Shall come immediately at posititon ‘i+1’

(b) Should come before all corressponding post-partners of pre-partners that is in positions < i and after all corressponding post-partners of pre-partners that is in position > i.

And the player has lost the game otherwise.

For example, if the word in the lot taken is ‘abon’ then the player has won the game. All pre-partners come before the post-partner and condition (iii) is also satisfied as follows:

1) ‘o’ comes immediately after its pre-partner ‘b’, and as per condition (a) of (iii) it is acceptable

2) ‘n’ comes after its prepartner ‘a’ and it comes after the post-partners of pre-partners that has come after ‘a’ and as per condition (b) of (iii) it is acceptable

Whereas if the word in the lot taken is ‘abno’ then the player has lost the game as the post-partener ‘n’ for pre-partner ‘a’ has come before the post-partner of the pre-partner ‘b’, violates condition (iii).
And if the word in the lot is ‘aerfsbon’ then also the player has won the game as shown in the following table:


Input Format
First line contains the word, w

Output Format
Print either Won or Lost

SOLUTION
import string
import sys
flag=False
b=string.ascii_lowercase
s=list(str(input()))
s1=sorted(s)
p=0
if(len(s1)%2!=0):#EXIT IF ODD STRING LENGTH
    print('Lost')
    sys.exit(0)
else: #CHECKING IF ALL POST-LETTERS EXIST IN THE STRING
 number=int(len(s)//2)
 NUM=31
 for i in s:
    k = (ord(i) & NUM) - 1
    if(b.index(b[k])<13):
        if(b[k+13] in s1):
           lst.append(b[k+13])
           p+=1
           if(p==number):
               flag=True
check=0
if(flag):
    for i1 in range(len(s)): #CHECKING IF THE POST LETTER COMES JUST AFTER THE PRE-LETTER
         position = (ord(s[i1]) & NUM) - 1
         if ((position) < 13):
           if(s[i1+1]==b[position+13]):
             check+=1
           if (check >= len(s) // 2):
               print('Won')
               sys.exit(0)
         else:
              for letters in range(len(s)-1): 
               nposition = (ord(s[letters]) & NUM) - 1
               oposition =(ord(s[letters+1]) & NUM) - 1
               if ((nposition) < 13 and oposition<13):
                 if(s.index(b[nposition+13])>s.index(b[oposition+13])):
                   check+=1
                 else:
                     print('Lost')
                     sys.exit(0)
if(check>=len(s)//2):
    print('Won')
else:
    print('Lost')
