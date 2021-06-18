
# def getINV(PID):
#     from openpyxl import Workbook
#     import xlwings as xw
#     # import win32com.client as win32 
#     app = xw.App()
#     # excel = win32.gencache.EnsureDispatch('Excel.Application')
#     path="S:\\開放公用區\★每日更新庫存水位警示表★\★庫存水位-唯讀參閱不可修改★.xlsm"
#     wb = Workbook()
#     wb = xw.Book(path)
#     # print(wb.sheets[0].range('A2').value)
#     # print(wb.sheets[0].range('B2').value)
#     # print(wb.sheets[0].range('C2').value)
#     # print(wb.sheets[0].range('D2').value)
#     # print(wb.sheets[0].range('D2').address)
#     # myCell = wb.sheets[0].api.UsedRange.Find('11103035')
#     # print('---------------')
#     # print (myCell.address)

#     ws=wb.sheets[0]
#     # 使用範囲
#     u = ws.api.UsedRange
#     r = u.Row + u.Rows.Count - 1
#     c = u.Column + u.Columns.Count - 1
#     rng = ws.range((1, 1), (r, c))
#     # print("u="+str(u))
#     print("r="+str(r))
#     print("c="+str(c))
#     # 使用範囲の値(list)を取得して出力
#     # print(rng.value)


#     import math

#     # print("wb.sheets[0].max_row = "+wb.sheets[0].max_row)
#     # excel.Application.Quit()
#     data=PID
#     # print("wb.sheets[0].max_row = "+wb.sheets['Sheet'].max_row)
#     print(round(2.5))
#     v=round(ws.range(2, 4).value)
#     print(v)
#     sum=0
#     try:
#         for i in range(2,r+1):
#             # print(i)
#             # print(round(ws.range(i, 4).value))
#             # print(data)
#             #比對品號，找出列
#             if str(round(ws.range(i, 4).value)) == data:
#                 # print("i="+str(i))
#                 # print(str(round(ws.range(i, 7).value)))
#                 print("sum="+str(sum)))
#                 sum=sum+int(round(ws.range(i, 7).value))
#     except:
#         print("無資料")
            


#     wb.close()
#     app.quit()
#     return sum



    