# Excel Column Extraction Script

This script allows users to extract specific columns from an Excel file based on their input. It is designed to simplify data manipulation tasks by providing an interactive way to specify which columns to extract.

## Features

- Displays all available columns in the Excel file.
- Prompts the user to specify columns for extraction.
- Validates column names and handles errors gracefully.
- Saves the extracted data to a new Excel file with a clear naming convention.

## How to Use

1. **Install Required Libraries**  
   Ensure you have the `pandas` library installed. You can install it using:
   ```bash
   pip install pandas openpyxl
2. **Run the Script**
   Save the script as `extract_columns.py` and execute it using:

    `python extract_columns.py`

3. **Provide User Inputs**
   Enter the path to your Excel file (e.g., data.xlsx).
   Review the list of available columns displayed in the terminal.
   Enter the names of the columns you want to extract, separated by commas (e.g., column1, column2).

4. **Output**
    The script will save the extracted columns to a new file with _Extracted appended to the original filename (e.g., data_Extracted.xlsx).

5. **Example**
   Input
   Excel File: sample_data.xlsx
   Available Columns: ['ID', 'Name', 'Age', 'Gender', 'Score']
   User Input: Name, Score
   Output

   New File: sample_data_Extracted.xlsx
   Extracted Data:

   Name, Score
   Alice, 95
   Bob, 87
   Charlie, 92

6. **Error Handling**
   File Not Found: The script will alert you if the specified file cannot be found.
   Invalid Columns: If one or more specified columns do not exist, the script will display an error and terminate.
