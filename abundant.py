
# Abundant number check
#Mathematically we can describe abundant number as given below:

# if D(i)are the proper divisors (excluding N itself) of a numberNand sum of all proper divisorsD(1) + D(2) + D(3) + …. = Tis greater than numberNi.e.(T>N)thenNis said to be an abundant number.

# So, in number theory, anabundant numberis a number that is smaller than the sum of its proper divisors.

# For example, if the integerNis12and Its proper divisors areD(1)=1, D(2)=2, D(3)=3, D(4)=4andD(5)=6for a totalTof16and16is greater than12that isT>NsoN=12is an Abundant Number.

# Your task is to write a program that accepts a numberNand check whetherNis an Abundant number or not. IfNis anabundant numberprint1in output and ifNisnot an abundant numberprint0in output.
num=4
n=1
sum=0

while n <num:
    if num%n==0:
        print(n)
        sum=sum+n
    n=n+1
    
if sum>num:
    print('The number is abundant',num)
else:
    print('The number is not abundant',num)