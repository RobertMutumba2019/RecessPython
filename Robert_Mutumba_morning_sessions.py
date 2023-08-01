#multithreading
"""
import threading

def course(name):
    print(f"I do {name} at COCIS")

th=[]
for i in range(10):
    t=threading.Thread(target=course, args=(f"Thread(i)",))
    th.append(t)
    t.start()

for t in th:
    t.join()

#multiprocessing

import multiprocessing

def process(Mitchell):
    print(f"The great {Mitchell} at MUK")
#CREATING A POOL
pool=multiprocessing.Pool(processes=5)

for can in range(6):
    pool.apply_async(process,args=(f"process(can)",))



pool.close()
pool.join()
"""
import threading
import multiprocessing
def main(name):
    print(f" show {name} on the Stack {threading.current_thread().name} and {multiprocessing.current_process().name}")
          
th=[]
for i in range(4):
   t=threading.Thread(target=main, args=(f"Thread(i)",))
   th.append(t)
   t.start()

for t in th:
    t.join()


#ContextManager for file handling
from contextlib import contextmanager


@contextmanager
def file_manager(filename, mode):
   
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()


with file_manager('example.txt', 'w') as file:
    file.write('This is my file.')



import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

        if exc_type is not None:
            # Exception occurred, handle it if needed
            print(f"An error occurred: {exc_val}")

        return True  # Suppress any exception

# Example usage
db_name = "software.db"

# Establishing a database connection using the context manager
with DatabaseConnection(db_name) as connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")

# The connection is automatically closed once we exit the context

# Performing database operations using the context manager
with DatabaseConnection(db_name) as connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Mutumba Robert", "rmutumba08@gmail.com"))

    # Committing the changes
    connection.commit()

    # Fetching data from the database
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

