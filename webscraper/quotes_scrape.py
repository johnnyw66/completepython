import requests
import bs4
import re
# toscrape.com

base_site_url = "http://quotes.toscrape.com"
quotes_tally = 0
authors = set()
quotes = set()

for page in range(1,11):
    url = f"{base_site_url}/page/{page}/"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "lxml")

    for quote in soup.select('.quote'):
        quotes_tally += 1
        text = quote.select('.text')[0].text
        author = quote.select('.author')[0].text
        authors.add(author)
        quotes.add(text)
        print(f"{author} : {text}")

print(f"Found {quotes_tally} quotes")

url = f"{base_site_url}"
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, "lxml")

#
search_keyword_tag='a'  # 'a' or 'tag'
for atag in soup.select(".col-md-4.tags-box")[0].select(search_keyword_tag):
    print("TOP KEY WORD",atag.text)


keywords = [atag.text for atag in soup.select(".col-md-4.tags-box")[0].select(search_keyword_tag)]
print(keywords)
print(authors)
print(quotes)

print(len(keywords))
print(len(authors))
print(len(quotes))
print("Quote Tally ", quotes_tally)
