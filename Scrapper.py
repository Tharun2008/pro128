from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

START_URL = ("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
browser = requests.get(START_URL)
soup = BeautifulSoup(browser.text, "html.parser")
temp_list = []
for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    star.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df = pd.DataFrame(
    list(zip(star, distance, mass, radius)),
    columns=["Star", "Distance", "Mass", "Radius"],
)
df.to_csv("data.csv")