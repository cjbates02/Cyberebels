import sqlite3

def initialize_database():
    connection = sqlite3.connect('Cyberebels.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Inquiries (
            inquiryID INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            description TEXT,
            first_name TEXT,
            last_name TEXT,
            phone INT
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_database()
    print("Remindful database initialized successfully.")