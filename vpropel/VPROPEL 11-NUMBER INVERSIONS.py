QUESTIONS
Number inversions
Rahul is facing a unique problem, which he doesn't know how to solve. The problem asks him to build the smallest possible number by applying inversion on any digit of the number any number of times.
Inversion of a digit is defined as that digit being replaced by 9 minus that digit. Meaning that inversion of 9 will be 9 - 9 = 0 and inversion of 1 will be 9 - 1 = 8 and so on.

The final output should not have any leading zeroes.

Input Format:
The only line of the input contains an integer N

Output Format:
Print only one single integer on a line as described above.

Constraints:
1 <= N <= 10^18

Examples:
Input:
87
Output:
12

Explanation:
9-8 = 1
and 9 -7 = 2
if we see carefully, 12 is the smallest possible number we can get.
 

Example:
Input:
99
Output:
90

Explanation:
In this case, we do not replace the first 9 since it will lead to a leading zero.


SOLUTION
n=list(str(input()))
c=0
l=''
for i in n:
    i=int(i)
    if(c==0 and 9-i==0):
        i=str(i)
        l+=i
        c+=1
    else:
        k=9-i
        if(k<i):
            k=str(k)
            l+=k
            c+=1
        else:
            i=str(i)
            l+=i
            c+=1
print(l)



