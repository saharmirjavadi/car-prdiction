import re
import requests
import mysql.connector
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


load_dotenv('.env')

sentence = []
filter_list = []
final_list = []


def sanitize():
    for tag in cars:
        div = tag.find_all('div')
        for tag in div:
            sentence.append(re.sub(r'\s+', ' ', tag.text).strip())

    regex = r'(\d{4})،\sکارکرد\s(\d+,?\d+)'
    regex1 = r'^\w+\s?\w+?\s?\w+?\s?\w+?،\s(\w+\s?(\w+)?\s?(\w+)?)'
    regex2 = r'(\d+,\d+,\d+,?\d+)\sتومان'
    regex3 = r'(\w+)،(\w+)?(\s)?(\w+)?(\s)?(\w+)?(\s)?(\d+)?(\s)?(\w+)?(\s)?پیش(\s)'
    for Str in sentence:
        name = re.findall(regex1, Str)
        output = re.findall(regex, Str)
        price = re.findall(regex2, Str)
        place = re.findall(regex3, Str)
        for i in output:
            filter_list.append([price, output, place, name])


def append_to_list():
    for i in filter_list:
        if i[0] != [] and i[1] != [] and i[2] != [] and i[3] != []:
            if len(final_list) < 80:
                check_dub = (i[0][0], i[1][0], i[2][0][0], i[3][0][0])
                if check_dub not in final_list:
                    final_list.append(
                        tuple((i[0][0], i[1][0], i[2][0][0], i[3][0][0])))


car_brand = input('enter your car brand\nfor example :bmw : ')
print('please wait seconds ...')
n = 1
while (len(final_list) < 80):
    request = requests.get(os.getenv('SITE_URL')+car_brand)
    soup = BeautifulSoup(request.text, 'html.parser')
    cars = soup.find_all('div', attrs={'class': 'kt-post-card__body'})
    sanitize()
    append_to_list()
    n += 1


# connection to database
cnx = mysql.connector.connect(user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), host=os.getenv('DB_HOST'))
cursor = cnx.cursor()

# create database
database_name = input('enter database name : ')
cursor.execute('CREATE DATABASE IF NOT EXISTS %s' % (database_name))
cursor.execute('USE %s' % (database_name))
cursor.execute('CREATE TABLE IF NOT EXISTS cars (name VARCHAR(255),place VARCHAR(255), output VARCHAR(255), year VARCHAR(255) ,price VARCHAR(255))')
cursor.execute('DELETE FROM cars')

with open('database_name.txt','w') as f:
    f.write(database_name)
    
for i in final_list:
    name = i[3].strip()
    place = i[2]
    output = i[1][1]
    year = i[1][0]
    price = i[0]
    cursor.execute('insert into cars VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' % (name, place, output, year, price))
    cnx.commit()


cursor.close()
cnx.close()

