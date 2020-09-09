"""
Name:Ansari Mohammed Ali Nasim
Date:09/09/2020
Purpose-Python Essentials-Batch 7 Day 5 Assignment 3
"""

text = 'Hello World. This is a Paragraph. This code is written in Python. Python is an interpreted language.'
capitalize = lambda sen: sen.title()
s = input('How many sentences do you want to enter(Enter only number)\n')
num = int(s)
lst = []
for i in range(num):
    sentence = input('Enter your sentence one by one\n')
    lst.append(sentence)
print(lst)
caplist = map(capitalize, lst)
mappedlist = list(caplist)
print(mappedlist)
