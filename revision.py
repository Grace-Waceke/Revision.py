
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

from random import shuffle
color = ["white", "black", "yellow", "blue", "red", "green"]
shuffle(color)
print(color)


