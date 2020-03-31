from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")

driver.get("https://www1.president.go.kr/petitions/best?page=1")

soup=BeautifulSoup(driver.page_source,'html.parser')
result=[]
for i in soup.select("#cont_view > div.cs_area > div > div > div.board.text > div.b_list.category > div.bl_body > ul > li"):
 print(i.find("div",class_="bl_subject").text[3:].strip())
 result.append(i.find("div",class_="bl_subject").text[3:].strip())
driver.close()
