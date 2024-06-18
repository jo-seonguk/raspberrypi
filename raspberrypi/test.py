import requests
from bs4 import BeautifulSoup
import pands as pd

res = requests.get('https://www.devicemart.co.kr/goods/catalog?code=00110001')

if response.status_code == 200:
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    data1 = soup.select('')

title = []
url = []
for s in soup:
    title.append(s.text)
    url.append(n['href'])

df = pd.DataFrame()
df['제목'] = title
df['URL'] = url

df.to_excel('test.xlsx', index = False)
