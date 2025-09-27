'''String Concatenation Problems'''
'''
Email Creation

Goal: Use concatenation of strings to create an email for a person. 
The email will have the following format: first letter of the first name of the person + last name + @upr.edu

Task: Given the first name and last name of a person build an email address for them.

Example:
first_name = Maria
last_name = Lopez

email_address = mlopez@upr.edu

Hint: You can use the .lower() string method to make a string lowercase.

'''
def email_builder(first_name, last_name):
    email_address = first_name[0].lower()+last_name.lower()+'@upr.edu'
    return email_address

'''Tests'''
print(email_builder('Maria', 'Lopez'))
print(email_builder('Carlos', 'Colon'))
print(email_builder('Jorge', 'Ruiz'))

'''
Hashtag generator

Goal: Use concatenation of strings to create a hashtag.
The hashtag will have the following format: #FirstWordSecodWordThirdWord

Task: Given three words generate a hashtag. The hashtag should have each first letter of the words capitalized.

Example:
word1 = puerto
word2 = rico
word3 = coding

Output: #PuertoRicoCoding

Hint: You can use upper() and lower() string methods to capitalize a word. 

'''
def hashtag(w1, w2, w3):
    w1 = w1[0].upper() + w1[1:].lower()
    w2 = w2[0].upper() + w2[1:].lower()
    w3 = w3[0].upper() + w3[1:].lower()
    
    tag = "#" + w1 + w2 + w3
    return tag

'''Test'''
print(hashtag("puerto", "rico", "coding"))
print(hashtag("string", "concatenation", "practice"))
print(hashtag("reD", "gReen", "bLue"))

'''
Password Hint

Goal: Use concatenation of strings to display a password hint.

Task: Given the first and last name of the person, build a password hint.
The password hint will be the two first letters of the first name and the two last letters of the last name.
For the in between place 3 stars (***).

Example:
first = Maria
last = Lopez

Output: ma***ez

Hint: Slicing :)

'''
def password_hint(first, last):
    first = first.lower()
    last = last.lower()
    left = first[:2]
    right = last[-2:]
    hint = left + "***" + right
    return hint

'''Tests'''
print(password_hint("Maria", "Lopez"))
print(password_hint('Luis', 'Colon'))
print(password_hint('Jorge', 'Ruiz'))
'''
File Check

Goal: Use concatenation of strings to check if the given file is an image.

Task: Given a filename check if the file ends in .jpg, .png, .jpeg. 
If it does then it is an image! Return the message: "The file {filename} is an image"
Use concatenation of strings to display the message.
If the file does not end in .jpg, .png, .jpeg, return the message: "{filename} is an unsupported file type"

Example:
filename = cat.jpg

Output: The file cat.jpg is an image

'''
def allow_image(filename):
    f = filename.lower()
    if f[-4:] =='.jpg' or f[-4:] =='.png' or f[-4:] =='.jpeg':
        return "The file " + filename + " is an image"
    return filename + " is an unsupported file type"

'''Tests'''
print(allow_image('cat.jpg'))
print(allow_image('game.py'))
print(allow_image('turtle.png'))

'''
Replace Vowels

Goal: Given a string of words replace all the vowels of the sentence to the a specific vowel using string concatenation.

Task: Make a program that takes as parameters the sentence and the specific vowel. Replace all the vowels of the sentence to this one.
Also, add the final puntuacion mark (.) to mark the end of the sentence.

Example:
sentence = "I like pizza"
vowel = "o"
new_sentence = "O loko pozzo."

Hint: Remember that strings are immutable.

'''
def replace_vowels(sentence, vowel):
    new_sentence = ''
    all_vowels = "aeiouAEIOU"
    for i in sentence:
        if i in all_vowels:
            new_sentence+=vowel
        else:
            new_sentence+=i

    return new_sentence + '.'

'''Tests'''
print(replace_vowels("Python is cool", 'a'))
print(replace_vowels("Practice, practice, practice", 'u'))
print(replace_vowels("Hello World", 'e'))

'''
Word Divide

Task: Write a function called word_divide() that has as parameter a string.

Return: given string with character '&' inserted in middle. If string has an odd number of characters, '&' appears right before middle character.

Example:

word_divide('banana') return 'ban&ana'

word_divide('happy') return 'ha&ppy'

'''
def word_divide(word_to_divide):
    # write your code here
    return -1

'''Solution'''
def word_divide(word_to_divide):
    length_of_word = len(word_to_divide)
    middle = length_of_word // 2
    return word_to_divide[0: middle] + '&' + word_to_divide[middle:]

'''Tests'''
print(word_divide('banana'))
print(word_divide('happy'))
print(word_divide('kiwi'))