'''
    This program will imitate the behaviour of 'split()'

    It just take an input string, check if is empty or has whitespaces and do the
    proper thing.
    Else, it will iterate over the string and when it gets a space it will stop and put
    the word in a 'list()'
'''

def mysplit(strng):
#
# put your code here
#
    txt= ""
    myList= list()

    # just to be secure we are working with a string
    try:
        assert str == type(strng)
    except:
        return "This is not a string -> {0} is {1}".format(str(strng),type(strng))
    
    if strng.isspace():
        return myList
    else:
        strng= strng.strip()
        for iterator in strng:
            txt += iterator
            if txt == chr(110):  
                continue
            elif (iterator == chr(32)) or (strng.endswith(txt)):    # in case there's no more whitespaces, we check if we're in the end
                txt= txt.rstrip()       # remove the space on the write of the string
                myList.append(txt)
                txt = ""
        return myList


# Some selected input

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(3*5))
print(mysplit((lambda x: x+3)(5.2)))
print(mysplit(" abc "))
print(mysplit("answer" in "To be or not to be, that is the question"))
print(mysplit(""))
print(mysplit(234))
print(mysplit(None))
