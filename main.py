import logging

from api import API
from datacleaner import DataCleaner
from datasaver import DataSaver

# Creating a logging configuration
logging.basicConfig(
    filename='/log.log',
    format='[%(asctime)s][%(name)s]%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)

# Logger for main script
logger = logging.getLogger(__name__)

# Logger for the start of the pipeline
logger.info('Starting data pipeline..')

# Initilize API, DataCleaner and DataSaver
api = API()
cleaner = DataCleaner()
saver = DataSaver()

# Fetching data from API
data = api.fetch_data()

# Checking if data was successfully returned from API
if data is not None:
    # Log a message if the data was fetched successfully 
    logger.info(f'Data fetched successfully from API!')
    print('Raw Data from API:')
    # Prints out first five rows of the data
    print(data.head())
    
    # Call the cleaner method to clean fetched data
    cleaned_data = cleaner.clean(data)
    # Call the saver method to save the cleaned data
    saver.save_data(cleaned_data)
    
    # Log message if data was cleaned
    logger.info('Data cleaned successfully!')
    print('Cleaned Data:')
    # Prints out first five rows of the cleaned data
    print(cleaned_data.head())
    
    # If the fetched data is None log a message
else:
    logger.info('Failed to fetch data from API')
