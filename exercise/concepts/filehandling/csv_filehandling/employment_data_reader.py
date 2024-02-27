import csv

# Define the file path
file_path = "employment-data-sep-2023.csv"  

# Open the CSV file
with open(file_path, "r", encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    next(csv_reader)
    #or read a specific header
    print(f"Seventh Column Header: {next(csv_reader)[7]}")
    
        
    # Print the seventh column for each row
    for row in csv_reader:
        print(row[7])