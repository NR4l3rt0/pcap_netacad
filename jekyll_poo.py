"""

This program will read a text and will print the results in the console
with a certain format and order.
It's a practice to develop the ability to create our own exceptions and familiarize
with that concept.

Keywords: 'raise' and passing messages.

"""

from os import strerror

# define the classes' hierarchy for the objects created in the exceptions
class StudentsDataException(Exception):
    def __init__(self, message= '', fileName= ''):
        Exception.__init__(self, message)
        self.fileName= fileName


class BadLine(StudentsDataException):
    def __init__(self, message= '', fileName= '', name= 'unknown', points= '0.0'):
        StudentsDataException.__init__(self, message, fileName)
        self.name= name
        self.points= points

        
class FileExistence(StudentsDataException):
    def __init__(self, message= '', fileName= '', info= 'Non existent'):
        StudentsDataException.__init__(self, message, fileName)
        self.info= info



def takeInput():

    txt= input("Enter the name of the file, please: ")
    print()
    
    if txt == str():
        raise FileExistence("No name provided")
    else:
        return txt

        

def readFile(txt):
    file= None
    pairsList= list()
    countLine= 0

    try:
        file= open(txt, 'rt')
        assert file != None

    except:
        raise FileExistence("file not found", file)

    else:
        line= file.readline()
        if line == str():
            raise FileExistence("file is empty", file)
        else:
            while line != '':
                
                countLine += 1

                pair= parseLine(line) # call an auxiliary method 

                pairsList.append(pair)
                
                line= file.readline()


    print("- Lines read in the file:", countLine)
    print()
    
    return pairsList                    



def parseLine(strng):
    
    whole= strng.split()
    name= str()
    points= float()


    if len(whole) < 3:
        raise BadLine(message= "A line has to have 3 elements minimum")

    # cancel the exception created when failing to transform a str() into float()
    try:        
        if type(float(whole[-1])) == type(float()):
            points= whole[-1]
            
    except:
        raise BadLine(message= "is not a number", points= whole[-1])

        
    for el in whole[:-1]:
        if el.isalpha():        # check the names are formed from just letters
            name +=  ' ' + el 
        else:
            raise BadLine(name= el, message= "is not properly defined")


    pair= tuple((name, points))

    return pair



def createDict(pairsList):

    dictionary= dict()


    try:
        assert pairsList != list()
    except:
        print()
        print("List cannot be printed without values")
        print()
        exit()
    
    for pair in pairsList:
        name= pair[0]
        points= float(pair[1]) # will let add numbers (if not it will concatenate strings)

        # create a new entry or update de values
        if name in dictionary:
            dictionary[name] += points
        else:
            dictionary.update({name : points})

    # sort lexically
    keys= sorted(dictionary.keys())

    print("### Summary ###")
    print()
    for k in keys:
        print("{0}\t{1}".format(k, dictionary[k]))




# start 
try:
    txt= takeInput()
    pairsList= readFile(txt)
    createDict(pairsList)

    print()
    print()
    print("Thanks for your time")
    print()


except FileExistence as fe:
    print()
    print("Error:", "|Message", fe, "|Special info", fe.info, sep=" : ")
    print()

except BadLine as bl:
    print("Error in", txt, "|Message", bl, "|Name", bl.name, "|Points", bl.points, sep=" : ")

except StudentsDataException as sdt:
    print()
    print("Error:", sdt.message, sdt.fileName, sep=" : ")
    print()

except IOError as e:
    print()
    print("Error while reading", strerror(e.errno))
    print()
    exit()
    
except KeyboardInterrupt:
    print()
    print("Error: Interruption!")
    print()
    exit()
    
except BaseException:
    print()
    print("Thanks anyway")
    print()






    












        
        
