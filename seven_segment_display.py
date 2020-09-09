"""
This program will print the elected numbers as a seven segment display panel
"""

# In this section the smallest parts are created
def one_to3():
    print("#"*3, end=" ")
        
def one_and3():
    print("# #", end=" ")
    
def first():
    print("#  ", end=" ")

def third():
    print("  #", end=" ")


# We build here each pannel's row given a concrete number
def step_one(lst):
    for i in lst:
        if i == 1:
            third()
        elif i == 4:
            one_and3()
        else:
            one_to3()

def step_two(lst):
    for i in lst:
        if i%4 == 0 or i == 9:
            one_and3()
        elif i <= 3 or i == 7:
            third()
        else:
            first()

def step_three(lst):
    for i in lst:
        if i == 1 or i == 7:
            third()
        elif i == 0:
            one_and3()
        else:
            one_to3()

def step_four(lst):
    for i in lst:
        if i == 6 or i%8 == 0:
            one_and3()
        elif i == 2:
            first()
        else:
            third()

def step_fifth(lst):
    for i in lst:
        if i == 1 or i == 4 or i == 7:
            third()
        else:
            one_to3()
            
# Putting all together row by row
def building_board(lst):
    try:
        assert lst != list()
    except:
        print("Error: empty list")

    print()    
    step_one(lst)
    print()
    step_two(lst)
    print()
    step_three(lst)
    print()
    step_four(lst)
    print()
    step_fifth(lst)
    print()

# Taking the input from the user
def taking_input():
    taking= True
    print("Press exit to end the program")
    while taking:
        try:
            number_in= input("Please, enter a number from 0 to 1 billion/ thousand million: ")
            if number_in == 'exit':
                quit()
            else:
                number_in= number_in.strip()
                assert type(int(number_in)) == type(1)
                assert int(number_in) >= 0 and int(number_in) < 100000000000
                return number_in
        except:
            print("\n\t### Error that doesn't follow the instructions ###", end="\n\n")

# Creating a list to iterate over which let us build the sequence to print later
def transform_input(number_in):
    lst= list()
    
    for i in number_in:
        lst.append(int(i))

    return lst


# invokation

number_in= str()
lst= list()

number_in= taking_input()
lst= transform_input(number_in)
building_board(lst)

print("\nTHE END!", end="\n\n")

















    
        
    
