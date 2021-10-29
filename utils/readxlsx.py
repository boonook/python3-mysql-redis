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
                item_6 = item[6].strip(',')
                print(eval(item_6.org))
                # print(str(i)+str('----')+item_6)
                # dict = {'org':item[0], 'dst':item[1], 'date':item[2],'rdate':item[3],'realprice':item[4],'body':{'org':item[6].org,'dst':item[6].dst,'orgcn':item[6].orgcn,'dstcn':item[6].dstcn,'date':item[6].date,'rdate':item[6].rdate,'period':item[6].period,'notaxprice':item[6].notaxprice}}
                # datasource.append(dict)
            else:
                print(item)
        city_json.append({'name':sheet.name,'data':datasource})               
            # print((sheet._cell_values)[1])
    data2 = json.dumps(city_json,ensure_ascii=False,separators=(',',':'),indent=2)
    f = open('filename.json','w',encoding='utf-8')
    f.write(data2)
    f.close()  
    # print(data2)