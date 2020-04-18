#네이트에서 엔시티 검색어 scrapper
import requests
from bs4 import BeautifulSoup
from scrap2 import extract_url,nct
max_nct_pages=extract_url()
print(nct(max_nct_pages))