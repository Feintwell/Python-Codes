import openpyxl

workbook = openpyxl.load_workbook("hello_world.xlsx")
sheet = workbook.active

# 2. Find the last row with data in Column A
# We start from the top and find where the data ends
last_row_a = sheet.max_row
while last_row_a > 0 and sheet.cell(row=last_row_a, column=1).value is None:
    last_row_a -= 1

# If Column A is completely empty, we start at row 1. 
# Otherwise, we start pasting on the row right after the last data point.
destination_row = max(1, last_row_a + 1)

# 3. Iterate through Column B, starting from row 2 (skipping the header)
for row in range(2, sheet.max_row + 1):
    b_value = sheet.cell(row=row, column=2).value
    
    # Optional: Skip empty cells in Column B so you don't paste blanks
    if b_value is not None:
        # Write the value to Column A at the next available slot
        sheet.cell(row=destination_row, column=1).value = b_value
        destination_row += 1

workbook.save("hello_world.xlsx")
print("Data from Column B successfully appended below Column A!")
