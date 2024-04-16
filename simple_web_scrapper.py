#Import of libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd



#url to website
web_url='https://www.scrapethissite.com/pages/simple/'

#scrap content_function
def scrape_content(url):
    resp= requests.get(url)

    #parse the contents
    soup= BeautifulSoup(resp.text,'html.parser')

    #scrappe the contents
    country_name=[]
    country_capital=[]
    country_population=[]
    country_area=[]

    for content in soup.findAll("div",{'class':'col-md-4 country'}):
        country_name.append(content.find("h3",{'class':'country-name'}).text)
        country_capital.append(content.find("span",{"class":"country-capital"}).text)
        country_population.append(content.find("span",{"class":"country-population"}).text)
        country_area.append(content.find("span",{"class":"country-area"}).text)


    #writing to output file
    data=pd.DataFrame({'Country':country_name,'Capital':country_capital,'Population':country_population,'Area':country_area})


    #replace corrupted charecters
    data['Country']= data.Country.str.replace('\n','')
    return data


output = scrape_content(web_url)

print(output)




