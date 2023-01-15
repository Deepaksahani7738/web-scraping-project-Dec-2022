import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.themoviedb.org/movie"
response=requests.get(url).text
soup_data=BeautifulSoup(response,"lxml")
first_data=soup_data.find("div",attrs={"class":"card style_1"})
link_data=first_data.find("h2")
data=link_data.find("a").get("href")
data=data.replace("/movie","")
url=url+data
html_code=requests.get(url).text
html = BeautifulSoup(html_code,'lxml')
Name=html.find("h2").text.strip().replace("\n","")
score_data=html.find("div",attrs={"class":"user_score_chart"})
Rating=score_data["data-percent"]
genre=html.find("span",attrs={"class":"genres"}).text.strip().replace("\xa0","")
Realease_date=html.find("span",attrs={"class":"release"}).text.strip().replace("(IN)","")
Runtime=html.find("span",attrs={"class":"runtime"}).text.strip()
movies_director=html.find("li",attrs={"class":"profile"})
director=movies_director.find("p").text

movie_info = {"Name":Name,"Rating":Rating,"Genre":genre,"Release Date":Realease_date,"Runtime":Runtime,"Director":director,"url":url}
print(movie_info)


url_lst=[]
base_url="https://www.themoviedb.org/movie/?page="  
for item in range(1,51):
    url_lst.append(base_url+str(item))
    
    
for i in url_lst:
    print(i)



url="https://www.themoviedb.org/movie"
all_movies_list=[]
for url_name in url_lst:
    html_data = requests.get(url_name).text
    soup_data = BeautifulSoup(html_data,"lxml")
    all_divs=soup_data.find_all("div",attrs={"class":"card style_1"})
    for item in all_divs:
        url="https://www.themoviedb.org/movie"
        response=requests.get(url).text
        first_data=item.find("div",attrs={"class":"card style_1"})
        soup_data=BeautifulSoup(response,"lxml")
        link_data=item.find("h2")
        first_data=soup_data.find("div",attrs={"class":"card style_1"})
        data=link_data.find("a").get("href")
        data=data.replace("/movie","")
        url=url+data
        html_code=requests.get(url).text
        html = BeautifulSoup(html_code,"lxml")
        Name=item.find("h2").text.strip().replace("\n","")
        score_data=item.find("div",attrs={"class":"user_score_chart"})
        Rating=score_data["data-percent"]
        Realease_date=html.find("span",attrs={"class":"release"}).text.strip().replace("(IN)","")
        genre=html.find("span",attrs={"class":"genres"}).text.strip().replace("\xa0","")
        try:
            Runtime=html.find("span",attrs={"class":"runtime"}).text.strip()
        except Exception as e:
            Runtime=None
        try:
            movies_director=html.find("li",attrs={"class":"profile"})
            director=movies_director.find("p").text
        except Exception as d:
            director=None
       
        data ={
        "Name":Name,
        "Rating":Rating,
        "Genre":genre,
        "Release Date":Realease_date,
        "Runtime":Runtime,
        "Director":director,
        "url":url}
        all_movies_list.append(data)
    print(all_movies_list)

data=pd.DataFrame(all_movies_list)
data.to_csv("web_scraping_project.csv",index=False)















    