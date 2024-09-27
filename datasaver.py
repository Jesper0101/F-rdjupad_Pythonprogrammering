import pandas as pd
import sqlite3
import logging

# Creates a class called DataSaver
class DataSaver:
    # Initialize the class with a defult path to SQLite database
    def __init__(self, db_path: str = 'database.db') -> None:
        self.logger = logging.getLogger(__name__)
        self.path = db_path 
    
    # Function to save DataFrame to SQLite database   
    def save_data(self, data = pd.DataFrame, table_name: str = 'cleaned_data') -> None:
        # Check if DataFrame is empty will log a warning if there is no data
        if data.empty:
            self.logger.warning('No data to save')
            return
        
        try:
            # Creates a SQLite3 connection to the database
            with sqlite3.connect(self.path) as con:
                # Saves DataFrame to a specified table in the database
                data.to_sql(table_name, con, if_exists='replace', index=False)
                # Log a message indicating the data was saved successfully
                self.logger.info(f'Data saved to {table_name} in {self.path}')
        
        # Log error if there is an issue with the database
        except sqlite3.DatabaseError as e:
            self.logger.error(f"Database error: {e}")
        # Log error if there is any other issue
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")

