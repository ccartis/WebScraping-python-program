import requests
from bs4 import BeautifulSoup


r=requests.get("http://pythonhow.com/example.html")
#grabe content from request datatype

c=r.content
l=type(c)
# print(c)
# print(l)
soup=BeautifulSoup(c,"html.parser")
print(soup.prettify())

all=soup.find_all("div",{"class":"cities"})
print(all)

all_too=soup.find_all("style")
print(all_too)
print("===================")
print("===================")
print("===================")
print("===================")
print("===================")
print("===================")

#what if I want only the h2 tags?

first_element_of_list=all[0].find_all("h2")
print(first_element_of_list)
print("----------------------------")
print("----------------------------")
print("----------------------------")
print("----------------------------")
print("----------------------------")
print("----------------------------")
london_only=all[0].find_all("h2")[0].text
print(london_only)

second_element_of_list=all[1].find_all("h2")
print(second_element_of_list)