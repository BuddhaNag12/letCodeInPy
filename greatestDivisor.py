# Given program checks for greatest divisor of a given number

def isPrime(number):
    len=number/2
    i=2
    flag=0
    while i<len:
        if number%i==0:
            flag=1
            break
        i=i+1
    if number==1:
        return False
    else:
        if flag==0:
            return True
        else:
            return False
            
def main():
   print("Enter a number :-")
   num = int(input())
   greatest = 0
   i = 1
   if isPrime(num):
       print("-1")
   else:
       while i<num:
           if num%i==0 and num != i:
               if greatest<i:
                     greatest=i
           i+=1 
       print(greatest)
               
   
    
if __name__=='__main__':
    main()