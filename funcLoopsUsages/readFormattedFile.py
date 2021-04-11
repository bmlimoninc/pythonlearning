
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('readwritefilesDir/readImage.jpg')

plt.imshow(img)


exit()
from PIL import Image
image = Image.open("readwritefilesDir/readImage.jpg")
image.show()


exit()
from bs4 import BeautifulSoup

# Opening the html file
HTMLFile = open("readwritefilesDir/readHTML.html", "r")

# Reading the file
index = HTMLFile.read()

# Creating a BeautifulSoup object and specifying the parser
Parse = BeautifulSoup(index, 'html.parser')

print(Parse.head)
print(Parse.body)
print(Parse.p)

exit()

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


with open("readwritefilesDir/readHTML.html", "r", encoding='utf-8') as f:
    text = f.read()

print(text)

parser = MyHTMLParser()
parser.feed(text)

exit()

import xml.etree.ElementTree as ET

tree = ET.parse('readwritefilesDir/readXML.xml')
root = tree.getroot()

print(root.tag)

for child in root:
    print("Tag:" + child.tag, "Data:" + child.text)

exit()
import csv

with open('readwritefilesDir/readCsvS.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print(f'Data: column1: {row[0]} - '
                  f'column2: {row[1]} - column3: {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

exit()

########EXCEL########
import pandas as pd

df = pd.read_excel('readwritefilesDir/readExcel.xlsx', sheet_name='SampleData', engine='openpyxl')
print(df)
