import xlrd

loc = input("input file path")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

print(sheet.ncols, sheet.nrows)