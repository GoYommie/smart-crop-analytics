# Import built-in Python library for reading CSV files
import csv

# Import the CropData model (this connects to the database table)
from crops.models import CropData


# Open the CSV file that contains the crop dataset
# newline='' ensures proper reading of rows
# encoding='utf-8-sig' removes hidden BOM characters from Excel files
with open('crop_data.csv', newline='', encoding='utf-8-sig') as csvfile:
    
    # DictReader reads each row as a dictionary:
    # Example: {'year': '2022', 'region': 'Alberta', ...}
    reader = csv.DictReader(csvfile)

    # Loop through each row in the CSV file
    for row in reader:
        
        # Get the 'year' value and remove extra spaces
        year = row['year'].strip()

        # Skip rows where year is missing or invalid
        # '(blank)' comes from Excel when cells are empty
        if not year or year == '(blank)':
            continue  # skip this row and move to next one

        # Create a new record in the database table (crops_cropdata)
        CropData.objects.create(

            # Convert year to integer (database expects number)
            year=int(year),

            # Clean region text by removing extra spaces
            region=row['region'].strip(),

            # Clean crop name text
            crop=row['crop'].strip(),

            # Convert production to float (decimal number)
            # If empty, store as NULL in database (None in Python)
            production=float(row['production']) if row['production'] else None,

            # Convert yield to float
            # If empty, store as NULL
            yield_amount=float(row['yield']) if row['yield'] else None
        )