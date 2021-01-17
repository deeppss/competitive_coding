QUESTION
---------
Same letter distance is the number of characters between two consecutive occurrances of the same character. Given a string, write a code to find 
the letter that has most frequently occurred in it. And also find same letter distance between the occurrances of the most frequently occurred character.
If distance is zero then print ‘No characters’, if distance is 1 then print ‘1 character’ and if distance is ‘d’, greater than 1 then print ‘d characters’.
For example, if the string is ‘accomodation’, the most frequently occurred character is ‘o’ and the same letter distances are

1 character
4 characters

If the string is ‘bookkeeper’, the most frequently occurred character is ‘e’ and the same letter distances are

No characters
1 character

If more than one character occurs maximum number of times then consider the first character in the string.

Input Format
First line contains the string

Output Format
Print the letter that has occurred most frequently
Print the same letter distance for consecutive occurrences of ch in next few lines



SOLUTION
---------
import collections
import sys
a = str(input())
p = (collections.Counter(a).most_common(1)[0][0])  #finding most common letter
u=(collections.Counter(a).most_common(1)[0][1])
if(u==1):
    print("No character")  #is all letters are equally common/there is no common letter 
    sys.exit(0)
lst = []
print(p)
z = ([pos for pos, char in enumerate(a) if char == p])  #to find the all the index of the most common letter
for i in range(len(z) - 1):   #to find the letter distance 
        t = z[i + 1] - z[i] - 1
        if (t == 0):
            print("No characters")
        elif (t == 1):
            print(t, end=" ")
            print("character")
        else:
            print(t, end=" ")
            print("characters")
