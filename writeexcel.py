import openpyxl

path = r"C:\Users\ADMIN\Desktop\sel_testing.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active

# writing data into this sheet in particular rows and columns
for r in range(1, 6):
 for c in range(1, 4):
  sheet.cell(row=r, column=c).value="welcome"

workbook.save(path)