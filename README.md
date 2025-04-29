📊 Fördjupad Pythonprogrammering – Country Comparison Data Pipeline
This project demonstrates an end-to-end ETL pipeline built in Python. It covers the extraction of country comparison data, cleaning specific fields, and saving it into a SQLite database. The project uses modular design with clear logging to track the entire data pipeline.

📁 Project Structure
graphql
Kopiera
Redigera
Fördjupad_Pythonprogrammering/
├── api.py                  # Class to load data from a CSV file
├── datacleaner.py          # Class to clean specific columns in the dataset
├── datasaver.py            # Class to save the cleaned data to a SQLite database
├── main.py                 # Main script that integrates the pipeline
├── country_comparison_dataset.csv  # Dataset used for the analysis
├── history_plot.png        # Optional plot or diagram
├── log.log                 # Generated log file (after running the pipeline)
├── README.md               # Project documentation
🧠 Project Overview
This Python project builds a data pipeline that:

Extracts data from a CSV file via api.py.

Cleans specific fields (such as GDP) using datacleaner.py.

Loads the cleaned data into an SQLite database using datasaver.py.

Key Features:
Logging: Each part of the pipeline logs its activity to ensure smooth debugging and tracking.

Data Pipeline: Fetch → Clean → Save. The modules interact seamlessly to process the dataset.

📦 Requirements
You need Python 3.7+ installed along with the required packages. Install them using:

bash
Kopiera
Redigera
pip install pandas sqlite3
🚀 How to Run
Clone the repository:

bash
Kopiera
Redigera
git clone https://github.com/Jesper0101/F-rdjupad_Pythonprogrammering.git
cd F-rdjupad_Pythonprogrammering
Ensure the dataset country_comparison_dataset.csv is available at the specified path, or update the file_path in api.py.

Run the main script:

bash
Kopiera
Redigera
python main.py
This will:

Fetch the raw data from the dataset.

Clean the data (removing non-numeric GDP values).

Save the cleaned data into an SQLite database (database.db).

Check the log file (log.log) for details on the pipeline progress, such as fetching data, cleaning, and saving.

🛠 Module Breakdown
api.py
Fetches the dataset from a CSV file.

Includes logging for success, errors (file not found, empty file), and progress.

datacleaner.py
Cleans the GDP (in Trillions USD) column by removing any non-numeric characters.

Ensures that invalid data (such as text in the GDP field) is replaced with NaN.

datasaver.py
Saves the cleaned data into an SQLite database (database.db).

Handles errors related to database operations and logs progress.

main.py
Coordinates the data pipeline by:

Fetching the data from the CSV file using api.py.

Cleaning the data using datacleaner.py.

Saving the cleaned data to SQLite using datasaver.py.

Logs the entire process, including any issues that arise.

Logging Configuration (main.py)
Configures logging for the entire pipeline to track the progress of fetching, cleaning, and saving data.

Logs are stored in the file log.log, and each step in the pipeline is logged with timestamped entries.
