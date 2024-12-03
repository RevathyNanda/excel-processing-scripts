import pandas as pd

# Function to get column names for extraction from the user
def get_columns_to_extract(data):
    print("Available columns in the Excel sheet:")
    print(list(data.columns))  # Display all column names
    print("Enter the columns you want to extract (comma-separated).")
    user_input = input("Columns to extract: ").strip()
    columns = [col.strip() for col in user_input.split(",")]
    return columns

# Main script
def main():
    # Step 1: Load the Excel file
    file_path = input("Enter the path to your Excel file: ").strip()
    data = pd.read_excel(file_path)
    
    # Step 2: Get the columns to extract from the user
    columns_to_extract = get_columns_to_extract(data)
    
    # Step 3: Validate and extract columns
    try:
        extracted_data = data[columns_to_extract]
    except KeyError as e:
        print(f"Error: One or more columns do not exist: {e}")
        return
    
    # Step 4: Save the extracted data to a new Excel file
    output_file_path = file_path.replace(".xlsx", "_Extracted.xlsx")
    extracted_data.to_excel(output_file_path, index=False)
    print(f"Extracted columns saved to: {output_file_path}")

if __name__ == "__main__":
    main()
