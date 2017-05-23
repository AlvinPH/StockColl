#from pandas import read_html
import pandas as pd
from pandas import DataFrame
#import numpy as np

import requests
from bs4 import BeautifulSoup


url = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
#Save_name = 'CollectedStock.xlsx'
Save_name = ''

r = requests.get(url)#get html data

if r.status_code == requests.codes.ok:
    print('Requests OK')

    soup = BeautifulSoup(r.text, 'html.parser')
    FindTag = soup.find_all('td')
    CodeList = []
    NameList = []
    IndList = []
    for i in range(8, len(FindTag), 7):
            Text = FindTag[i].get_text()
            StockCode = Text[0:4]
            StockName = Text[5:]
            if not StockCode.isdigit():
                break
            CodeList.append(StockCode)
            NameList.append(StockName)
            Ind = FindTag[i+4].get_text()
            IndList.append(Ind)
            Stock_Num = len(CodeList)
            print('Stock Number = %d' % Stock_Num)

            df1 = DataFrame({'code':CodeList, 'name':NameList, 'Ind':IndList})

    if Save_name.endswith('.xlsx'):
        print('Start Save')
        writer = pd.ExcelWriter(Save_name, engine = 'xlsxwriter')
        df1.to_excel(writer, sheet_name='Sheet1')
        writer.save()

else:
    print('Requests Fail')



print('Finish')