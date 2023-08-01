'''
Question 2
Create a fully commented program to:
Ask a user to input a word, and the program will check to see if the word is a palindrome (reads the
same backwards and forwards).
'''
word = input("Please input a string to check it's palindrome or not: \t")
word = word.casefold()

# reverse the string
rev_str = reversed(word)

# check if the string is equal to its reverse
if list(word) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")