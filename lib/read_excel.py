import xlrd
from config.config import *

def get_data(file_name,sheet_name,case_name):
    wb = xlrd.open_workbook(file_name)
    sh = wb.sheet_by_name(sheet_name)
    for i in range(1, sh.nrows):
        if sh.cell(i, 0).value == case_name:
            return sh.row_values(i)

if __name__ == '__main__':
    case_data = get_data(data_file, 'Testaddfuel', 'test_add')  #没有路径，这样的结构获取不到excel文件
    print(case_data)
    print(case_data[3])
    print(case_data[4])
