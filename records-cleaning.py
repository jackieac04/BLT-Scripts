"""
Clean up txt files
Export to csv
"""

import os
import re
import glob
from datetime import date

today = date.today()
file_date = today.strftime("%Y-%m-%d")
# print(file_date)

# Heather's folder path
# folder_path = "G:\\Shared drives\\Brown CLPS Shared Dev Database\\Recruitment\\birth-records"
# Annika's folder path
# folder_path = "/Users/annika/Library/CloudStorage/GoogleDrive-annika_mcdermott-hinman@brown.edu/Shared drives/Brown CLPS Shared Dev Database/Recruitment/birth-records"
# Jackie's foler path
folder_path = "/Users/jaclyncohen/Desktop/birthRecords/newrecs/"

symb = "@"


# List of Emails
emails = list()
no_emails = list()
# Find every txt file in this folder
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
    print(filename)
    # try to open
    try:
        file = open(filename, 'r')
    except:
        "An error occured."
    else:
        lines = file.readlines()
        file.close()
        # New list
        rows = list()
        for line in lines:
            line = line.strip()
            # Separate each word
            new_line = re.split("\t", line)
            # Add the elements to the new list
            rows += (new_line)
            # print(rows[0])
        # if @ symbol is in the indexed row, add it to the email list
        for word in rows:
            if symb in word:
                emails.append(word)
                # print(word)
            else:
                no_emails.append(word)


for i, email in enumerate(emails):

    new_email = email.replace(",", ".")
    new_email = new_email.replace("@@", "@")
    new_email = new_email.replace("LCOM", "L.COM")
    new_email = new_email.replace(".VOM", ".COM")
    new_email = new_email.replace(".COME", ".COM")
    new_email = new_email.replace(".COMN", ".COM")
    new_email = new_email.replace("`", "")
    new_email = new_email.replace("..", ".")
    new_email = (new_email.split(symb, 1)[
                 0])+symb+(new_email.split(symb, 1)[1]).replace("GAMIL.", "GMAIL.")
    new_email = (new_email.split(symb, 1)[
                 0])+symb+(new_email.split(symb, 1)[1]).replace("GMIL.", "GMAIL.")
    new_email = (new_email.split(symb, 1)[
                 0])+symb+(new_email.split(symb, 1)[1]).replace("GMAL.", "GMAIL.")
    new_email = (new_email.split(symb, 1)[
                 0])+symb+(new_email.split(symb, 1)[1]).replace("GAIL.", "GMAIL.")
    new_email = (new_email.split(symb, 1)[
                 0])+symb+(new_email.split(symb, 1)[1]).replace("GNAIL.", "GMAIL.")
    new_email = (new_email.split(symb, 1)[
                 0])+symb+(new_email.split(symb, 1)[1]).replace("GMAIAL.", "GMAIL.")
    new_email = (new_email.split(symb, 1)[
                 0])+symb+(new_email.split(symb, 1)[1]).replace("FMAIL.", "GMAIL.")
    new_email = (new_email.split(symb, 1)[
                 0])+symb+(new_email.split(symb, 1)[1]).replace("GMAI.", "GMAIL.")
    new_email = (new_email.split(symb, 1)[
                 0])+symb+(new_email.split(symb, 1)[1]).replace("MIAL", "MAIL")
    new_email = (new_email.split(symb, 1)[
                 0])+symb+(new_email.split(symb, 1)[1]).replace("ICOLUD", "ICLOUD")
    new_email = (new_email.split(symb, 1)[
                 0])+symb+(new_email.split(symb, 1)[1]).replace("ICLOULD", "ICLOUD")
    new_email = new_email.replace("GMAILL.", "GMAIL.")
    if ".COM" not in new_email:
        new_email += ".COM"
    new_email = new_email.replace(".EDU.COM", ".EDU")
    new_email = new_email.replace(".ORG.COM", ".ORG")
    new_email = new_email.replace(".NET.COM", ".NET")
    emails[i] = new_email


# Make a new text file containing new emails
try:
    # For PC
    # new_file = open(folder_path+"\\"+file_date+"_emails.txt", "w")
    # For Mac
    new_file = open(folder_path+"/"+file_date+"_emails.txt", "w")
    new_file_no_emails = open(folder_path+"/"+file_date+"no_emails.txt", "w")
    for email in emails:
        new_file.write(email)
        new_file.write("\n")
    new_file.close()
    for no_email in no_emails:
        new_file_no_emails.write(no_email)
        new_file_no_emails.write("\n")
    new_file.close()
except Exception as error:
    print("something went wrong!", error)
