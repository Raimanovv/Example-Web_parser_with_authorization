import xlsxwriter
from file_scraping import array


def writer(parametr):
    book = xlsxwriter.Workbook(r'C:\Users\rusta\Desktop\data.xlsx')
    page = book.add_worksheet("Цитаты")

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 100)
    page.set_column("C:C", 50)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        row += 1

    book.close()


writer(array)
