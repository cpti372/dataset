from bs4 import BeautifulSoup
from selenium import webdriver
import time 
import openpyxl
driver = webdriver.Chrome("./chromedriver")

driver.get("https://www1.president.go.kr/petitions/best?page=1")
#for i in range(1,11):
  #  print("https://www1.president.go.kr/petitions/best?page="+str(i))

for i in range(1,10):
    driver.get("https://www1.president.go.kr/petitions/best?page="+str(i))
    soup=BeautifulSoup(driver.page_source,'html.parser')
    result=[]
    for i in soup.select("#cont_view > div.cs_area > div > div > div.board.text > div.b_list.category > div.bl_body > ul > li"):
        print(i.find("div",class_="bl_subject").text[3:].strip())
        result.append(i.find("div",class_="bl_subject").text[3:].strip())
    time.sleep(5)
driver.close()
from openpyxl import Workbook
write_workbook=openpyxl.Workbook()
write_cell=write_workbook.active
for i in range(1,len(result)+1):
    write_cell.cell(i,1,result[i-1])
write_workbook.save("bluehouse.xlsx")