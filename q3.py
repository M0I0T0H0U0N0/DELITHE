# Check if a number is prime or not
def isPrime(num):
    if num == 0 or num == 1 or num ==2:
        return True
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    return True

# To generate all prime no from one to n
def generatePrime(r1,r2):
    for i in range(r1, r2+1):
        flag = 0
        for j in range(2, int(i/2)+1):
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            print(i)

# To check if a number is a strong number or not
# 
def factorial(num):
    if num ==1 or num==0:
        return 1
    return num * factorial(num-1)

def strongNumber(num):
    # The sum of factorial of individual digits is equal to the number itself
    num = str(num)
    sum = 0
    for i in range(len(num)):
        sum+=factorial(int(num[i]))
    
    if(sum == int(num)):
        return True
    else:
        return False

# To check if a no is armstrong no or not
def isArmstrong(num):
    temp = num
    sum = 0
    count = len(str(num))
    while num:
        digit = num%10
        sum+=digit**count
        num = num//10
    if temp == sum:
        return True
    return False

# Happy no or not
def isHappyNumber(num):
    iter = 1
    while num>1 and iter<100:
        sum = 0
        while num:
            digit = num%10
            sum+=digit**2
            num = num//10
        num = sum
        iter+=1
    if iter>=100:
        return False
    return True

# Neon No or not
def isNeonNumber(num):
    square = num ** 2
    sum = 0
    while square:
        digit = square % 10
        sum+=digit
        square = square//10
    if sum == num:
        return True
    return False

# Spy number or not
def isSpy(num):
    temp = num
    sum = 0
    product = 1
    while num:
        digit = num % 10
        sum += digit
        product*=digit
        num = num // 10
    if product == sum:
        return True
    return False

# Program to generate the fibonauci series and fib no 
def fibNo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibNo(num-1)+fibNo(num-2)

def generateFibSeries(num):
    for i in range(num):
        print(fibNo(i))

 
# Convert a no from negative to positive

def convertToPositive(num):
    return -abs(num)

# Program to check palindrome or not for a number
def isPalindrome(num):
    temp = num
    rev = 0
    while num:
        digit = num % 10
        rev =rev + digit * 10**(len(str(num))-1)
        num = num // 10
    print(rev)
    if temp == rev:
        return True
    return False
        
# Display the multiplication table
def printMultiplicationTable(r1,r2):
    for j in range(r1,r2+1):
        for i in range(1,11):
            print(j*i)
        print()
           
# Display the year

num = int(input())
r1 = int(input("range 1:"))
r2 = int(input("range 2:"))
# print(isPrime(num))
# generatePrime(r1,r2)
# print(strongNumber(num))
# print(isArmstrong(num))
# print(isHappyNumber(num))
# print(isNeonNumber(num))
# print(isSpy(num))
# generateFibSeries(num)
# print(isPalindrome(num))
printMultiplicationTable(r1,r2)



