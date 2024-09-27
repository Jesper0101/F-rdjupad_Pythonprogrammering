import pandas as pd
import logging
import re

# Creates a class called DataCleaner
class DataCleaner:
    def __init__(self) -> None:
        # Creates a logger for this class
        self.logger = logging.getLogger(__name__)
     
    # Creates a function that will remove letters
    def clean(self, data: pd.DataFrame) -> pd.DataFrame:
        if data is not None:
            # Creates a for loop that iterrates through GDP (in Trillions USD)
            for index, row in data.iterrows():
                try: 
                    # Use regex to remove any letters from GDP (in Trillions USD) column
                    cleaned_GDP = re.sub(r'[a-zA-Z]', '', str(row['GDP (in Trillions USD)']))  
                    # Strip leading/trailing whitespace from cleaned value and convert to a float                  
                    data.at[index, 'GDP (in Trillions USD)'] = float(cleaned_GDP.strip())
                
                except (TypeError, ValueError):
                    # If there is a issues converting to float the value will be set to NaN
                    data.at[index, 'GDP (in Trillions USD)'] = pd.NA
                    
                except Exception as e:
                    # Log any other exception
                    self.logger.error(e)
                    # Set value to NaN if error occurs
                    data.at[index, 'GDP (in Trillions USD)'] = pd.NA
                    
        else:
            self.logger.error('Data not available')
            
        return data
