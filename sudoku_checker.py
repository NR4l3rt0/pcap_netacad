"""

This program will ask for the rows of a sudoku and will check if it's valid or not

"""


def take_row():

    ok= sure= False
    
    while not ok:

        try:
            row= input("Please, enter a row: ")
            row= row.strip()   # quit the whitespace before and after if it is the case
            assert row.isdigit()  # assert is digit the entire string

            for el in row:
                assert int(el) in range(1,10) # check that the elements are in the necessary range
            ok= True

        except KeyboardInterrupt:
            print()
            print("That was unusual... Thanks anyway!")
            print()
            quit()
        except:
            print()
            print("### Error: it has to be just different digits fom 1-9 ###")
            print()

        if ok:
            try:
                assert len(row) == 9   # checks that it has exactly 9 elements
                sure= True
                
            except:
                print()
                print("There has to be 9 numbers with no spaces")
                print()
                ok= False  # in case it doesn't pass the second part we're force to start again
          
    return row


def create_all_rows():
    
    for row in range(9): 
        row= take_row()
        rows.append(row)

    return rows



def create_columns(rows):
    
    try:
        assert rows != list() 
    except:
        print("We had a problem transfering the rows")

    for i in range(len(rows)):
        column= ''
        for row in range(9):
            column += rows[row][i]       
        cols.append(column)

    return cols



def create_sub_squares(rows):

    try:
        assert rows != list()
    except:
        print("Empty rows transfered")

    sub_q1 = ''
    sub_q2 = ''
    sub_q3 = ''
        
        
    for row in range(len(rows)): 

        if row < 3:
            sub_q1 += rows[row][:3]   # access the elements through slices, 
            sub_q2 += rows[row][3:6]  # concatenate them and append them to 'sub_squares'
            sub_q3 += rows[row][6:9]  # three at a time 
            
            if row == 2:
                sub_squares.append(sub_q1) 
                sub_squares.append(sub_q2)
                sub_squares.append(sub_q3)
                sub_q1 = ''                 # restart the variables
                sub_q2 = ''
                sub_q3 = ''
                
        if row >= 3 and row <6:
            sub_q1 += rows[row][:3]    
            sub_q2 += rows[row][3:6]
            sub_q3 += rows[row][6:9]
            
            if row == 5:
                sub_squares.append(sub_q1)
                sub_squares.append(sub_q2)
                sub_squares.append(sub_q3)
                sub_q1 = ''
                sub_q2 = ''
                sub_q3 = ''

        if row >= 6 and row < 9:
            sub_q1 += rows[row][:3]    
            sub_q2 += rows[row][3:6]
            sub_q3 += rows[row][6:9]
                
            if row == 8:
                sub_squares.append(sub_q1)
                sub_squares.append(sub_q2)
                sub_squares.append(sub_q3)
          
    try:
        assert sub_squares != list()
    except:
        print("Something happened with the sub_squares")

    return sub_squares



def is_unique(lst):   # check that rows, cols and sub_squares are unique as a unit
                      # That is to say, that they follow the rules
    checked= False
    
    for i in range(9):
        for j in lst[i]:
            if lst[i].count(j) != 1:
                print("Is not valid")
                quit()
            else:
                continue
            
        checked= True

    return checked



def is_sudoku(checked_rows, checked_cols, checked_subs):

    if checked_rows == checked_cols == checked_subs: # each part has to be checked and ok
        print("Yes, it is")
    else:
        print("Sorry, something misteriously happened")
                    




# start program

rows= list()
cols= list()
sub_squares= list()

rows= create_all_rows()
cols= create_columns(rows)
sub_squares= create_sub_squares(rows)

checked_rows= is_unique(rows)    
checked_cols= is_unique(cols)
checked_subs= is_unique(sub_squares)

is_sudoku(checked_rows, checked_cols, checked_subs)


