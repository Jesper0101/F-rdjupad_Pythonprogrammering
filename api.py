import pandas as pd
import logging

# Creates a class called API
class API:
    def __init__(self) -> None:
        # Creates a logger for this class
        self.logger = logging.getLogger(__name__)
        
        # Defines file path as an instance
        self.file_path = 'C:/Users/dogsh/OneDrive/Dokument/Python Kurs/.venv/Kunskapskontroll2/country_comparison_dataset.csv'
                
    # Creates a function to fetch data and raise any error and logging it
    def fetch_data(self):
        
        try:
            self.logger.info(f'Fetching data from {self.file_path}')
            
            # Reads the CSV file into a Dataframe
            df = pd.read_csv(self.file_path)
            self.logger.info(f'Fetched data successfully from {self.file_path}')
            return df
        
        except FileNotFoundError:
            # Log error if file not found
            self.logger.error(f'File not found: {self.file_path}')
        
        except pd.errors.EmptyDataError:
            # Log error if file is empty
            self.logger.error(f"File is empty: {self.file_path}")    
        
        except Exception as e:
            # Log any other exception
            self.logger.error(f"An error occurred while fetching data: {str(e)}") 
            