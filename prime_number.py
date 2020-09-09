# This exercise doesn't have the OOP style yet, so it's a bit procedural
# This program will show the number of primes that exist in a list either given a range
# o creating one on-the-fly.

# Notice too that I sometimes shadow the node_list variable to try to show the program's
# logic.

def prime_number(num):
    divisor= 0
    for i in range(1, num):
        if num%i == 0:
            divisor += 1
    else:
        if divisor < 2 and not num<=1:
            return True


def check_number_list(lst):
    is_prime= None
    for i in lst:
        is_prime= prime_number(i)
        
        if is_prime:
            true_primes.append(i)
        else:
            false_primes.append(i)


def take_number_list():
    answer= True
    num= None
    
    while answer:
        try:
            num = int(input("Please, enter integers or 'stop' to stop creating the list: "))
            number_list.append(num)
        except:
            answer= input("That's not a number... Are you tired of writing? (y/n): ")
            if (answer == 'y') or (answer == 'Y'):
                return number_list
            else:
                continue


def create_secuential_list():
    start_point = end_point= num= None
    sequencial_list= []
    
    try:
        print("\n\tRemember!\nNotice that it must be integers and the beginning must be lower than the end point")
        start_point= int(input("Select a number where you want to start: "))
        end_point= int(input("Now the end point: "))

        for i in range(start_point, end_point+1):
            num= i
            sequencial_list.append(num)
        else:
            return sequencial_list
    except:
        print("You didn't follow the rules!\n\nGoodbye!")

        

def do_process():
    sequence= None;

    print("\tWelcome to the prime number program wizard!!")
    print("\tWe'll discover them all! ;)\n")
    print("Do you want to know a secuential range or do you prefer to introduce your numbers? ")
    choice= input ("Type 1 if you want a secuence\nType 2 for the second option\n-> ")

    sequence= True if(choice=='1') else False  # ternary operator 
    
    if sequence:
        number_list= create_secuential_list()
    else:    
        number_list= take_number_list()
        
    check_number_list(number_list)

    true_primes.sort()
    false_primes.sort()

    print("\nThese are primes", true_primes, sep=" -> ", end="\n\n")
    print("These are not primes", false_primes, sep=" -> ", end="\n\n")


# defining lists and invoking

number_list= []
true_primes= []
false_primes= []    


do_process()    
