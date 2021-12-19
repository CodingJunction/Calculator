#calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def exp(a,b):
    return a**b
    
print('''
 _____________________
|  _________________  |
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')
ans=0
condition=True
function={"+":add,"-":sub,"x":mult,"/":div,"%":mod,"**":exp}
print('Welcome to the calculator')
num1=float(input('Enter first number\n'))
while condition:
    print('''Enter the operation which you want to perform
+
-
x
/
%
**''')
    op=input()
    num2=float(input('Enter next number\n'))
    ans=function[op](num1,num2) 
    print('Answer is',ans)
    print('''Do you want to continue with calculation?
Enter 'yes' for yes
Enter 'no' for no''')
    c=input()
    if c=="yes":
        condition=True
        num1=ans
    else:
        condition=False
