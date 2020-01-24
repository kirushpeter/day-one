'''print ("hello world")

print("The capaybala likes to swim very fast")
#prints as its written
print ("""i am a new
 trick""")

name = input("what is your name? ")
country = input("what country do you live in? ")
country = country.upper()
print()

print(name)

firstName = input("what is your first name?")
lastName = input("what is your lastname?")
print("hello " + firstName + " " + lastName)

message = "Hello world"

print(message.lower())
print(message.upper())
#message = "Hello world"

#print(message.find("world"))
#print(message.count("o"))
#print(message.capitalize())
#print(message.replace("Hello","Hi"))
# 
'''
"""
firstname = input("what is your firstname? ")
lastname = input("what is your lastname?")
print(firstname.upper())
print(lastname.upper() """


"""area = 0
height = 10
width = 20 
#calaculates the area of a triangle.

area = width * height / 2

print("the area of the triangle would be %f" % area)"""

"""
salary = input("please enter your salary: ")

bonus = input("please enter your bonus: ")

payCheck = int(salary) + float(bonus)

print(payCheck)"""


"""
import datetime

currentDate = datetime.date.today()

print(currentDate)

print(currentDate.year)

print(currentDate.month)

print(currentDate.day)

print(currentDate.strftime("%d-%b-%Y"))
"""


"""
answer = input("would you like express shipping?")

if answer == "yes":

    print("that would be an extra $19")

print("Have a nice day")
"""
"""
# favoriteTeam = input("what is your favourite team? ")

# if favoriteTeam == "senators":
#     print("whoorayy  ")

"""
"""
freeToaster = False

deposit = int(input("how much do you want to deposit? "))

if deposit > 100:

    freeToaster = True

if freeToaster:
    print("enjoy your toaster")

print("have a nice day!")
"""
"""
shippingFree = False
totalPurchase = input("enter your total amount of purchase: ")

if totalPurchase > 50:
    shippingFree = True
    
if shippingFree:
    print("your total cost is" + totalPurchase)
    
"""
"""
country = input("Where are you from? ").upper()

if country == "CANADA":
    print("hello")
elif country == "GERMANY":
    print("hello")
elif country == "JAPAN":
    print("hello")
    """
"""
team = input("enter your favourite hockey team: ").upper()

sport = input("Enter your favourite sport: ").upper()

if sport == "Hockey" and team =="RANGERS":

    print("i miss messier")

else:
    print("I don't know that team")

"""

import matplotlib.pyplot as plt
import re
from collections import Counter, defaultdict, namedtuple, deque
from itertools   import chain, cycle, product, islice, count as count_from
from functools   import lru_cache, total_ordering
from dataclasses import dataclass

#### CONSTANTS

infinity = float('inf')
bignum   = 10 ** 100

#### FILE INPUT AND PARSING

def Input(day, line_parser=str.strip, file_template='data/advent2018/input{}.txt'):
    "For this day's input file, return a tuple of each line parsed by `line_parser`."
    return mapt(line_parser, open(file_template.format(day)))

def integers(text): 
    "A tuple of all integers in a string (ignore other characters)."
    return mapt(int, re.findall(r'-?\d+', text))

#### UTILITY FUNCTIONS

def mapt(fn, *args): 
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))

def first(iterable, default=None):
    "Return first item in iterable, or default."
    return next(iter(iterable), default)

def nth(iterable, n): return next(islice(iter(iterable), n, n+1))

cat = ''.join

def rangei(start, end, step=1):
    """Inclusive, range from start to end: rangei(a, b) = range(a, b+1)."""
    return range(start, end + 1, step) 

def quantify(iterable, pred=bool):
    "Count how many items in iterable have pred(item) true."
    return sum(map(pred, iterable))

def multimap(items):
    "Given (key, val) pairs, return {key: [val, ....], ...}."
    result = defaultdict(list)
    for (key, val) in items:
        result[key].append(val)
    return result
    