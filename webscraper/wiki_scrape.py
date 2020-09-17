import requests
import bs4
import re
#res = requests.get("http://www.wikipedia.com")
res = requests.get("http://www.example.com")

print(type(res))
print(res)
print(res.text)
#print(res.title)

soup = bs4.BeautifulSoup(res.text, "lxml")
print("BS4",soup)

print(soup.select("Title"))
print(soup.select("titLe"))
print(soup.select("title"))
print(soup.select("TITLE"))
print(soup.select("title")[0].getText())


print(soup.select("p"))

print("Extracting paragraphs")
for para in soup.select("p"):
    print(f"**>{para.getText()}")


for m in soup.select("meta"):
    if (m.get('charset')):
        print("Meta Charset Attribute '%s'" % m.get('charset'))

"""
soup.select('div') #Grab tag
soup.select('#some_id') #Grab element with a given id 'some_id'
soup.select('.some_class') #Grab class
soup.select('div span') #Any elements named span within a div element
soup.select('div > span') #Any elements named span DIRECTLY within a div element and nothing in between

"""


# Example code to grab elements with a particular class ID '.toctext'
class_id = '.toctext'
res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(res.text, "lxml")
print("\n\nGrace Hooper Content--->\n")
for tag in soup.select(class_id):
    print(f"\t{tag.getText()}  Alternative {tag.text}")

#help(tag)

# Grabbing an image
#//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png

deepblue_url = "https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)"
res = requests.get(deepblue_url)
soup = bs4.BeautifulSoup(res.text, "lxml")
cnt = 0
for imgtag in soup.select('.thumbimage'):
#for imgtag in soup.select('img'):
    # Retrieve attributes by using get or dict type lookup
    #print(imgtag.get('src'), imgtag['src'])
    image_src_attr = imgtag['src']
    imgurl = 'https:' + image_src_attr

    # Grab last bit from src attrubute and use this as our local source name
    mainasset_name = re.search('[\w-]+\.\w+$', image_src_attr)[0]

    image = requests.get(imgurl)
    #print(image.content)
    with open(f'{mainasset_name}', 'wb') as fd:
        fd.write(image.content)
    cnt = cnt + 1
