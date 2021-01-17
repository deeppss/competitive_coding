QUESTION
Splicing of Strings
Let S1 and S2 be any two strings with few symbols in common. If there are duplicates in S1 or S2 then remove them. During the duplicate removal process retain the first occurence of the characters. For example, if element is the string then after duplicates removal it will be elmnt.

Crossover is the process of joining two strings S1 and S2 with pivot as one of the common characters of S1 and S2. If ‘α’ be a common character of S1 and S2 such that S1 = Prefix(S1)αSuffix(S1) and S2 = Prefix(S2)αSuffix(S2). Here Prefix(S1) is the sequence of characters that appear before α in S1 and Suffix(S1) is the sequence of characters that appear after α in S1. Then crossover(S1,S2, α) = Prefix(S1)+α+Suffix(S2) and Prefix(S2)+α+Suffix(S1). Splicing is the process of forming all posible new strings from S1 and S2 by performing crossover of S1 and S2 with all common characters.

For example, consider two strings abcdce and ecfgdc then after duplicate removal the strings are abcde and ecfgd. There are three common characters ‘c’ and ‘d’.

crossover(s1,s2,c) = abcfgd and ecde
crossover(s1,s2,d) = abcd and ecfgde
crossover(s1,s2,e) = abcdecfgd and e
and splicing (s1, s2) = abcfgd, ecde, abcd, ecfgde, abcdecfgd, e


SOLUTION
a=list(str(input()))
b=list(str(input()))
c=""
d=""
lst=[]
lst1=[]
for i in a:
    if i not in c:
        c+=i
for j in b:
    if j not in d:
        d+=j
for q in c:
    for w in d:
        if q==w:
            lst.append(q)

for a in lst:
 n=(lst1.append("".join(c[:(c.index(a))])+a+d[(d.index(a)+1):]))
 m=(lst1.append("".join(d[:(d.index(a))])+a+c[(c.index(a) + 1):]))

v=sorted(lst1)
for i in v:
    print(i)
