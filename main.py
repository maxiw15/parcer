from bs4 import BeautifulSoup
import requests
from datetime import datetime
import csv
import time as spleepy

with open('result.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    writer.writerow([datetime.now()])
    counter = 0
    while counter != 20:
        url_openphish = 'https://openphish.com/'

        page = requests.get(url_openphish, stream=True, allow_redirects=True, timeout=10, verify=False)
        soup = BeautifulSoup(page.text, "html.parser")
        table = soup.find('table', class_ = 'pure-table pure-table-striped')
        internal_table = table.find('tbody')


        alive_sites = []
        now = datetime.now()
        current_time = now.strftime("%m/%d/%Y %H:%M:%S")
        date = current_time.split(" ")[0]
        for tr in internal_table.find_all('tr'):
            url = ""
            target = ""
            time = ""
            row = []
            for td in tr.find_all('td'):
                # print(td.text.strip())
                row.append(td.text.strip())
            url = row[0]
            target = row[1]
            time = row[2]
            if url not in alive_sites:
                alive_sites.append({url:{"URL":url, "Компания":target, "Время":time}})
                writer.writerow([url, target, time])
        print(counter, "Перерыв")
        spleepy.sleep(180)

        counter += 1

    writer.writerow([datetime.now()])




import csv
import pandas as pd


arr = np.array(temp)
temp = []
with open('result.csv') as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        temp.append(row[0].split(','))


new_df = df.drop_duplicates()
new_df.value_counts()
most_common = new_df[1].value_counts()
len(new_df[0].unique())