import requests     #allows us to grab html files
from bs4 import BeautifulSoup   # let us use html and grab different data
import pprint

url = 'https://news.ycombinator.com/news'    #url we want to grab data from
res = requests.get(url)
res2 = requests.get(url+'?p=2')
#print(res.text)

# For cleaning the text, to parse html output and convert it into something readable
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
#print(soup.body.contents)
#print(soup.find_all('div'))
#print(soup.find(id='score_20514750'))

# Accessing data using CSS selector
links = soup.select('.storylink')    #  .class_name
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')    #  .class_name
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = vote[0].getText().replace(' points', '')
            points = int(points.replace(' point', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))