#Portfolio Project - Web Scraping Largest Companies by Revenue
#Skills Used: Web Scraping with BeautifulSoup, importing data into Pandas

from bs4 import BeautifulSoup
import requests

URL = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html')

print(soup)

table = soup.find_all('table')[1]
print(table)

public_titles = table.find_all('th')

public_table_titles = [title.text.strip() for title in public_titles]
print(public_table_titles)

# # Importing into Pandas Dataframe
import pandas as pd

df = pd.DataFrame(columns = public_table_titles)
df

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)
    length = len(df)
    df.loc[length] = individual_row_data
df

#Import to CSV for further analysis
df.to_csv(r'C:\Users\KayleighMacdonald\Documents\Largest_Companies.csv', index = False)
