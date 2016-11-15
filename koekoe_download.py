#######################
# http://koe-koe.com/ #
#######################

import urllib2
import wget
import re
from bs4 import BeautifulSoup

def main():
    select = raw_input("page or all? > ")
    if select == "page":
        url = raw_input("url > ")
        try:
            html = urllib2.urlopen(url)
        except urllib2.HTTPError as e:
            if e.code == 404:
                return
        soup      = BeautifulSoup(html)
        href_list = soup.find_all(href=re.compile("detail"))
        file_list = []

        for i in range(len(href_list)):
            if i % 2 == 0:
                file_list.append(str(href_list[i])[22:27])

        print "total files is", len(file_list)
        for i in range(len(file_list)):
            url = 'http://file.koe-koe.com/sound/upload/' + file_list[i] + '.mp3'
            wget.download(url)
            print "\n", i+1, ": ", file_list[i], ".mp3 file download complete..."
    elif select == "all":
        url = raw_input("url(http://.....&p=) > ")
        print "now page:", i
        for i in range(1, 100):
            url = url + str(i)
            try:
                html = urllib2.urlopen(url)
            except urllib2.HTTPError as e:
                if e.code == 404:
                     return
            soup      = BeautifulSoup(html)
            href_list = soup.find_all(href=re.compile("detail"))
            file_list = []

            for i in range(len(href_list)):
                if i % 2 == 0:
                    file_list.append(str(href_list[i])[22:27])

            print "total files is", len(file_list)
            for i in range(len(file_list)):
                url = 'http://file.koe-koe.com/sound/upload/' + file_list[i] + '.mp3'
                wget.download(url)
                print "\n", i+1, ": ", file_list[i], ".mp3 file download complete..."

if __name__ == "__main__":
    main()
