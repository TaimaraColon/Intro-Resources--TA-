'''LISTS PRACTICE'''

'''
Fruit Hunt!

Goal: Given a list, return the position of a specific item.

Task: You are given as parameter of the function a list that represent a fruit basket and a fruit. 
Find the position of a specific fruit in the list. If there are more than one, return the first position.
If the fruit is not in the basket return "There is no {fruit} in the basket", where {fruit} is the specific fruit we couldn't find.
'''
def find_fruit(fruit_basket, fruit):
    # write your code here
    return -1

'''Solution'''
def find_fruit(fruit_basket, fruit):
    for i in range(len(fruit_basket)):
        if fruit_basket[i]==fruit:
            return i
    return f"There is no {fruit} in the basket."

'''Tests'''
print(find_fruit(['orange', 'apple', 'kiwi', 'banana', 'grape', 'mango'], 'mango'))      # 5
print(find_fruit(['orange', 'kiwi', 'kiwi', 'banana', 'mango'], 'kiwi'))                 # 1
print(find_fruit(['mango', 'apple', 'kiwi', 'banana', 'grape', 'strawberry'], 'orange')) # There is no orange in the basket.

'''
Move Item To The End

Goal: Use list methods to move an item from one place to the last place in the same list.

Task: You are given a list of items and a specific item. Your job is to move said item to the end of the list.
If the item is not in the list return this message: "{item} not in the list"

Example:
flowers_list = [rose, lily, peony, daisy, tulip, orchid]

item = peony

Output = [rose, lily, daisy, tulip, orchid, peony]

Hint: Use list methods.

'''
def move_flower_to_the_end(flower_list, flower):
    # write your code here
    return -1

'''Solution'''
def move_flower_to_the_end(flower_list, flower):
    if flower not in flower_list:
        return f"{flower} is not in the list"
    
    for i in range(len(flower_list)):
        if flower == flower_list[i]:
            flower_list.append(flower_list.pop(i))
    return flower_list

'''Tests'''
print(move_flower_to_the_end(['rose', 'lily', 'peony', 'daisy', 'tulip', 'orchid'],'peony')) # ['rose', 'lily', 'daisy', 'tulip', 'orchid', 'peony']
print(move_flower_to_the_end(['tulip', 'lily', 'peony', 'daisy', 'rose', 'orchid'],'tulip')) # ['lily', 'peony', 'daisy', 'rose', 'orchid', 'tulip']
print(move_flower_to_the_end(['rose', 'lily', 'peony'],'daisy'))                             # daisy is not in the list

'''
Find Position

Goal: GIven the number of occurance to look for, a list and an item, find the index of that item.

Task: Return the index of the x-th occurrence of a specific course in a list of courses. If it doesn't occur x times, return -1.

Example:

course_list = ['CIIC3015','MATE3173','QUIM3131','FISI3171','CIIC3015','BIOL3061']
course = 'CIIC3015'
x = 2

Output: 4
Because the position of the 2nd instance of CIIC3015 is in position 4.

'''
def find_position(courses_list, course, x):
    # Write your code here
    return -1

'''Solution'''
def find_position(courses_list, course, x):
    count_instances = 0
    for i in range(len(courses_list)):
        if courses_list[i] == course:
            count_instances +=1
        if count_instances == x:
            return i
    
    return -1

'''Tests'''
items = ["a", "b", "c", "a", "b", "a"]
print(find_position(items, "a", 2))  #  3
print(find_position(items, "b", 1))  #  1
print(find_position(items, "a", 4))  # -1

'''
Add to list

Task: Write a function named add_to_list that takes in two arguments.

argument 1: A list containing 1, 2,  3, 4

argument 2: An integer

If argument 2 is greater than 0, add it to the end of the list. 
If it is less than 0, add it to the beginning of the list. 
If it is equal to 0, add it to the middle of the list (between the 2 and the 3). 

Examples:

add_to_list([1, 2, 3, 4], 7) returns [1, 2, 3, 4, 7]

add_to_list([1, 2, 3, 4], -20) returns [-20, 1, 2, 3, 4]

add_to_list([1, 2, 3, 4], 0) returns [1, 2, 0, 3, 4]

Hint: Use list methods.

'''
def add_to_list(nums_list, num):
    # write your code here

    return -1

'''Solution'''
def add_to_list(nums_list, num):
    if num > 0:
        nums_list.append(num)
    if num < 0: 
        nums_list.insert(0, num)
    if num == 0:
        middle = int(len(nums_list)/2)
        nums_list.insert(middle, num)
    return nums_list

print(add_to_list([1, 2, 3, 4], 7))   # [1, 2, 3, 4, 7]
print(add_to_list([1, 2, 3, 4], -20)) # [-20, 1, 2, 3, 4]
print(add_to_list([1, 2, 3, 4], 0))   # [1, 2, 0, 3, 4]


'''
Reverse list

Goal: Reverse a list.

Task: Given a list of ints length 3, return a new list with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

Examples:

reverse([1, 2, 3]) returns [3, 2, 1]
reverse([5, 11, 9]) returns [9, 11, 5]
reverse([7, 0, 0]) returns [0, 0, 7]

Hint: Remember the beginning, end, and step in a for loop.

'''
def reverse(nums):
    # write your code here
    return -1

'''Solution'''
def reverse(nums):
    new_list = []
    for i in range(len(nums)-1,-1, -1):
        new_list.append(nums[i])
    return new_list

print(reverse([1, 2, 3]))  # [3, 2, 1]
print(reverse([5, 11, 9])) # [9, 11, 5]
print(reverse([7, 0, 0]))  # [0, 0, 7]

'''
Is Sorted

Goal: Write a program that says if a list is sorted or not.

Task: Write a function called isSorted() which takes a list as a parameter and returns True if all of the elements in that list are in sorted order, 
False if they are not. The elements in the list may be of any type. Two sequential values (a,b) are defined to be in sorted order if and only if a <= b. 
Empty lists, or lists with only a single element, are considered to be sorted by definition.

'''
def isSorted(items):
    # Write your code here
    return 0

'''Solution'''
def isSorted(items):
    if len(items) > 0:
        prev = items[0]
        for item in items:
            if prev > item:
                return False
            prev = item
    return True

print(isSorted([2,3,4,5,1]))  # False
print(isSorted([0,1,2,3,4]))  # True
print(isSorted([1,2,3,5,4]))  # False
'''
Dot Product

The dot product of two vectors is calculated by multiplying the corresponding elements of each vector together and summing those products. 

Task: Write a function called dotProduct() which takes two lists as arguments and returns the dot product of those lists as a float. 
You may assume that both lists have equal length and contain only numeric values.

Example:
The dot product of [2, 0, 1] and [6, 3, 4] = 2*6 + 0*3 + 1*4 = 12 + 0 + 4 = 16

Note: We want you to roll your own loops here. Do not import a module like numpy to do the work for you.

'''
def dotProduct(a,b):
    # Write your code here
    return -1

'''Solution'''
def dotProduct(a,b):
    out,i = 0.0,0
    while i < len(a):
        out += a[i]*b[i]
        i += 1
    return out

print(dotProduct([2,0,1], [6,3,4])) # 16.0
print(dotProduct([6,3,4], [2,0,1])) # 16.0
print(dotProduct([1,2,3], [4,5,6])) # 32.0