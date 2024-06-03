#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):return s[:5]
    # Returns a string that contains the first five characters of the argument given

def last_seven(s):return s[-7:]
    # Returns a string that contains the last seven characters of the argument given

def middle_number(n):
    n_str = str(n) 
    return n_str[1:3]
    # Place code here - refer to function specifics in section below

def first_three_last_three(s1, s2): return s1[:3] + s2[-3:]
    # Place code here - refer to function specifics in section below

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1)) 