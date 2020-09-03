"""
Name:Ansari Mohammed Ali Nasim
Date:03/09/2020
Purpose-Python Essentials-Batch 7 Day 2 Assignment
"""

# Questions 1
# List and its default functions.

lst = ['apple', 'banana', 'cherry']
# 1)append
x = lst.append('orange')
print(x)
# 2)copy
fruits = lst.copy()
print(fruits)
# 3)pop
fruits.pop(0)
print(fruits)
# 4)insert
fruits.insert(0, 'apple')
print(fruits)
# 5)reverse
fruits.reverse()
print(fruits)

# Questions 2
# Dictionary and its default functions.

dit = {'red': 'apple', 'yellow': 'banana', 'red-dotted': 'cherry'}
# 1)get
a = dit.get('red')
print(a)
# 2)keys
b = dit.keys()
print(b)
# 3)update
dit.update({"white": "lychee"})
print(dit)
# 4)values
c = dit.values()
print(c)
# 5)pop
dit.pop('red-dotted')
print(dit)


# Questions 3
# Sets and its default functions

st = {"apple", "banana", "cherry"}
# 1)add-for one item
st.add("orange")
print(st)
# 2)update-for multiple item
st.update(["watermelon", "mango", "grapes"])
print(st)
# 3)remove
st.remove('watermelon')
print(st)
# 4)discard-same as remove
st.discard('banana')
print(st)
# 5)pop-removes last item
d = st.pop()
print(d)


# Questions 4
# Tuple and explore default methods.
t1 = ("a", "b", "c")
t2 = (1, 2, 3)
# 1)join two tuples
t = t1 + t2
print(t)
# 2)count
e = t.count('a')
print(e)
# 3)index-search the 1st occurence
f = t.index(1)
print(f)
# 4)slicing
s = t[2:5]
print(s)
# 5)reverse slicing
rs = t[-4:-1]
print(rs)


# Questions 5
# Strings and explore default methods.
stings = "Hello,My name is Ansari Mohammed Ali Nasim"
# 1)casefolds-covert into lower case
cf = stings.casefold()
print(cf)
# 2)count- count the occurence
ct = stings.count("a")
print(ct)
# 3)islower-true if all character is lower
al = cf.islower()
print(al)
# 4)replace
re = stings.replace("My name is", "Myself")
print(re)
# 5)upper-covert into upper case
up = stings.upper()
print(up)
