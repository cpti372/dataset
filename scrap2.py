#네이트 판에 있는 엔시티 게시글 제목 긁어오기 
import requests
from bs4 import BeautifulSoup

url="https://pann.nate.com/fantalk/117809?"

def extract_url():
#url 상태를 리턴해준다.
    nct=requests.get(url)
    #print(nct.status_code)
    nct_soup=BeautifulSoup(nct.text,"html.parser")
    #html이 다출력인데 print(nct_soup), 페이지 출력 
    pagination=nct_soup.find("div",{"class":"paginate space"}) 
    #print(pagination)
    pages=pagination.find_all('a')
    nct_list=[]
    for page in pages[:-1]:#다음은 빼고 계산 
        nct_list.append(int(page.string))
    #print(nct_list[-1])#마지막꺼 제외
    max_page=nct_list[-1]
    return max_page


def nct(last_page):

    for page in range(last_page):
        #페이지 자동으로 이동 
        result=requests.get(url+"page={}".format(page+1))
        soup=BeautifulSoup(result.text,"html.parser")
        result3=soup.find_all("td",{"class":"subject"})
        for item in result3:
            #태그 빼고 텍스트만 
            print(item.getText())