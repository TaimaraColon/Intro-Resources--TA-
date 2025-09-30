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

Goal: Given the number of occurance to look for, a list and an item, find the index of that item.

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
        middle = int(len(nums_list)//2)
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

'''
Remove Duplicates

Description
Given an integer list nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the list nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.

Return k.

Examples
remove_duplicates([1,1,2]) → 2, nums = [1,2,_]

It does not matter what you leave beyond the returned k (hence they are underscores).

remove_duplicates([0,0,1,1,1,2,2,3,3,4]) → 5, nums = [0,1,2,3,4,_,_,_,_,_]

Constraints
1 <= nums.length <= 3 * 104

-100 <= nums[i] <= 100

nums is sorted in non-decreasing order.

Source
https://leetcode.com/problems/remove-duplicates-from-sorted-array/ 
'''
def remove_duplicates(nums):
    # Write your code here
    return -1

'''Solution'''
def remove_duplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i+1

'''Tests'''
print(remove_duplicates([1,1,2]))               # 2
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4])) # 5 
print(remove_duplicates([3,3,4,4,5,6,7,8]))     # 6

'''
Maximum Difference

Description
Given a list of numbers, find the difference between the largest and the smallest (the maximum difference).

Examples
max_diff([7, 1, 8, 8, 9]) → 8

max_diff([1, 1, 1]) → 0

Source
Googler: Donnell Debnam Jr., ddebnam@google.com
'''
def max_diff(nums):
    # Write your code here 
    return -1

'''Solution'''
def max_diff(nums):
    smallest = nums[0]
    biggest = nums[0]
    for item in nums:
        smallest = min(smallest, item)
        biggest = max(biggest, item)
    return biggest - smallest

'''Tests'''
print(max_diff([7, 1, 8, 8, 9]))          # 8
print(max_diff([14, 90, 14, 3, 3, 7, 9])) # 87
print(max_diff([1, 1, 1]))                # 0

'''
Sum First Col

Write a function named sum_first_col that takes a 2D list of numbers as an argument, and returns the sum of all the elements in the first column.

Examples:

sum_first_col([[1, 2, 3], [4, 5, 6]]) returns 5

sum_first_col([[10], [20], [30]]) returns 60

sum_first_col([[], [], []]) returns 0

Hint: Create a variable (e.g. total) to keep track of the sum of each element.
      Remember to update total by adding the first item of each row.
'''
def sum_first_col(grid):
  # write your code here
  return -1
'''Solution'''
def sum_first_col(grid):
  total = 0
  for row in grid:
    if len(row) > 0:
      total = total + row[0]
  return total

'''Tests'''
print(sum_first_col([[1, 2, 3], [4, 5, 6]])) # 5
print(sum_first_col([[10], [20], [30]]))     # 60
print(sum_first_col([[], [], []]))           # 0

'''


Write a function named duck_duck_goose that takes a 2D list of strings as an argument.

This 2D list will contain lists of strings that represent many different kinds of animals, but you only care about 'duck' and 'goose'. Count the number of times the string 'duck' or 'goose' appears.

Examples:

duck_duck_goose([['dog', 'mouse', 'cDuck Duck Gooseat'], ['eel', 'fish', 'mongoose']]) returns 0

duck_duck_goose([['duck', 'cat', 'duck'], ['duck', 'goose', 'sheep']]) returns 4

duck_duck_goose([['duck', 'duck', 'duck'], ['duck', 'goose', 'goose']]) returns 6
'''
def duck_duck_goose(grid):
    # write your code here
    return -1
'''Solution'''
def duck_duck_goose(grid):
    total = 0
    for row in grid:
        for val in row:
            if val == 'duck' or val == 'goose':
                total += 1
    return total

'''Tests'''
print(duck_duck_goose([['dog', 'mouse', 'cat'], ['eel', 'fish', 'mongoose']]))  # 0
print(duck_duck_goose([['duck', 'cat', 'duck'], ['duck', 'goose', 'sheep']]))   # 4
print(duck_duck_goose([['duck', 'duck', 'duck'], ['duck', 'goose', 'goose']]))  # 6
