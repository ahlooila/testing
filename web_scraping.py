import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import requests
from bs4 import BeautifulSoup

url = ('xxx')

html_page=requests.get(url, verify=False).text
soup=BeautifulSoup(html_page,'lxml')
df=pd.read_html(url,header=0)
header1=soup.find('div",class_='row inner-conent sibro')
header2=header1.find('p',class_='para-semibold').text
                  
first_table=df[0]
writer=pd.ExcelWriter('sample.xlsx')
first_table.to_excel(writer,sheet_name='Sheet1',startrow=1)
writer.save()
                  
         
