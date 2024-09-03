import pandas as pd

# Load the CSV file
df = pd.read_csv('contacts.csv')

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

    # Save to a .vcf file
    with open(f"{row['First Name']}_{row['Last Name']}.vcf", "w") as file:
        file.write(vcard)
