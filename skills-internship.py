# i am using internshala

from bs4 import BeautifulSoup
import pandas as pd
import requests

job_title,company_name,location,start_date,duration,stipends,apply_by,posted_on=[],[],[],[],[],[],[],[]
# print(posted_on)
skill=input('enter the skill:- ')

html_text=requests.get("https://internshala.com/internships/keywords-{}".format(skill)).text
# print(html_text) 
soup=BeautifulSoup(html_text,'lxml')
posts=soup.find_all(class_="internship_meta")
# print(posts)
for post in posts:
    job_title.append(post.find('a',class_="view_detail_button").text.strip())
    company_name.append(post.find('a',class_='link_display_like_text view_detail_button').text.strip())
    location.append(post.find('a',class_='location_link view_detail_button').text.strip())
    start_date.append(post.find('span',class_="start_immediately_mobile").text.replace('\xa0',' ').strip())
    # duration.append(post.find('div',class_='item_body').text.strip())
    print(post.find('div',class_='other_detail_item large_stipend_text'))
# print(duration)