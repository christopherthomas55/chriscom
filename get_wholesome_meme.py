from bs4 import BeautifulSoup
import urllib


def get_wholesome_meme():
    page = urllib.urlopen('https://www.reddit.com/r/wholesomememes/').read()
    soup = BeautifulSoup(page, "html.parser")
    link = soup.body.find('div', {'data-rank':'1'}).a['href']
    with open('../static/misc/meme_url.txt', 'w+') as f:
        f.write(link)

if __name__ =="__main__":
    get_wholesome_meme()
