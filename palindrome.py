"""
This program will receive an input and will tell if such a string is a
palindrome or not with the help of the print method.

"""

def take_input():
    try:
        phrase= input("Please enter a phrase to check (or press enter to exit): ")
        assert phrase != str()
    except KeyboardInterrupt:
        print("\nYou went out so quickly!\nSee you")
        quit()
    except:
        print("\nI cannot read your mind yet... \nWhy don't you try to write something? :)")
        quit()
        
    return phrase

def is_palindrome(phrase):

    yes= bool() # just for asigning it a value and printing the result

    phrase= phrase.upper() # for having it case insensitive
    phrase= phrase.lstrip() # we discard the whitespace at the beginning

    tmp= str()
    for ch in phrase: # remove the empty spaces between words
        if ch == chr(32):
            continue
        else:
            tmp += ch
            
    phrase= tmp
    
    rev_phrase= phrase[::-1] # we use the idiom for copying backwards the string 
    
    for i_ch in range(len(phrase)):
        if phrase[i_ch] == rev_phrase[i_ch]: 
            yes= True
        else:
            yes= False
            break
        
    if yes:
        print("\nIt's a palindrome")
    else:
        print("\nIt's not a palindrome")

        
        
# invoking

print('''
##########################
# Is this a palindrome?? #
##########################
''')
print()

phrase= str()

phrase= take_input()
is_palindrome(phrase)
    
    
