# Grab a Book with at least 2 Star Rating
import requests
import bs4
import re
# toscrape.com

main_book_site_url = "http://books.toscrape.com"
minimum_required_rating = 0
found = 0
products_tally = 0
rating_errors = 0
for num in range(1,51):
    url = f"{main_book_site_url}/catalogue/page-{num}.html"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "lxml")

    for product in soup.select('.product_pod'):
        products_tally += 1
        book = product.select('h3')[0].select('a')[0]
        title = book['title']
        href = book['href']
        star_rating = product.select('.star-rating')[0]
        text_star_rating = star_rating['class'][1].capitalize()
        #print(f"STAR RATING ===> '{text_star_rating}'")
        try:
            rating = ['None','One','Two','Three','Four','Five','Six'].index(text_star_rating)
            if (rating >= minimum_required_rating):
                print(f"'{title}' **Star Rating** {text_star_rating}" )
                found += 1

        except Exception as e:
            print(f"ERROR **** {e} ****")
            rating_errors +=1


print(f"Found {found} books with our required minimum rating of {minimum_required_rating} (out of a total of {products_tally} books)")
print(f"Rating Errors {rating_errors}")
