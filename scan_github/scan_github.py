import requests
from bs4 import BeautifulSoup

keywords = ['angular', 'flask', 'django', 'react', 'node.js', 'mysql', 'sqlite', 'mongodb']
site = 'https://github.com/'
result = {}
max_term = 0
max_num = 0

## Web scrapping
for term in keywords:
    url = site + 'search?q=' + term
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for h in soup.find_all("h3"):
        arr = h.text.split()
        if 'repository' in arr:
            num = arr[0].replace(',','')
            if max_term < len(term): max_term = len(term)
            if max_num < len(num): max_num  = len(num)
            result[term] = int(num)
            # show initial search result
            print(f'Retriving term \'{term}\' : {arr[0]}')

## Sort dictionary 'result'
print()
print('Sorted result:')
tuples = sorted(result.items(), reverse=True, key = lambda kv:(kv[1], kv[0]))
for t in tuples:
    print(f'{t[0]:{max_term}} : {t[1]:{max_num}}')
