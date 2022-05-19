from comm import FilePath
import yaml
import xlrd


class OpenExcel:

    def openYaml(self, file, filename):
        with open(FilePath.path_file(file, filename), 'r') as f:
            return yaml.load(f, Loader=yaml.Loader)

    def open_excelsheet(self, file, filename, sheetname=0):
        data = xlrd.open_workbook(FilePath.path_file(file, filename))
        return data.sheet_by_index(sheetname)

    def open_excelvalue(self, file, filename, sheetname):
        data = []
        title = self.open_excelsheet(file, filename, sheetname).row_values(0)
        rows = self.open_excelsheet(file, filename, sheetname).nrows
        for f in range(1, rows):
            row_value = self.open_excelsheet(file, filename, sheetname).row_values(f)
            data.append(dict(zip(title, row_value)))
        return data


class ExcelVarles:
    case_id = "用例ID"
    case_module = "用例模块"
    case_name = "用例名称"
    case_url = "用例地址"
    case_method = "请求方式"
    case_type = "请求类型"
    case_data = "请求参数"
    case_headers = "请求头"
    case_preposition = "前置条件"
    case_isRun = "是否执行"
    case_code = "状态码"
    case_result = "期望结果"



a=OpenExcel()
b=a.openYaml('apis','data.yaml')

print(b)