import pandas as pd
import os

# Load the CSV file
csv_file_path = '/Users/jordanallen/Desktop/contacts.csv'
df = pd.read_csv(csv_file_path)

# Directory to save the .vcf files
output_directory = os.path.dirname(csv_file_path)

for index, row in df.iterrows():
    # Start the vCard content
    vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{row['Last Name']};{row['First Name']}
FN:{row['First Name']} {row['Last Name']}
TEL;TYPE=CELL:{row['Phone Number']}
EMAIL:{row['Email Address']}
END:VCARD
"""

    # Save to a .vcf file in the same directory as the CSV file
    file_name = f"{row['First Name']}_{row['Last Name']}.vcf"
    file_path = os.path.join(output_directory, file_name)
    with open(file_path, "w") as file:
        file.write(vcard)
