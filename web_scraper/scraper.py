import requests
from bs4 import BeautifulSoup

def get_citations_needed_count():
    URL=input('please input wikipedia link here >>   ')
    page_content=requests.get(URL).content
    soup=BeautifulSoup(page_content,'html.parser')
    parent_paras=soup.find_all('p')
    counter=[]
    for i in parent_paras:
        count=i.find_all('sup',class_="noprint Inline-Template Template-Fact")
        if count != []:
            counter.append(count)
            text=i.get_text().strip()
    print(f"number of citations needed    {len(counter)}")
    print('**'*40)

def get_citations_needed_report():
    URL=input('please input wikipedia link here >>   ')
    page_content=requests.get(URL).content
    soup=BeautifulSoup(page_content,'html.parser')
    parent_paras=soup.find_all('p')
    counter=[]
    for i in parent_paras:
        count=i.find_all('sup',class_="noprint Inline-Template Template-Fact")
        if count != []:
            counter.append(count)
            text=i.get_text().strip()
            print(f'the paragraph:  {text}')
            print('**'*40)
            print('**'*40)
    

## to test each function call it by itself
## i tested https://en.wikipedia.org/wiki/History_of_Malawi, https://en.wikipedia.org/wiki/History_of_Mali
## https://en.wikipedia.org/wiki/History_of_sudan and  https://en.wikipedia.org/wiki/History_of_jordan 
## and all worked nicely!
get_citations_needed_count()
get_citations_needed_report()