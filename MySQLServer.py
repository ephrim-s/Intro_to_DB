
import mysql.connector
from mysql.connector import errorcode

# Function to create the database
def create_database():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password")
        
        cursor = db_connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        db_connection.commit()

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()

if __name__ == "__main__":
    create_database()
