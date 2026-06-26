import csv
import os
import openpyxl


def work():
    #Dynamically get the folder where THIS script is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))

    #Join that folder path with your file names. Make sure the files are in the same folder as the script
    input_excel = os.path.join(script_dir, "test.xlsx")
    output_csv = os.path.join(script_dir, "test1.csv")

    # Check if the Excel file exists in that specific folder
    if not os.path.exists(input_excel):
        print(f"Error: Could not find 'test.xlsx' at this location:\n{input_excel}")
        print("\nPlease make sure 'test.xlsx' is inside that exact folder!")
        return

    print(f"Opening Excel file: {input_excel}...")
    wb = openpyxl.load_workbook(input_excel, data_only=True)
    sheet = wb.active

    headers = [cell.value for cell in sheet[1]]

    try:
        code_idx = headers.index("Code")
        name_idx = headers.index("Name")
        desc_idx = headers.index("Description")
    except ValueError:
        print(
            f"Error: Could not find all required headers ('Code', 'Name', 'Description')."
        )
        print(f"Found headers: {headers}")
        return

    csv_headers = ["Column A", "Name", "Column C", "Column D", "Short Description"]

    print(f"Writing data to CSV: {output_csv}...")

    with open(output_csv, mode="w", encoding="utf-8-sig", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(csv_headers)

        for row in sheet.iter_rows(min_row=2, values_only=True):
            if not any(row):
                continue

            code = str(row[code_idx]).strip() if row[code_idx] is not None else ""
            name = str(row[name_idx]).strip() if row[name_idx] is not None else ""
            description = (
                str(row[desc_idx]).strip() if row[desc_idx] is not None else ""
            )

            short_description = f"<h4>{name}\n{code}</h4>\n\n{description}"
            csv_row = ["", code, "", "", short_description]
            writer.writerow(csv_row)

    print(f"\nSuccess! 'test1.csv' is filled\n{output_csv}")


if __name__ == "__main__":
    work()
