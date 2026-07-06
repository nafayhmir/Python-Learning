#Strings

#python accepts input as well as output in "" and ''
#i.e name="Ali" and name='Ali' both work
#Each Variable is indexed starting form zero
#i.e 
#P Y T H O N
#0 1 2 3 4 5
#we can use this feature to print specific parts of a word
'''name="Nafayh Akhlaq Ahmed"
degree="BS-EE"
print("Welcome",name[0],degree)''' #OutPuts one letter of a name, not very useful
#we can change this by knowing this syntax string[start:end]
#now 
'''print("Welcome",name[0:6],degree) '''#both numbers given will be used
#we can find length of a string using len() function
'''length=len(name)
print(length)'''
'''
name = "Nafayh"

print(len(name))
print(max(name))--> Largest ASCII value
print(min(name))--> Lowest ASCII value
'''

#Omitting Values
#we can ommit values
'''name="Nafayh"
print(name[2:]) '''# will print fayh

#Reverse string
'''name="Nafayh"
print(name[::-1]) #Code to completely reverse a string'''

#Changing Strings: Cant be done directly 
#name="Ali", name[0]=K will give error
#we need to slice the word and make it into a new variable 
'''
word = "Python"
new_word = "J" + word[1:]
print(new_word)
'''
#Task: user based palindrome checker
word=input("Enter word to check palindrome: ")
new_word=word[::-1]
if word==new_word:
    print("Is a Palindrome")
else:
    print("Not a Palindrome")