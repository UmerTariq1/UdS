"""
Introduction to Python Programming
COLLECTIONS

Exercise 2: Dictionaries (6 Points)

In this exercise, you are supposed to implement your own
'address book'. In this address book, you can store your
contacts using a nickname. For each nickname, you can save
different 'fields', such as 'First Name', 'Last Name',
'e-Mail', 'Office Phone', 'Home Phone' or 'Cell Phone'.
The entries in your phone book do not all have to have the
same fields, as the following examples show.

NICKNAME:     Stefan
First Name:   Stefan
Last Name:    Thater
Occupation:   Researcher
E-Mail:       stth@coli.uni-saarland.de
Office Phone: 4496

NICKNAME:     Anne
First Name:   Annemarie
Last Name:    Friedrich
Office Phone: 4347
Cell Phone:   0123456789

Your address book should provide the following functions.
Have a look at ex2_log.txt to see an example run of
this program. Before implementing the functions, scroll
down to the main() function and make sure you understand
its code and how you can test your program.

"""

def add_info(book, nickname, key, value):
    """
    'book' is a variable pointing to your address book dictionary
    object. As dictionaries are mutable, you can directly modify
    the dictionary pointed to by 'book'. This is what we called
    a 'side effect' in the lecture. Here, we actually want to use
    this effect.
    Important: In case the nickname doesn't exist yet in the address
    book, it should be added, and the field should be added as well.
    """

    if nickname not in book.keys():
        book[nickname] = {}
        book[nickname][key] = value
    else:
        book[nickname][key] = value

def show_info(book, nickname, key):
    """
    This function prints out a the information saved in a particular
    'field' of a contact (identified by the nickname) given a reference
    to the address book dictionary. Make sure that your function doesn't
    break when asking for a contact or a field that doesn't exist.
    """
    if nickname not in book.keys():
        print("There is no entry with the name : ",nickname)
    else:
        if key not in book[nickname].keys():
            print("There is no entry for this account for the field : ",key)
        else:
            print("key: \t ",book[nickname][key])



def show_entry(book, nickname):
    """
    This function prints out the complete entry (all keys together
    with their values) of a contact.
    Make sure that your function doesn't break in case the nickname
    asked for doesn't exist.
    """

    print("**************************************************")

    if nickname not in book.keys():
        print("There is no entry with the name : ",nickname)
    else:
        print("NICKNAME: \t",nickname)
        for each_key in book[nickname].keys():
            print(each_key,": \t", book[nickname][each_key])  

    print("**************************************************")


def del_entry(book, nickname):
    """
    Delete the complete entry for 'nickname' from the address book.
    """
    if nickname not in book.keys():
        print("There is no entry with the name : ",nickname)
    else:
        del book[nickname]

    

def del_info(book, nickname, key):
    """
    Delete the information saved using the key for 'nickname'.
    The rest of the contact information for 'nickname' should
    stay in the address book.
    Make sure your function doesn't break in case the nickname
    or the key don't exist.
    """
    if nickname not in book.keys():
        print("There is no entry with the name : ",nickname)
    else:
        if key not in book[nickname].keys():
            print("There is no entry for this account for the field : ",key)
        else:
            del book[nickname][key]

def show_book(book):
    """
    This function prints out the complete address book, i.e.,
    all contacts together with all their fields. Think about
    whether you can re-use one of the functions above for this
    function. Hint: You can solve this in two lines of code. But
    it's fine if you write more code, as long as it works!
    """

    for nickname in book.keys():
        print("**************************************************")
        print("NICKNAME: \t",nickname)
        for each_key in book[nickname].keys():
            print(each_key,": \t", book[nickname][each_key])  
        print("**************************************************")


def main():

    # Create an empty phone book (= dictionary) here.
    book = {}

    # Menu String
    menu = """
1 - Add / Update contact information
2 - Show contact information
3 - Show field information for contact
4 - Delete a contact
5 - Delete a field of information
6 - Show the whole address book
Press ENTER to leave.\n>> """
    
    # Loop to ask the user for input
    user_input = None
    while user_input != "":
        
        print("\n")

        choice = input(menu)

        # The following lines are to make sure the input
        # works correctly. Don't worry if you don't understand
        # them (yet).
        if choice == "":
            break
        try:
            choice = int(choice)
        except:
            print("Sorry, your choice was not recognized.\n")
            continue

        # From here on, you need to read and understand the code.
        if choice == 1:
            nickname = input("Nickname: ")
            key = input("Field: ")
            value = input("Value: ")
            add_info(book, nickname, key, value)
            
        elif choice == 2:
            nickname = input("Nickname: ")
            show_entry(book, nickname)

        elif choice == 3:
            nickname = input("Nickname: ")
            key = input("Field: ")
            show_info(book, nickname, key)

        elif choice == 4:
            nickname = input("Nickname: ")
            del_entry(book, nickname)

        elif choice == 5:
            nickname = input("Nickname: ")
            key = input("Field: ")
            del_info(book, nickname, key)

        elif choice == 6:
            show_book(book)

        else:
            print("Sorry, your choice was not recognized.\n")
            
if __name__ == '__main__':
    main()
