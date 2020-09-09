"""

This program will take a string as input, and a number in the range of 1-25
to shift the value of the previously inserted string.

As prerequisites:
- It will maintain if the character was lower/upper case.
- Besides, if it was not latin letter it won't case any effect.

Finally, the result will be printed.

"""

def taking_inputs():
    global text, shift # To have access later

    try:
        text= taking_text()
        shift= taking_range()
    except:
        print("""
            ###

            We had some issue with the input...
            Maybe, have you left it blank?
            
            ###
            """)
        quit()
        

def taking_text():

    try:
        text= input("Please, enter a text to cipher: ")
    
        if text.isspace() or text == str(): # In this case, we're not considering the whitespace as a valueable input because it would be just that
            assert type('error') is type(True)
        else:
            return text
    except:
        raise  # just a remainder how the exceptions work (as a kind of stack)
    


def taking_range():

    ok= False

    while not ok:
        try:
            # with int() we check that the input is an integer
            shift= int(input("Please, enter a integer in range 1-25 to shift the value: "))
            # the assertion makes us know if it's in the established range
            assert shift in range(1,26)        
            ok = True
        except:
            print("\n### Error: the value is not in the mentioned range ###\n")

    return shift



def ciphering(text, shift):

    #just to be sure we're working with the proper data
    assert text != str()
    assert type(shift) == type(1)

    # What we're doing here is just to check the range of the character if is uppercase
    # or lowercase, and if so, start from the beginning (it's a requirement).
    # Then, we append it to the string to print 'encrypted'
    
    encrypted=''
    
    for ch in text:
        if ord(ch) in range(65, 91):
            tmp= ord(ch) + shift

            if tmp > 90:
                ch = (tmp - 90) + 64
                encrypted += chr(ch)
            else:
                encrypted += chr(tmp)

        elif ord(ch) in range(97, 123):
            tmp= ord(ch) + shift

            if tmp > 122:
                ch = (tmp - 122) + 96
                encrypted += chr(ch)
            else:
                encrypted += chr(tmp)
                
        else:
            encrypted += ch

    print("\nThis is your message", encrypted, sep=" -> ")

    

# invoking

text= str()
shift= int()

print('''
################################
# Welcome to the Caesar cipher #
################################
''', end= "\n\n")
taking_inputs()
ciphering(text, shift)

print("\nHave a nice day!", end= "\n\n")
