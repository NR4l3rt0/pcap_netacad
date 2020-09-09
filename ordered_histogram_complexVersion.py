"""

This program will read a file, analyze and sort the words by frequency.
Finally, it will write the result in a new text file ending with '.hist'

"""
from os import strerror

def take_input():
    out= False

    while not out:
        txt_name= input("Please, enter a text name: ")

        try:
            assert txt_name != str()
            out= True
            
        except:
            print("It should be given a name")

    return txt_name


def open_file(txt):
    file= str()
    
    # the '__next__' method returns the next line from the file and will be close automatically
    try:
        for line in open(txt, 'rt'):
            file += line
            
    except IOError as e:
        print("Error while opening", strerror(e.errno))
        exit(e.errno)

    finally:
        return file if (file != str()) else None


def create_dict(file):

    result= dict()
    not_there= list()
    
    try:
        assert file != None
        file= file.lower()
    except:
        print("We cannot work in this condition... we have nothing!!")

    for ch in generate_letter(): # use a generator for the letters
        
        value= 0
        if ch in file:
            value= file.count(ch)
            result.update({ch : value}) # create a dictionary with the result
        else:
            not_there.append(ch) # create an informative list with the other letters

    print()
    print("This letters are not in the file", not_there)
    print()

    return result



def generate_letter():
    letter= ''

    for ch in range(97,123):
        yield chr(ch)



def order_dict(result):

    sorted_dict= dict()

    try:
        assert result != None
        
    except:
        print("The dictionary provided has nothing in it")

    # Sort all the values from higher to lower
    
    # create a new sorted dictionary comparing each value with a key,
    # in the event that there's more than one key with the same value
    # then, a list with those keys are created and assigned to
    # the sorted list as a subgroup

    all_values= reversed(sorted(result.values()))

    count= count2= 0
    for val in all_values:
        for k in result:
            if val == result[k]:
                if k not in sorted_dict.keys():
                    sorted_dict.update({k : val})
                    break
                else:
                    #count += 1
                    continue
            else:
                #count2 += 1
                continue

    #print(count, count2)
    #print(sorted_dict, result)


    try:
        assert len(sorted_dict) == len(result) # check they have the same number
        return sorted_dict                     # of elements
    
    except:
        print("Some pair has been missed")
        exit()
                        
            

def write_to_file(sorted_dict):

    global txt
    
    try:
        assert sorted_dict != None
    except:
        print("No sorted dictionary at all")

    try:      
        txt_name = txt + ".hist"

        file= open(txt_name, 'wt')
        
        for k,v in sorted_dict.items():
            writing= "{key} -> {value}".format(key= k, value= v)
            file.write(writing)
            print(k,v, sep= " -> ")

    except IOError as e:
        print("Some error while writting", strerror(e.errno))
        exit(e.errno)

    except:
        print("Not sure what went wrong, but almost there")
        
    finally:
        file.close()
        print()
        print("The required name -> ",txt_name)



# start

try:
    
    txt= take_input()
    file= open_file(txt)
    result= create_dict(file)
    sorted_dict= order_dict(result)
    write_to_file(sorted_dict)
    print()
    print("All went fine")
    print()
    
except:
    print("Sorry to hear that")
    print()
    



    





