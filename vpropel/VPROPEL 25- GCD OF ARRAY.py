QUESTION 
Find GCD b/w 2 numbers and return YES if there is gcd else print NO


SOLUTION
def find_gcd(x, y): 
      
    while(y): 
        x, y = y, x % y 
      
    return x 
          
num1=int(input())
num2=int(input())

gcd = find_gcd(num1, num2) 
  
if(gcd==1):
   print('NO')
else:
   print('YES')   
   

      
