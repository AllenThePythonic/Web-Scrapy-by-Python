from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


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
    raise

if __name__ == '__main__':
    getNames()
