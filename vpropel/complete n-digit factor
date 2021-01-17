QUESTION
--------
A number is said to be a complete ‘n’ digit factor, if it is a factor of all ‘n’ digit numbers when concatenated (joined to right) to itself.
For example, 7 is a complete 3-digit factor as it divides all three digit numbers from 100 to 999 when concatenated to itself (i.e. 100100, 101101,102102, ... ..., 998998, 999999).
Given the value of n and m, write a code to generate all numbers from 2 to m (both inclusive) that are complete n-digit factor and print ‘No complete factors’ otherwise.
For example, if n is 3 and m is 15 then print 7, 11, 13 and if n is 3 and m is then print ‘No complete factors’
Boundary Conditions: 2<n<9
Note: The code needs to optimized to complete execution within the time bound given for the problem

Input Format
First line contain the number of digits, n
Next line contains the maximum value of m that has to be checked for Complete n-Digit Factor
 
Output Format
Print each Complete n-Digit Factor in one line and print No complete factors otherwise


SOLUTION
---------
n=int(input()) #no. of digits
m=int(input()) #upto what number we want to check divibility
f=pow(10,n-1) #lower limit
g=pow(10,n)-1 #upper limit
lst=[]
for j in range(2,m): 
    d=0 
    for i in range(f,g):
        i = str(i) * 2  #to concatenate the integer twice
        i=int(i)   #type conversion to divide the number
        if(i%j==0):  #dividing the n digit number by a number from 2-m
            d+=1     #each time a number is divisible by the n digit number, it increments.
            if(d==g-f-1):   #this is to check whether that number is divisble by all numbers in the given range
                print(j)    #if it meets the above condition, it would be incremented to a list
                lst.append(j)
                break
            else:
                pass
        else:      #if the number is not divisble with the n digit number, then it breaks from the loop, we don't need to check for the rest of the numbers
            break
if(len(lst)==0):  #if the list is empty there are no factors
    print("No complete factors")
