#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator support supports PEMDAS
"""
import re

def operate(num1,op,num2):
    num1 = float(num1)
    num2 = float(num2)
    if op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    elif op == '+':
        return num1 + num2 
    elif op == '-':
        return num1 - num2 
    elif op == '**':
        return num1**num2
    
    
def exponent(exp):
    tot = 0
    while '**' in exp:
        for i, x in enumerate(exp):
            if x in['**']:
                tot += operate(exp[i-1],exp[i],exp[i+1])
                del exp[i-1:i+2]
                exp.insert(i -1,tot)
                tot = 0
                break
    return(exp)

def mul_or_div(exp):
    tot = 0
    while '*' in exp or '/' in exp:
        for i, x in enumerate(exp):
            if x in['*','/']:
                tot += operate(exp[i-1],exp[i],exp[i+1])
                del exp[i-1:i+2]
                exp.insert(i -1,tot)
                tot = 0
                break
    return(exp)

def add_or_sub(exp):
    tot = 0
    while '+' in exp or '-' in exp:
        for i, x in enumerate(exp):
            if x in['+','-']:
                tot += operate(exp[i-1],exp[i],exp[i+1])
                del exp[i-1:i+2]
                exp.insert(i -1,tot)
                tot = 0
    return(exp)



def paren(exp):
    while '(' in exp:
        st =  len(exp) - 1 - exp[::-1].index('(')
        en = st + exp[st:].index(')')
        inside = exponent(exp[st+ 1:en])
        inside = mul_or_div(inside)
        inside = add_or_sub(inside)
        exp.insert(st,inside[0])
        del exp[st + 1:en + 2]
    return exp  
        

eq = input("enter equation: ")
match = re.findall('\*\*|[-+][\d]+|[0-9]+|[-()+/\*]',eq)
print("Initial input")
print(match)
eq = paren(match)
print("After paren: ")
print(eq)
eq = exponent(eq)
print("After exponent: ")
print(eq)
eq = mul_or_div(eq)
print("After mult/div")
print(eq)
eq = add_or_sub(match)
print("After add/sub")
print(eq)




