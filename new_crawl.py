import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd

url_temp= "https://in.indeed.com/jobs?q={}&l={}&start={}"
base_link="https://in.indeed.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
def get_href(url_temp,position,city):
    results_per_city=200
    href_list=[]
    for start in range(0,results_per_city+10,10):
        url=url_temp.format(position,city,start)
        r=requests.get(url,headers=headers)
        soup=BeautifulSoup(r.text,"html.parser")    
       
        for i in soup.find_all('a'):
            # if tag has attribute of class
            if i.has_attr( "href" ):
                k=i['href']
                href_list.append(base_link+k)
    
    return href_list
  
def get_job_links(href_list):
    job_links=[]
    for a in href_list:
        if a.find('/rc/clk')!=-1:
            job_links.append(a)
        elif a.find('/company/')!=-1:
            job_links.append(a)
    return job_links
  
def get_job_df(job_links,city):
    df=pd.DataFrame(columns=["job_location", "job_title", "company", "job_description"])
    
    for i in job_links:
        req=requests.get(i,headers=headers)
        soup_req=BeautifulSoup(req.text,"html.parser")
        try:
            title=soup_req.find('h1',{'class': 'icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title'}).text
        except:
            continue
        try:
            company=soup_req.find('div',{'class':'icl-u-lg-mr--sm icl-u-xs-mr--xs'}).text
        except:
            continue
        try:
            location=soup_req.find('div',{'class':'jobsearch-InlineCompanyRating icl-u-xs-mt--xs jobsearch-DesktopStickyContainer-companyrating'}).text
        except:
            location=city
        try:
            desc=soup_req.find('div',{'class':'jobsearch-jobDescriptionText'}).text
        except:
            continue
        df = df.append({"job_location":city, "job_title":title, "company":company, "job_description":desc},
                    ignore_index=True)
    
    return df
  
def get_job_postings(url_temp,position,city):
    
    href_list= get_href(url_temp,position,city)
    
    job_links= get_job_links(href_list)
    
    job_df= get_job_df(job_links,city)
    
    return job_df

data_scientist_df= get_job_postings(url_temp,position='Data+Scientist',city='Bengaluru')
data_scientist_df.head(10)