#! python3

"""
Have the user enter in a sentence. 
Check to see if the word "password" is located in the sentence

Inputs:
a sentence

Outputs:
"the sentence contains password"
"the sentence does not contain password"

Examples:
Enter a sentence: I will not buy this record, it is scratched.
the sentence does not contain password

Enter a sentence: The best password is no password.
the sentence contains password
"""
sentence = input("Input your sentence")
word = 'password'
word2 = "Password"

if word in sentence:
    print('the sentence contains the password')
elif word2 in sentence:
    print("the sentence conatains the password")
elif word not in sentence:
    print("the sentence does not contain password")