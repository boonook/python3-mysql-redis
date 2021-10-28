import xlrd
import json
excel_path = "excel/city.xlsx" 
def readxlsxfile():
    excel = xlrd.open_workbook(excel_path,encoding_override="utf-8")
    all_sheet = excel.sheets()
    city_json = []
    for index,sheet in enumerate(all_sheet):
        item_list = sheet._cell_values
        datasource = []
        for i,item in enumerate(item_list):
            # print(i)
            # print(item)
            if i>0:
                dict = {'org':item[0], 'dst':item[1], 'date':item[2],'rdate':item[3],'realprice':item[4],'body':item[6]}
                datasource.append(dict)
            else:
                print(item)
        city_json.append({'name':sheet.name,'data':datasource})               
            # print((sheet._cell_values)[1])
    data2 = json.dumps(city_json,ensure_ascii=False)
    f = open('filename.json','w',encoding='utf-8')
    f.write(data2)
    f.close()  
    # print(data2)