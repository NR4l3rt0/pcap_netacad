"""

This program will check how many characters there are in a given text file
and will create a histogram from it (if the value is 0, then will be omitted)

"""

from os import strerror


# In this case, we will assume that the text file is in the same directory as the program
def take_txt_name():
    out= False
    
    while not out:
        
        txt_name= input("Please, enter the name of the file you want to analyse: ")

        try:
            assert txt_name != str()
            out= True
        except:
            print("Error: no valid input")
            exit()

    return txt_name


# This will try to read the file and put it in the memory 
def read_file(txt_name):
    file= ''
    
    try:
        lines_no= 0
        
        txt_f= open(txt_name, 'rt')
        line= txt_f.readline()
        
        while line != '':
            file += line
            line= txt_f.readline()        
            lines_no += 1

    except IOError as e:
        print("Error in the I/O operation: ", strerror(e.errno))
        exit(e.errno)

    # close the stream   
    else:
        txt_f.close()
        print("Number of lines read=", lines_no)

    
    return file



def create_results(file):

    result= dict()
    file= file.lower() # transform the file to be case-insensitive
    
    for i in range(97, 123):        # define and initialize the dictionary's keys
        result.update({chr(i): 0})

    for ch in file:             # actualize the values for each key for this concrete text
        if ch in result.keys():
            result[ch] += 1
        else:
            continue

    for el in result:       # show the results if the value is greater than 0
        if result[el] != 0:
            print(el, result[el], sep=" -> ")
        else:
            continue

    

# start
try:
    
    txt_name= take_txt_name()
    file= read_file(txt_name)
    create_results(file)
    
except KeyboardInterrupt:
    print()
    print("Thanks anyways!")
    print()
                
