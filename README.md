# Fördjupad Pythonprogrammering – Country Comparison Data Pipeline

A modular Python ETL pipeline for processing and analyzing country comparison data, demonstrating advanced programming techniques with proper logging and error handling.

## Project Structure
```bash 
Fördjupad_Pythonprogrammering/
├── api.py                  # Loads data from a CSV file
├── datacleaner.py          # Cleans specific fields in the dataset
├── datasaver.py            # Saves the cleaned data to a SQLite database
├── main.py                 # Main script that ties everything together
├── country_comparison_dataset.csv  # Dataset used for the analysis
├── history_plot.png        # Optional visualization or schedule diagram
├── log.log                 # Generated log file (after running)
├── README.md               # Project documentation
```

## Project Overview
This project implements a basic ETL (Extract, Transform, Load) pipeline using pandas, regular expressions, and SQLite:

- **Extract** – Read a dataset from a CSV file using `api.py`.
- **Transform** – Clean the GDP (in Trillions USD) column using `datacleaner.py`.
- **Load** – Save the cleaned dataset to an SQLite database using `datasaver.py`.

The pipeline handles country comparison data including GDP, population, and other metrics for various countries with proper error handling and logging throughout the process.

## Dataset Information
The dataset contains comparison metrics for multiple countries including:
- Country names
- Population figures
- GDP values (in Trillions USD)
- Military spending
- Geographic data
- And more

The primary cleaning operation focuses on the GDP column, which requires reformatting from strings (like "$21.4T") to proper floating-point values (21.4).

## Requirements
Make sure you have Python 3.7+ and the following packages installed:
```bash
pip install pandas numpy sqlite3
```

## Configuration
Key configuration options can be modified in the respective modules:
- Input file path: Set in `api.py`
- Database name: Set in `datasaver.py` (default: `database.db`)
- Log file path: Set in `main.py` (default: `log.log`)

## How to Run
Clone the repository:

```bash
git clone https://github.com/Jesper0101/F-rdjupad_Pythonprogrammering.git
cd F-rdjupad_Pythonprogrammering
```

Make sure the dataset file `country_comparison_dataset.csv` is located in the correct path or update `api.py` to reflect its location.

Run the main script:

```bash
python main.py
```

On successful execution:
- A cleaned version of the dataset is saved to `database.db` in the `cleaned_data` table.
- Logs are recorded in `log.log`.

## Example Data Transformation

Before cleaning:
```
Country  GDP (in Trillions USD)  Population
USA      $21.4T                  331 million
China    $14.3T                  1.4 billion
Japan    $5.1T                   126 million
```

After cleaning:
```
Country  GDP (in Trillions USD)  Population
USA      21.4                    331 million
China    14.3                    1.4 billion
Japan    5.1                     126 million
```

## Module Breakdown

### api.py
- Loads the dataset using `pandas.read_csv`.
- Includes logging and error handling for missing or empty files.
- Returns a pandas DataFrame or raises an exception if the file is inaccessible.

### datacleaner.py
- Cleans the GDP (in Trillions USD) column using regular expressions.
- Converts the cleaned data into floats, handling invalid entries with NaN.
- Provides detailed logging of the cleaning process.

### datasaver.py
- Saves a DataFrame into a SQLite database using `sqlite3`.
- Creates or replaces the `cleaned_data` table.
- Includes error handling for database operations.

### main.py
- Orchestrates the pipeline: load → clean → save.
- Sets up logging configuration for the entire application.
- Provides proper error handling and execution flow.

## Logging Details
The application logs information at multiple levels:
- INFO: General progression through the pipeline stages
- WARNING: Non-critical issues (e.g., missing values)
- ERROR: Critical problems that prevent successful execution
- DEBUG: Detailed information useful for troubleshooting

Log entries include timestamps and the module that generated them for easy debugging.

## Error Handling
The pipeline handles several error scenarios:
- Missing input files
- Corrupt data in the CSV
- Database connection issues
- Invalid data types

If you encounter an error, check the log file for details about what went wrong and where.

## Dataset
Download the dataset from:

[Country Comparison Dataset (USA & More) – Kaggle](https://www.kaggle.com/datasets/waqi786/country-comparison-dataset-usa-and-more#)

## License
This project is open-source and available under the [MIT License](https://mit-license.org/).

## Author
Jesper – [GitHub Profile](https://github.com/Jesper0101)

For questions or suggestions, feel free to open an issue!
