"""
This program will compare two strings and will notice if they're an anagram or not.

Rules:
- Two empty strings are not anagrams
- Case-insensitive
- Spaces are not taken into account while checking

· I'll add the possibility of being a phrase too

"""

def take_input():

    try:
        text= input("Enter a word or phrase to check if it's an anagram: ")
        text= text.strip()   # this two step will discover if is an empty string or not
        assert text != str() 
    except KeyboardInterrupt:
        print("\nGood bye, friend!", end="\n\n")
    except:
        print("\nWe had an issue with your input", end="\n\n")
        quit()

    return text


def analize_chars(strng):
    text= ''
    
    try:
        strng= strng.lower()
    except:
        print("We've an issue while neutralizing lowercase letters")

    for ch in strng:   # remove whitespace
        if ch == ' ':
            continue
        else:
            text += ch
    
    return text


def scrutinize_phrase(strng):
    summary= dict()
    # total= int()

    for ch in strng:
        if ch in summary.keys():
            continue
        else:
            total= strng.count(ch)
            summary.update({ ch : total})

    return summary


def compare_parts(summary1, summary2):

    # is_anagram= bool()
    
    try:
        assert summary1 != dict() and summary2 != dict()
    except:
        print("Nothing to compare")


    if len(summary1) == len(summary2): # this will check that they have the same distinct chars
        for pair in summary1.items():  # check if every letter exist in the other part and the same number of times
            if pair in summary2.items():
                is_anagram= True
                continue
            else:
                print(f"\n This {pair} is not the same")
                is_anagram= False
                break                
   
    else:
        is_anagram= False
        
    if is_anagram:
        print("Yes, they are!")
    else:
        print("They're not an anagram.")
        
    

# start program
print()
print("""
--------------------------
|   Are they anagrams?   |
--------------------------
""", end="\n\n")

text1= take_input()
text2= take_input()
print()
text1= analize_chars(text1)
text2= analize_chars(text2)

summary1= scrutinize_phrase(text1)
summary2= scrutinize_phrase(text2)

compare_parts(summary1, summary2)




