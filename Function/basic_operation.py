#Basic mathematical operation using user defined function
#defining functions
def add(num1,num2):
    return num1+num2

def subr(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def divi(num1,num2):
    return num1/num2

#implimenting the functions
print("Enter two numbers(int) : ")
n1 = int(input())
n2 = int(input())
print('Addition of {} & {} is = '.format(n1,n2),add(n1,n2))
print('Subtraction of {} & {} is = '.format(n1,n2),subr(n1,n2))
print('Multiplication of {} & {} is = '.format(n1,n2),mult(n1,n2))
print('Division of {} & {} is = '.format(n1,n2),divi(n1,n2))

#Format operator is used for appending strings within a string