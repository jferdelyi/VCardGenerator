"""
This small script can generate a valid .vcf (vCard) from CSV file. It will ask you to fill
in some details and write the vcf file.
"""

import csv
import tkinter as tk
from tkinter import filedialog as fd

# Convert CSV to VCard
# @param filename input CSV filename
def convert(filename: str) -> None:
    data = read_csv(filename)
    vcf_file = f'{filename.split(".csv")[0]}.vcf'
    vcards = []
    ok = True
    for d in data:
        first_name = ""
        if len(d) > 0:
            first_name = d[0]
        
        last_name = ""
        if len(d) > 1:
            last_name = d[1]
        
        tel = ""
        if len(d) > 2:
            tel = d[2]

        mobile = ""
        if len(d) > 3:
            mobile = d[3]

        email = ""
        if len(d) > 4:
            email = d[4]

        note = ""        
        if len(d) > 5:
            note = d[5]
            
        vcards.extend(make_vcard(first_name, last_name, tel, mobile, email, note))
    write_vcard(vcf_file, vcards)
    text.set("Done!")

# Create VCard data
# @param last_name last name
# @param first_name first name
# @param tel telephone
# @param mobile mobile phone
# @param email email
# @param note note
def make_vcard(last_name: str, first_name: str, tel: str, mobile: str, email: str, note: str) -> None:
    return [
        'BEGIN:VCARD',
        'VERSION:2.1',
        f'N:{last_name};{first_name}',
        f'FN:{first_name} {last_name}',
        f'EMAIL;PREF;INTERNET:{email}',
        f'TEL;HOME;VOICE:{tel}',
        f'TEL;HOME;VOICE:{mobile}',
        f'NOTE:{note}',
        f'REV:1',
        'END:VCARD'
    ]

# Read CSV contact file
# FIRSTNAME, NAME, TEL, MOBILE, EMAIL, NOTES
# @param filename the CSV filename
def read_csv(filename: str) -> list:
    data = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader, None)  # Skip the header line
        for row in spamreader:
            data.append(row)
        
    return data

# Write the VCard
# @param filename the VCF filename
# @param data the VCard data
def write_vcard(filename: str, data: list) -> None:
    with open(filename, 'w') as f:
        f.writelines([l + '\n' for l in data])

# Define picker of files
def picker() -> None:
    filetypes = (('CSV file', '*.csv'),)
    filename = fd.askopenfilename(title='Select the file', initialdir='.', filetypes=filetypes)
    convert(filename)

# Main
if __name__ == "__main__":
    root = tk.Tk()
    root.title("CSV to VCard")
    root.resizable(False, False)
    root.iconphoto(False, tk.PhotoImage(file='./icon.png'))
    root.geometry("300x100")
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)

    button = tk.Button(root, text='Select CSV file', command=picker)
    button.grid(column=0, row=0)

    text = tk.StringVar()
    text.set("Waiting")

    label = tk.Label(root, textvariable=text)
    label.grid(column=0, row=1)

    root.mainloop()
