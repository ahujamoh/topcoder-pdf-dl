__author__ = 'mohit'

from bs4 import BeautifulSoup

import urllib2
import pdfkit
import os

class topCoderScrapper:

    def __init__(self):
        
        self.alumni_page=urllib2.urlopen("http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=alg_index")
        self.alumni_data=BeautifulSoup(self.alumni_page.read())


    def convertPage(self):
        base_url = "http://community.topcoder.com"
        orig_tds = self.alumni_data.findAll("td")
        new_tds = []
        for stri in orig_tds:
            if str(stri).startswith('<td><a href="https://www.topcoder.com/community/data-science/data-science-tutorials/'):
                new_tds.append(stri)
        #for data in self.alumni_data.findAll("td",{'class':'bodyText', 'nowrap':'nowrap'}):
        for data in new_tds: 
            for url in data.findAll("a"):
                name = url.get_text()
                tmp = url['href']
                file_name = tmp.split('tutorials')[1][1:-1]
                final_url = tmp
                print "Downloading " + file_name +"...."

                os.system("wkhtmltopdf '"+final_url+"' "+file_name+".pdf")
