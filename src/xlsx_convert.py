import pandas as pd

def convert_xlsx_to_csv(xlsx_file, csv_file):
    try:
        df = pd.read_excel(xlsx_file)  # Read the XLSX file using pandas
        df.to_csv(csv_file, index=False)  # Convert and save as CSV
        print(f"Conversion successful! CSV file '{csv_file}' created.")
    except Exception as e:
        print(f"Conversion failed. Error: {str(e)}")

# Example usage
xlsx_file_path = 'data/base_files/coded_notes.xlsx'  # Path to your XLSX file
csv_file_path = 'data/coded_notes.csv'  # Path to the output CSV file

convert_xlsx_to_csv(xlsx_file_path, csv_file_path)

