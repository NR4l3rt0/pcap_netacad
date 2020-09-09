# This program will ask for numbers to add to a list, and then delete the repeated ones.
# Finally, it will show the result sorted.
#(Just one way of doing it)
# I put the lists here for clarity.
# The end is just as a flag that is going to determine if we finish the program before the end point.

myList= []
uniqueList= []
repeatedValues=[]
end= True

try:
    elements = int(input("How many numbers do you want to insert?: "))
except:
    try:
        elements = int(input("Not letters, in numbers please: "))
    except:
        end= False
        print("Don't have time now for this...")

        
if end:
    counter= 0
    for i in range(elements):
        if counter<=1:
            try:
                value= float(input("Insert an integer, please: "))
                myList.insert(0, int(value))
            except:
                repeating= True
                while repeating:
                    if counter<=1:
                        try:
                            value= float(input("I was distracted... sorry. Can you repeat it, please? "))
                            repeating = False
                            myList.insert(0, int(value))
                        except:
                            print("I'm confused today...")
                            counter += 1
                    else:
                        repeating = False
                        print("Why don't we try it later?")
                        end= False
                    

if end:
    print("\nSummarizing:", end="\n\n")
    print("\tElements in your list:\n\t", myList, end="\n\n")

    for i in myList:
        if i not in uniqueList:
            uniqueList.insert(0, i)
        else:
            repeatedValues.append(i)


    uniqueList.sort()
    myList= uniqueList[:]  # check the slice that let us copy all the values easily

    print("\tThe distinct elements in the list are: \n\t",myList, end="\n\n")
    print("\tThe repeated ones: \n\t",repeatedValues, end="\n\n")

    print("That's all! Thanks!")

