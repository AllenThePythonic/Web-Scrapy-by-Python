from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import random
import datetime


def getNames():

    try:

        html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

        #  Check html is available
        if html is None:
            print("URL is not found")

        else:
            # Initialise the BeautifulSoup

            bsObj = BeautifulSoup(html.read(), "html.parser")

            # Find bad content  : where nonExistentTag is a made-up tag, not the
            # name of a real BeautifulSoup function :
            # bsObj.findAll(tagName, tagAttributes)

            try:
                # bsObj.tag.subTag.anotherSubTag

                content = bsObj.findAll("span", {"class": "green"})

            except AttributeError as e:
                print("Tag was not found : " + e)

            else:
                if content is None:
                    print("Tag was not found")
                else:
                    #  Get All names excepts "the prince" and "The prince"
                    resultList = list(
                        filter(lambda x: x.get_text() not in "the prince"
                               and x.get_text() not in "The prince", content))
                    print([name.get_text() for name in resultList])

                    # get Total no. of "the prince "
                    princeList = bsObj.findAll("", {"id": "text"})

                    print(
                        "\nGet total of the prince : " + str(len(princeList)))

                    allText = bsObj.findAll(id="text")
                    print("n" + allText[0].get_text())

    except HTTPError as e:
        print(e)


def getTableElement():

    # Initialise the BeautifulSoup

    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html, "html.parser")

    # Scan the table by cursor -> bsObj.find("table", {"id":
    # "giftList"}).tr.next_siblings

    for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
        print(sibling)

    print("Select the specified item and price ")

    # 1. The image tag where src="../img/gifts/img2.jpg" is first selected
    # 2. We select the parent of that tag (in this case, the <td> tag).
    # 3. We select the previous_sibling of the <td> tag (in this case,
    #    the <td> tag that
    # contains the dollar value of the product).
    # 4. We select the text within that tag, “$10,000.52”

    print(bsObj.find("img", {"src": "../img/gifts/img2.jpg"}) .parent.previous_sibling.previous_sibling.previous_sibling.get_text()
          + "Price :  "
          + bsObj.find("img", {"src": "../img/gifts/img2.jpg"}).parent.previous_sibling.get_text())


def getContentByRegularExpression():

    # Initialise the BeautifulSoup

    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html, "html.parser")

    # == myImgTag.attrs['src']
    images = bsObj.findAll(
        "img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
    for image in images:
        print(image["src"])


def getAllAttributesByLambdaExp():
     # Initialise the BeautifulSoup

    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html, "html.parser")

    # Get all attrs from all tag
    print(bsObj.findAll(lambda tag: print(tag.attrs)))


def traverSingleDomain():
    # Initialise the BeautifulSoup
    html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
    bsObj = BeautifulSoup(html, "html.parser")

    # Find all a-href on entire page
    # for link in bsObj.findAll("a"):
    #     if 'href' in link.attrs:
    #         print(link.attrs['href'])

    for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])


def traverSingleDomain2():
    random.seed(datetime.datetime.now())
    links = getLinks("/wiki/Kevin_Bacon")
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


if __name__ == '__main__':
    # getNames()
    # getTableElement()
    # getContentByRegularExpression()
    # getAllAttributesByLambdaExp()

    # traverSingleDomain()
    traverSingleDomain2()
