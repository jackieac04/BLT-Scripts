This repo contains scripts created for the BLT Lab at Brown University meant
to convert txt data into more readable formats: records-cleaning transfers rows with emails and rows without emails into separate files, while csv to xlsx converts these files into sheets.

The csv converter splits the last column separately from the rest of the columns so that emails can be parsed different from addresses and names.

The main branch splits the files into two columns where the second column in just meant for emails, while the all cols branch splits by space into each column.
