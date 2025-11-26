'''EXERCISE - COUNT ELEMENT'''
'''
Write a function count_element_recursive(nums, to_search) that returns the number of times that integer to_search appears in list of integers nums recursively.

Examples:

count_element([1,2,2,3,4,2], 2) =  3 (2 appears 3 times in the list)

count_element([], 2) = 0 (2 does not appear in the list)
'''
def count_element_recursive(nums, to_search):
    # YOUR CODE HERE
    return -1

'''SOLUTION'''
def count_element_recursive(nums, to_search):
    if len(nums) == 0:
        return 0
    if nums[0] == to_search:
        return 1 + count_element_recursive(nums[1:], to_search)
    return count_element_recursive(nums[1:], to_search)

'''TESTS'''
print('----- TESTS: COUNT ELEMENT RECURSIVE -----')
print(count_element_recursive([1,2,2,3,4,2], 2))                    # Output: 3
print(count_element_recursive([], 2))                               # Output: 0
print(count_element_recursive([1], 1))                              # Output: 1
print(count_element_recursive([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 3))   # Output: 10

'''EXERCISE - LAST CONSONANT'''
'''
Write a function last_consonant_recursive(s) that takes a string s and returns the last consonant in the string using RECURSION. If the string contains no consonants, the function must return the value None.

Examples:

last_consonant_recursive('') returns None
last_consonant_recursive('aeiou') returns None
last_consonant_recursive("help") returns 'p'
'''
def last_consonant_recursive(s):
    # YOUR CODE HERE
    return ''

'''SOLUTION'''
def last_consonant_recursive(s):
    if len(s) == 0:
        return None
    if not s[-1].lower() in 'aeiou':
        return s[-1]
    return last_consonant_recursive(s[:-1])

'''TESTS'''
print('----- TESTS: LAST CONSONANT RECURSIVE -----')
print(last_consonant_recursive(""))         # Output: None
print(last_consonant_recursive("aeiou"))    # Output: None
print(last_consonant_recursive("help"))     # Output: p
print(last_consonant_recursive("Halo"))     # Output: l
print(last_consonant_recursive("Bienve"))   # Output: v

'''EXERCISE - REVERSE STRING RECURSIVELY'''
'''
Write a function recursive_reverse_a_string(string) that reverses a given string  recursively.

Examples:

recursive_reverse_a_string("hello") returns "olleh"

recursive_reverse_a_string("kayak") returns "kayak"
'''
def recursive_reverse_a_string(string):
    # YOUR CODE HERE
    return ''

'''SOLUTION'''
def recursive_reverse_a_string(string):
    if len(string) == 0:
        return ''
    return recursive_reverse_a_string(string[1:]) + string[0]

'''TESTS'''
print('----- TESTS: REVERSE A STRING RECURSIVELY -----')
print(recursive_reverse_a_string(""))           # Output: 
print(recursive_reverse_a_string("olleh"))      # Output: hello
print(recursive_reverse_a_string("a"))          # Output: a
print(recursive_reverse_a_string("kayak"))      # Output: kayak
print(recursive_reverse_a_string("esrever"))    # Output: reverse
print(recursive_reverse_a_string("gfedcba"))    # Output: abcdefg

'''EXERCISE - LARGEST INTEGER'''
'''
Write a function recursive_largest_number_of_a_list(nums) that finds the largest number in a given list of integers recursively. You can assume the list will have at least one integer.

Examples:

recursive_largest_number_of_a_list([10, 100, 5, 9]) returns 100

recursive_largest_number_of_a_list([-10, -100, -5, -9]) returns -5
'''
def largest_number_of_a_list_recursive(nums):
    # YOUR CODE HERE
    return -1

'''SOLUTION'''
def largest_number_of_a_list_recursive(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return nums[0]
        else:
            return nums[1]
    largest_first_two = largest_number_of_a_list_recursive(nums[:2])
    largest_remaining = largest_number_of_a_list_recursive(nums[2:])
    if largest_first_two > largest_remaining:
        return largest_first_two
    else:
        return largest_remaining
    
'''TESTS'''
print('----- TESTS: LARGEST INTEGER -----')
print(largest_number_of_a_list_recursive([1,10,9,8,2,3]))       # Output: 10
print(largest_number_of_a_list_recursive([10, 20, 5, 40, 15]))  # Output: 40
print(largest_number_of_a_list_recursive([5]))                  # Output: 5
print(largest_number_of_a_list_recursive([1,8]))                # Output: 8
print(largest_number_of_a_list_recursive([-1, -5, -3]))         # Output: -1
print(largest_number_of_a_list_recursive([10,90,1]))            # Output: 90

'''EXERCISE - ADD NUMBERS TO LIST'''
'''
Write a function add_nums_to_list_recursive(n) that returns a list with numbers 0 through n-1 recursively. Feel free to use auxiliary functions if needed. Assume non-negative inputs.

Example:

Input: n = 5
Output: [0,1,2,3,4]
'''
def add_nums_recursive(n):
    # YOUR CODE HERE
    return -1

'''SOLUTION'''
def aux(i, n, nums):
    if i == n:
        return
    nums.append(i)
    aux(i+1, n, nums) 

def add_nums_recursive(n):
    nums = []
    aux(0, n, nums)
    return nums

'''TESTS'''
print('----- TESTS: ADD NUMBERS TO LIST -----')
print(add_nums_recursive(0))    # Output: []
print(add_nums_recursive(1))    # Output: [0]
print(add_nums_recursive(5))    # Output: [0,1,2,3,4]
print(add_nums_recursive(10))   # Output: [0,1,2,3,4,5,6,7,8,9]
print(add_nums_recursive(25))   # Output: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

'''EXERCISE - POWER FUNCTION'''
'''
Write a recursive function called power_function_recursive(base, exponent) that calculates the power of a number. The function should take two arguments:

base: The base number.

exponent: The exponent to which the base is raised.

The function should return the result of base raised to the power of exponent calculated recursively.

Example:

power_function_recursive(2, 4) = 2 * 2 * 2 * 2 = 16
'''
def power_function_recursive(base, exponent):
    # YOUR CODE HERE
    return -1

'''SOLUTION'''
def power_function_recursive(base, exponent):
    if exponent == 0:
        return 1
    return base * power_function_recursive(base, exponent-1)

'''TESTS'''
print('----- TESTS: POWER FUNCTION -----')
print(power_function_recursive(2,0))    # Output: 1
print(power_function_recursive(2,10))   # Output: 1024
print(power_function_recursive(3,4))    # Output: 81
print(power_function_recursive(10,2))   # Output: 100
print(power_function_recursive(2,5))    # Output: 32
print(power_function_recursive(1,1))    # Output: 1
print(power_function_recursive(2,4))    # Output: 16

'''EXERCISE - PALINDROME'''
'''
A palindrome is a word, phrase, number, or other sequence of characters that reads the same backward as forward (ignoring spaces, punctuation, and capitalization)

Write a recursive function recursive_is_palindrome(word) that takes a string as input and determines if it is a palindrome.

Examples:

recursive_is_palindrome("racecar") returns True

recursive_is_palindrome("Hello") returns False
'''
def is_palindrome_recursive(word):
    # YOUR CODE HERE
    return ''

'''SOLUTION'''
def is_palindrome_recursive(word):
    if len(word) <= 1:
        return True
    return word[0] == word[-1] and is_palindrome_recursive(word[1:-1])

'''TESTS'''
print('----- TESTS: PALINDROME -----')
print(is_palindrome_recursive("racecar"))   # Output: True
print(is_palindrome_recursive("hello"))     # Output: False
print(is_palindrome_recursive("Madeline"))  # Output: False
print(is_palindrome_recursive("a"))         # Output: True
print(is_palindrome_recursive(""))          # Output: True

'''EXERCISE - DOT PRODUCT'''
'''
Write a function dot_product_recursive(nums_1, nums_2) that calculates the dot product of two lists of integers nums_1 and nums_2 recursively. The dot product of two lists is calculated by multiplying the corresponding elements of both lists and then adding those products. You can assume that both lists have the same length.

Example:

dot_product_recursive([1, 2, 3], [4, 5, 6]) = (1*4) + (2*5) + (3*6) = 32
'''
def dot_product_recursive(nums_1, nums_2):
    # YOUR CODE HERE
    return -1

'''SOLUTION'''
def dot_product_recursive(nums_1, nums_2):
    if len(nums_1) == 0:
        return 0
    return nums_1[0] * nums_2[0] + dot_product_recursive(nums_1[1:],nums_2[1:])

'''TESTS'''
print('----- TESTS: DOT PRODUCT -----')
print(dot_product_recursive([1,0,2,0,3,0],[0,1,0,2,1,3]))   # Output: 3
print(dot_product_recursive([1,2,3],[1,1,1]))               # Output: 6
print(dot_product_recursive([],[]))                         # Output: 0
print(dot_product_recursive([-3],[2]))                      # Output: -6
print(dot_product_recursive([1,0,2,0,3,1],[0,1,0,2,1,4]))   # Output: 7

'''EXERCISE - ACKERMANN'S FUNCTION'''
'''
Ackermann’s Function is a recursive mathematical algorithm that can be used to test how well a system optimizes its performance of recursion. White a function ackermann(m, n), which solves Ackermann’s function. Use the following logic in your function:

If m = 0 then return n + 1
If n = 0 then return ackermann(m - 1, 1)
Otherwise, return ackermann(m - 1, ackermann(m, n - 1))

Examples:

ackermann(0, 0) = 1

ackermann(1, 1) = 3
'''
def ackermann(m, n):
    # YOUR CODE HERE
    return -1

'''SOLUTION'''
def ackermann(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))

'''TESTS'''
print("----- TESTS: ACKERMANN'S FUNCTION -----")
print(ackermann(0, 0)) # Output: 1
print(ackermann(1, 1)) # Output: 3
print(ackermann(2, 2)) # Output: 7
print(ackermann(3, 4)) # Output: 125

'''EXERCISE - HARMONIC SUM'''
'''
Write a  function harmonic_sum_recursve(n) that,  given an int n greater or equal to zero, computes the harmonic sum H(n). H(n) is
defined as the sum of the reciprocals of the numbers from 1 to n.

That is, the formula is:

H(0) = 0
H(1) = 1
H(n) = 1 + 1/2 + 1/3 + 1/4 ... + 1/n for n > 1

After calculating the harmonic sum, the result must be rounded to two decimal places using the round() function.

Examples:

harmonic_sum_recursve(0) = 0

harmonic_sum_recursve(4) = 2.08

harmonic_sum_recursve(3) = 1.83
'''
def harmonic_sum_recursive(n):
    # YOUR CODE HERE
    return -1

'''SOLUTION'''
def harmonic_sum_recursive(n):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  else:
    return round((1 / n) + (harmonic_sum_recursive(n - 1)), 2)
  
'''TESTS'''
print("----- TESTS: HARMONIC SUM -----")
print(harmonic_sum_recursive(0)) # Output: 0
print(harmonic_sum_recursive(1)) # Output: 1
print(harmonic_sum_recursive(2)) # Output: 1.5
print(harmonic_sum_recursive(3)) # Output: 1.83
print(harmonic_sum_recursive(4)) # Output: 2.08
print(harmonic_sum_recursive(5)) # Output: 2.28

'''EXERCISE - CHANGE X TO Y'''
'''
Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.

change_x_y("codex") → "codey"
change_x_y("xxhixx") → "yyhiyy"
change_x_y("xhixhix") → "yhiyhiy"
'''
def change_x_y(word):
    # YOUR CODE HERE
    return ''

'''SOLUTION'''
def change_x_y(word):
    if len(word) == 0:
        return word
    character = word[0]
    if character == 'x':
        character = 'y'
    return character + change_x_y(word[1:])

'''TESTS'''
print("----- TESTS: CHANGE X TO Y -----")
print(change_x_y("codex"))      # Output: codey
print(change_x_y("xxhixx"))     # Output: yyhiyy
print(change_x_y("xhixhix"))    # Output: yhiyhiy
print(change_x_y("x"))          # Output: y
print(change_x_y("code"))       # Output: code
print(change_x_y(""))           # Output: 

'''EXERCISE - SUM DIGITS'''

'''EXERCISE - STRING COUNT'''

'''EXERCISE - PAIR STAR'''

'''EXERCISE - COUNT 7'''

'''EXERCISE - LIST 220'''

'''EXERCISE - COUNT "ABC" AND "ABA"'''

'''EXERCISE - CHANGE PI'''

'''EXERCISE - '''

'''EXERCISE - '''