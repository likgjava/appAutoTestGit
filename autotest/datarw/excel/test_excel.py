import xlrd
import xlwt
import xlutils.copy
from xlwt import Font, XFStyle


def read():
    # workbook = xlrd.open_workbook('low.xls')
    workbook = xlrd.open_workbook('high.xlsx')

    sheet_names = workbook.sheet_names()
    print('sheet_names=', sheet_names)

    sheet = workbook.sheet_by_index(0)
    print('sheet=', sheet)

    nrows = sheet.nrows
    ncols = sheet.ncols
    print('nrows=', nrows)
    print('ncols=', ncols)

    for rownum in range(nrows):
        row = sheet.row(rownum)
        # print(row)
        row_values = sheet.row_values(rownum)
        print(row_values)

    cell = sheet.cell(0, 0)
    print(cell)
    print('ctype={} value={}'.format(cell.ctype, cell.value))


def create():
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('学生')
    sheet.write(0, 0, 'hello')
    workbook.save('new.xlsx')


def update():
    workbook = xlrd.open_workbook('new.xls', formatting_info=True)

    copybook = xlutils.copy.copy(workbook)

    sheet = copybook.get_sheet(0)
    sheet.write(1, 1, '中国12')
    copybook.save('new.xls')


def set_cell_value_of_link():
    """
    向单元格中插入图片链接
    """
    workbook = xlrd.open_workbook('new.xls', formatting_info=True)
    copybook = xlutils.copy.copy(workbook)
    sheet = copybook.get_sheet(0)

    font = Font()
    font.underline = Font.UNDERLINE_DOUBLE
    font.colour_index = 4
    h_style = XFStyle()
    h_style.font = font

    s = 'HYPERLINK("{}";"截图")'.format('img/a.png')
    sheet.write(8, 8, xlwt.Formula(s), h_style)
    copybook.save('new.xlsx')


# read()
# create()
# update()
set_cell_value_of_link()
