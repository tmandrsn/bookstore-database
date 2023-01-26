
# Program to create a database for the book store and to populate it
# Only run once

import sqlite3
db = sqlite3.connect('ebookstore')
cursor = db.cursor()  # Get a cursor object

# create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, 
                    Title varchar(255), Author varchar(255),  Qty INTEGER);
''')

# Insert values
book_list = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30), 
(3002, "Harry Potter and the Philosopher's Stone", "J.K.Rowling",40),
(3003, 'The Lion the Witch and the Wardrobe', "C. S. Lewis", 25),
(3004, 'The Lord of the Rings', "J. R. R Tolkien", 37),
(3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]


cursor.executemany('''
    INSERT INTO books(id, Title, Author, Qty)
    VALUES (?,?,?,?)
''', book_list)

db.commit()
db.close()