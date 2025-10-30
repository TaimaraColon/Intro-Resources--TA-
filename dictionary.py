'''DICTIONARY PRACTICE PROBLEMS SET'''

''' EXERCISE 1 - Purge '''
'''
Write a function called solution() which takes a dictionary and a value as its arguments, 
removes every key from the dictionary that maps to the given value, and returns the modified dictionary.

If the dictionary given as parameter is empty, it should return an empty dictionary.
If value is NOT in the dictionary return the same dictionary (no modifications).

Remember: Do not alter the contents of a container while using that same container as the target of a for-loop! 
That behavior is undefined!
'''
def solution(D,val):
    for key in D.copy():
        if D[key] == val:
            del D[key]
    return D

print(solution({'dog':3, 'frog': 9, 'bird': 3}, 3))                   # Output: {'frog': 9}
print(solution({'a': 3, 'b': 2, 'c': 3, 'd': 1}, 3))                  # Output: {'b': 2, 'd': 1}
print(solution({0:'apple', 1:'banana', 2:'cherry',3:'date'}, 'date')) # Output: {0: 'apple', 1: 'banana', 2: 'cherry'}
print(solution({},1))                                                 # Output: {}
print(solution({'a': 3, 'b': 2, 'c': 3, 'd': 1}, 4))                  # Output: {'a': 3, 'b': 2, 'c': 3, 'd': 1} 

'''EXERCISE 2 - Word Count'''
'''
Write a function word_count which takes a string and returns a dictionary mapping each word to number of times
that word appears in the string.

Parameters:

A string with only capital and lowercase letters

Input Example: "That that is is that that is not is not Is that it It is"

Return Value:

Dictionary mapping number of times a word appears in the given string. Words that are capitalized are different than 
words without capitalization, meaning if the string was "Hello hello", the dictionary would hold two entries: one with 
key "Hello" and another with key "hello".

Example:

sentence = "That that is is that that is not is not Is that it It is"

word_count(sentence) returns:
{
 'That': 1, 
 'that': 4,
 'is': 5,
 'not': 2,
 'Is': 1,
 'it': 1,
 'It': 1
}
'''
def word_count(str):
    result = {}
    list_str = str.split()
    for i in list_str:
        if i not in result:
            result[i]= 1
        else:
            result[i]+=1
    return result

print(word_count("That that is is that that is not is not Is that it It is")) # Output: {'That': 1, 'that': 4,'is': 5,'not': 2,'Is': 1,'it': 1,'It': 1}
print(word_count("That that tHat thAT"))                                      # Output: {'That': 1, 'that': 1, 'tHat': 1, 'thAT': 1}
print(word_count(""))                                                         # Output: {}

'''EXERCISE 3 - Max Frequency'''
'''
Write a function most_frequent_element which takes a list of values with any type and returns the value appearing the most number of times in the list.
If the list is empty return -1.

Parameters:

A list of values that can be of any type

Return Value:

Return the value appearing the most number of times in the list. Assume there is always one element that appears the most frequently.

Example:

most_frequent_element(['hello', True, 4, -30.3, True, 'hello', 4, True]) returns True
'''
def most_frequent_element(lst):
    dict = {}
    if lst == []:
        return -1
    for w in lst:
        dict[w] = dict.get(w, 0) + 1
    max_freq = 0
    for w in dict:
        if dict[w] > max_freq:
            max_freq = dict[w]
            max_val = w
    return max_val

print(most_frequent_element(['hello', True, 4, -30.3, True, 'hello', 4, True]))             # Output: True
print(most_frequent_element(['no', 'expert', 'terrific', 'order', 'no', 'no', 'terrific'])) # Output: no
print(most_frequent_element(['1', 0, 0, -3, True, '0', 4, False]))                          # Output: 0
print(most_frequent_element([]))                                                            # Output: -1

''' EXERCISE 4 - Common Animal '''
'''
You went on a hike looking for animals and wrote down a list of all animals you saw. 

Write a function called animal_count that takes in a list of animals as an argument and returns a dictionary with the counts of how many times each animal was seen. 
If the list of animals is empty, return an empty dictionary. 

Since you were so excited, you did not pay attention to capitalization, so sometimes you used capital letters and sometimes used lowercase letters. 
You should make all of your dictionary keys lower case. 
'''
def animal_count(animals):
    sightings_count = {}
    for animal in animals:
        lower_animal = animal.lower()
        if lower_animal in sightings_count:
            sightings_count[lower_animal] += 1
        else:
            sightings_count[lower_animal] = 1
    return sightings_count

print(animal_count(['bear', 'goat', 'Pika', 'BEAR', 'bear', 'goat']))             # Output: {'bear': 3, 'goat': 2, 'pika': 1}
print(animal_count(['deeer', 'squirrel', 'rabbit', 'RABBIT', 'Rabbit', 'DEEER'])) # Output: {'deeer': 2, 'squirrel': 1, 'rabbit': 3}
print(animal_count(['chipmunk', 'moose', 'Moose', 'BEAVER']))                     # Output: {'chipmunk': 1, 'moose': 2, 'beaver': 1}
print(animal_count(['blue jay']))                                                 # Output: {'blue jay': 1}
print(animal_count([]))                                                           # Output: {}

''' EXERCISE 5 - Lists to Dictionary'''
'''
Write a Python program to convert two Python lists into a dictionary where elements from the first list become keys and elements from the second list become values.
You can assume both lists are the same size.

For example:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

Expected Output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
'''
def lists_to_dict(keys_list, values_list):
    result = {}
    for i in range(len(keys_list)):
        result[keys_list[i]] = values_list[i]
    return result

print(lists_to_dict(['Ten', 'Twenty', 'Thirty'], [10,20,30])) # Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
print(lists_to_dict(['a', 'b', 'c', 'd'], [1,2,3,4])) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(lists_to_dict([], [])) # Output: {}

''' EXERCISE 6 - Merge Dictionaries '''
'''
Write a code to merge two dictionaries into a new dictionary.

Example:
'''

''' EXERCISE 7 - Only Selected Keys '''
'''
Write a Python program to create a new dictionary by extracting the selected keys given in a list from a given dictionary.

Example: 

'''
''' EXERCISE 8 - Rename Key'''

'''
Write a program to rename a specific key to a given one in the parameters in a dictionary.
'''

''' EXERCISE 9 - Unique Values'''
'''
Write a function that takes a dictionary and returns True if all values in the dictionary are unique, False otherwise.
'''