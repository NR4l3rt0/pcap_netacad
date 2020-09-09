"""
    This program will receive an input and print it out on console.
    The goal of the exercise is to familiarize with exceptions, how they work
    and how can they be handled (asserting for being sure of the data
    one receives is the one it should be; and raising for communicating among
    functions, modules,...).
"""

def readint(prompt, min, max):
    try:
        assert v in range(-10,11) # just remember the end is x-1
        print("The number is:", v)
    except:
        print("### \nError: the value is not within permitted range.")
        raise
        


receiving_input= True

while receiving_input:
    
    try:
        v= int(input("\nEnter a number from -10 to 10: "))
        readint(v, -10, 10)
        receiving_input= False
        
    except ValueError:
        print("### \nError: wrong input. \nPlease, insert an integer. \n###")
    except AssertionError:
        print("That's it brother!! \n###")
    except KeyboardInterrupt:
        print("\n### \nLeaving things without finishing?\nThat's not very nice... \n###")
        break
    except:
        print("### I still have no idea about what happened... ###")

print("\nAnd I'm out!!")
    
