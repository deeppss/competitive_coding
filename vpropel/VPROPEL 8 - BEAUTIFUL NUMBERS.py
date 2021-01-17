QUESTION
Beautiful Numbers
A sequence of numbers is called cute if all the numbers in the sequence are made of only two digits, 8 and 9.
Example of a cute sequence is: 8, 9, 88, 89, 98, 99…. and so on.
A number is called beautiful if it is divisible by any number which is part of the cute sequence.
For example: 8 (divisible by 8), 9(divisible by 9), 889 (divisible by 889),  10668 (divisible by 889) are beautiful numbers. Given a number, n, write a code to print “beautiful” (without quotes) if it is divisible by any number that contains only 8 or 9 or both and print -1 otherwise.

Input Format:
Input contains one single line denoting the number, n

Output Format:
Print "beautiful" if the number is a beautiful number and -1 otherwise

Constraints:
1 <= N <= 999999999999999999

SOLUTION
arr =[0] * 1000000
arr[1] = 8
arr[2] = 9
lst1=[]
lst2=[]
for i in range(3, 100000):
        if (i % 2 != 0):
            arr[i] = arr[i // 2] * 10 + 8
            lst1.append(arr[i])
        else:
            arr[i] = arr[(i // 2) - 1] * 10 + 9
            lst2.append(arr[i])
n=int(input())
c=0
k=lst1+lst2
k.append(9)
for i in k:
    if(n%i==0):
        print("beautiful")
        c+=1
        break
    else:
        pass
if(c==0):
    print("-1")
