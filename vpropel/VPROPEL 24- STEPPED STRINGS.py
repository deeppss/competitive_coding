QUESTION
Stepped if the difference in position of letters in s1 and s2 (in the alphabets) =i where i is the position in the string

SOLUTION
import string, sys
letters = string.ascii_lowercase
space1 = 0
space2 = 0
s1 = input()
s2 = input()
for a in s1:
    if a == ' ':
        space1 += 1
for b in s2:
    if b == ' ':
        space2 += 1
if (space1 != space2):
    print('Length different')
    sys.exit(0)
s1 = s1.split()
s2 = s2.split()
for i3 in range(len(s1)):
        if (len(s1[i3]) != len(s2[i3])):
            print('Strings differ in space')
            sys.exit(0)
        else:
           s1 = ''.join(s1)
           s2 = ''.join(s2)
           check = 0
           check1 = 0
           for i1 in s1:
              if i1 not in letters:
               check += 1
           for i2 in s2:
              if i2 not in letters:
                check += 1
           if (check > 0):
              print('Strings contain non alphabets')
              sys.exit(0)
           if (len(s1) != len(s2)):
              print('Length different')
              sys.exit(0)
           else:
               for i in range(len(s1)):
                  if (abs(letters.index(s2[i]) - letters.index(s1[i]) == i + 1)):
                      check1 += 1
if (check1 == len(s1)):
             print('Strings are stepped')
else:
             print('Strings are not stepped')
