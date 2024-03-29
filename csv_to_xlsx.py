import csv
from openpyxl import Workbook


def txt_to_excel(input_txt_file, output_excel_file):
    # Create a new Excel workbook and add a worksheet.
    wb = Workbook()
    ws = wb.active

    with open(input_txt_file, 'r') as txt_file:
        # Use csv.reader with delimiter as whitespace
        reader = csv.reader(txt_file, delimiter=' ', skipinitialspace=True)

        for row in reader:
            # Separate all columns except the last one
            first_columns = row[:-1]
            # Get the last column
            last_column = row[-1]

            # Append the first columns as one column
            ws.append([' '.join(first_columns), last_column])

    # Save the data to an Excel file
    wb.save(output_excel_file)


if __name__ == "__main__":
    input_txt_file = "/Users/jaclyncohen/Desktop/birthRecords/newrecs/08262022.txt"
    output_excel_file = "output.xlsx"  # Desired name for the output Excel file

    txt_to_excel(input_txt_file, output_excel_file)
    print(
        f"Data from {input_txt_file} has been written to {output_excel_file}")
