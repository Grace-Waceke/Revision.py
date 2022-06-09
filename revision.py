
def age():
    yob = int(input("Enter Year of Birth"))
    cy = int(input("Enter the Current Year"))

    new_age = cy - yob
    if new_age>18:
        return f"The person with the age of {new_age} years can vote"
    else:
        return f"The person with the age of {new_age} years cannot vote"

print(age())  



def sum_list(items):
    sum_nums = 0
    for x in items:
        sum_nums += x
        return sum_nums


print(sum_list([1,2,-8]))    


def max_num(list):
    max = list[0]
    for a in list:
        if a < max:
            max = a
            return max
print(max_num([1,2,7,-8,10,0]))


def multiply(items):
    tot = 1
    for x in items:
            tot *= x
            return tot


print(multiply([2,3,4,5,6,]))



# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
def last(n): return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)

print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))

# Write a Python program to remove duplicates from a list.
# This returns and prints in a set
a = [40,50,80,40,60,50,10,20,30,20,10]
dup_item = set()
org_item = []
for x in a:
    if x not in dup_item:
        org_item.append(x)
        dup_item.add(x)

print(dup_item)

# Write a Python program to clone or copy a list.
firstlist = [30,45,67,23,13,25,6,37]
nlist = list(firstlist)
print(firstlist)
print(nlist)


# Write a Python function that takes two lists and returns True if they have at least one common member.
def data(list1, list2):
    result = False
    for x in list1:
            for y in list2:
                if x == y:
                    result = True
                    return result
print(data([1,2,3,4,5], [5,6,7,8,9]))
print(data([1,2,3,4,5], [6,7,8,9]))

# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
color = ["red", "green", "blue", "black", "pink", "yellow"]
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

# Write a Python program to generate a 3*4*6 3D array whose each element is *.
array = [[ ["*"for col in range(6)]for col in range(4)] for row in range(3)]
print(array)

# Write a Python program to print the numbers of a specified list after removing even numbers from it.
Num = [3,5,6,12,120,25,44,35,2742,10]
Num = [x for x in Num if x%2!=0]
print(Num)

# Write a Python program to shuffle and print a specified list.
def shuffle(color):
    for x in color:
        return(color.shuffle())

print(["white", "black", "yellow", "blue", "red", "green"])

from cgitb import text
from pickletools import string1
from random import shuffle
from re import L
from unicodedata import name
color = ["white", "black", "yellow", "blue", "red", "green"]
shuffle(color)
print(color)

# Write a Python program to find the list of words that are longer than n from a given list of words.
def longest(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
            return word_len
print(longest(5, "This is the ever best day that has ever happened to me in my entire life. Trusting the process"))

# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
def values():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
        print(l[:5])
        print(l[-5:])
print (values())

list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)
# Write a Python program to convert a list of characters into a string.
b = ["a", "b", "c", "d", "e"]
string1 = "".join(b)
print(string1)

# Write a Python program to find the index of an item in a specified list.
num = [10,20,30,40,50,-26]
print(num.index(-26))

# Write a Python program to flatten a shallow list.
import itertools
origin_list = [[2,3,6], [1,4,7,8], [16], [12,14,17,19]]
new_list = list(itertools.chain(*origin_list))
print(new_list)

# Write a Python program to append a list to the second list.
lista = [34,45,67,89,90]
listb = ["Mary", "Waceke", "Maimbo", "Dylan", "Tamara"]
new_list =lista + listb
print(new_list)

# Write a Python program to append a list to the second list.
listx = ["Mary", "Waceke", "Maimbo", "Dylan", "Tamara"]
print(listx[2])

import random
listx = ["Mary", "Waceke", "Maimbo", "Dylan", "Tamara"]
print(random.choice(listx))

x = range(1,11)
for n in x:
    sum = n +(n-1)
    print(f"current figure is {n}, and the previous figure is {n-1}, and the sum is {sum}")

    # write a python program that prints the least number in a list without using any python inbuilt function
    list = [30,24,90,60,45,67,89]
    smallest = 0
    for x in list:
        if x < smallest:
            smallest = x
print (smallest)
