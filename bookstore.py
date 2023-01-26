# Program to add, update, delete and search books in the database

import sqlite3
db = sqlite3.connect('ebookstore')
cursor = db.cursor()


def add_book():
    '''
    Function to add new book to database
    '''
    while True:
        title = input('Enter the title of the book: \t')
        author = input('Enter author of book:\t')
        quantity = input('How many books? \t')
        # Check input is a integer
        try:
            quantity = int(quantity)
        except:
            print('Not a valid number')
            break
        # Enter details to table
        cursor.execute('''
        INSERT INTO books(Title, Author, Qty)
        VALUES (?,?,?)
        ''', (title, author, quantity))
        db.commit()
        print(f'{title} added to the bookstore')  
        break  

def update_book():
    '''
    Function to update column for a particular book
    '''
     # Select book to update
    while True:
        id = input('Enter the id number of the book you want to update \t')
       
        # Test if input is a number
        try:
            id = int(id)
        except:
            print('Not a valid number')
            break

        cursor.execute('''
        SELECT * FROM books
        WHERE id = ?
        ''', (id,))
        book = cursor.fetchone()
        # Check if book is in database
        if book == None:
            print('Book not found')
            break
        else:
            # Print details of book
            print('The followin book will edited')
            print(book)
            # Select which column to update
            update_choice = input('''Which column do you want to update?
            t - Title
            a - Author
            q - Quantity
            ''')
            if (update_choice == 't'):
                title = input('Enter the new title\t')
                # Update title
                cursor.execute('''
                UPDATE books
                SET title = ?
                WHERE id = ?
                ''',(title,id))
                db.commit()
                print('Book updated')
                break
            elif (update_choice == 'a'):
                author = input('Enter the new author\t')
                # Update author
                cursor.execute('''
                UPDATE books
                SET title = ?
                WHERE id = ?
                ''',(author,id))
                db.commit()
                print('Book updated')
                break
            elif (update_choice == 'q'):
                quantity = input('Enter the new quantity\t')
                # Check input is a number
                try:
                    quantity = int(quantity)
                except:
                    print('Not a valid number')
                    break
                # Update quantity
                cursor.execute('''
                UPDATE books
                SET title = ?
                WHERE id = ?
                ''',(quantity,id))
                db.commit()
                print('Book updated')
                break
                
            else:
                print('Incorrect selection')
                break


def delete_book():
    '''
    Function to remove book from database
    '''
     # Select book to update
    id = input('Enter the id number of the book you want to remove \t')
    
    while True:
        # Check input is an integer
        try:
            id = int(id)
        except:
            print('Not a valid number')

        cursor.execute('''
        SELECT * FROM books
        WHERE id = ?
        ''', (id,))
        # Print details of book
       
        book = cursor.fetchone()
        # Check book exists
        if book == None:
            print('Book not found')
            break
        else:
            print('The followin book will deleted')
            print(book)
            # Select which column to update
            update_choice = input('''Are you sure?
            y - yes
            n - no
            ''')
            if (update_choice == 'y'):
                cursor.execute('''
                DELETE FROM books
                WHERE id = ?
                ''',(id,))
                db.commit()
                print('Book deleted')
                break
            elif (update_choice == 'n'):
                print('Book not deleted')
                break
            else:
                print('Incorrect selection')
                break


def search_books():
    '''
    Function to search for a book
    '''
    # Determine how to search for the book
    search_by = input(''' Do you want to search by id, title or author?
    i - id
    t - title
    a - author
    ''')
    if search_by == 'i':
        # Search by ID number
        id = input('Enter the id of the book \t')
        # Check input is a valid integer
        while True:
            try:
                id = int(id)
            except:
                print('Not a valid number')
                break
            # select by id
            cursor.execute('''
            SELECT * FROM books
            WHERE id = ?
            ''', (id,))
            print(cursor.fetchall())
            break

    elif search_by == 't':
        # Search by Title        
        title = input('Enter the title of the book (case sensitive) \t')
        # select where title contains the input
        cursor.execute('''
        SELECT * FROM books
        WHERE instr(Title, ?) > 0
        ''', (title,))
        print(cursor.fetchall())

    elif search_by == 'a':
        # Search by Author
        author = input('Enter the author of the book (case sensitive) \t')
        # Select where author contains the input
        cursor.execute('''
        SELECT * FROM books
        WHERE instr(Author, ?) > 0
        ''', (author,))
        print(cursor.fetchall())

    else:
        print('Incorrect selection')




#### Main Program ####

# Return to menu after selection
while True:
    menu = input('''Select one of the following:
    1 - Enter a new book
    2 - Update a book
    3 - Delete a book
    4 - Search for a book
    0 - Exit
    ''')

    # Enter new book for database
    if menu == '1':
        add_book()

    # Update an book in the database
    elif menu == '2':
       update_book()

    # Delete a book from the database
    elif menu == '3':
        delete_book()
    # Search for a book from the database
    elif menu == '4':
        search_books()
    # Exit program
    elif menu == '0':
        print('Closing program')
        db.close
        exit()

    else:
        print('Incorrect selection please try again')
