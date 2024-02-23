import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.tutorialsfreak.com/") # response store into web var

soup = BeautifulSoup(web.content, "html.parser")

# print(soup.prettify()) # make html tree 

# print(soup.title) # get title

# print(soup.a) # get first anker tag

# print(soup.p) # get first p tag

p = soup.find("p") # finding first p from soup object
print(p.string) # getting sting from p 
print(type(p))

p = soup.find_all("p") # finding first all p from soup object from the url
print(len(p)) # getting len of p 
print(type(p))
