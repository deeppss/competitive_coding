QUESTION
--------
In English, blend words are words which are formed by combining two English words. Vowel based blended words are one which are formed by joining the part of the first word before a vowel in it and part of the second word starting from the same vowel as in first word.
For example, spork is a vowel based blending word formed from spoon and fork as shown below:
spoon + fork – spork (sp+ork)
When more than one vowel is present in the words, consider the first occurrence of the vowels.
Given two words, write a code to form the vowel based blended word from them

Input Format
First line contains the first word, w1
Next line contains the second word, w2

Output Format
Print the vowel based blended words formed


Solution
--------
w1=list(str(input()))
w2=list(str(input()))
vowel=['a','e','i','o','u']
for i in w1:
    if(i not in vowel):
        print(i,end="")
    else:
        s=i
        break
for i in w2:
    if(i==s):
      p=(w2[w2.index(s):])
      print("".join(p))
