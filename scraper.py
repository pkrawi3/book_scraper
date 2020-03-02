"""
Scrapes good reads web pages to retreive information associated with books and authors
"""
import json
import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB

"""
Gets good reads page associated with the supplied book or author
"""
def get_page(type, page_num):

    # USE 1: Book Page
    if type == 'book':
        url = 'https://www.goodreads.com/book/show/{}'.format(page_num)
        page = requests.get(url)
    # USE 2: Author Page
    elif type == 'author':
        url = 'https://www.goodreads.com/author/show/{}'.format(page_num)
        page = requests.get(url)
    return page

"""
Parses through the book page to get relevent information; returns it in the form of a map
"""
def parse_book_page(page, num):
    soup = BeautifulSoup(page.content, 'html.parser')
    page_map = {}
    try:
        page_map["book_url"] = soup.find('link')['href']
    except BaseException:
        print("No book url for {}".format(num))
    try:
        page_map["title"] = soup.find('title').text
    except BaseException:
        print("No title for {}".format(num))
    try:
        page_map["book_id"] = num
    except BaseException:
        print("No book id for {}".format(num))
    try:
        page_map["ISBN"] = soup.find('span', itemprop='isbn').text
    except BaseException:
        print("No ISBN for {}".format(num))
    try:
        page_map["author_url"] = soup.find('a', 'authorName')['href']
    except BaseException:
        print("No author url for {}".format(num))
    try:
        page_map["author"] = soup.find('a', 'authorName').text
    except BaseException:
        print("No author for {}".format(num))
    try:
        page_map["rating"] = soup.find('span', itemprop='ratingValue').text.strip()
    except BaseException:
        print("No rating for {}".format(num))
    try:
        page_map["rating_count"] = soup.find('meta', itemprop='ratingCount').text.strip()
    except BaseException:
        print("No rating count for {}".format(num))
    try:
        page_map["review_count"] = soup.find('meta', itemprop='reviewCount').text.strip()
    except BaseException:
        print("No review count for {}".format(num))
    try:
        page_map["image_url"] = soup.find('img', id='coverImage')['src']
    except BaseException:
        print("No image url for {}".format(num))
    try:
        page_map["similar_books"] = soup.find('a', 'actionLink right seeMoreLink')['href']
    except BaseException:
        print("No similar books for {}".format(num))
    return page_map

"""
Parses through the author page to get relevent information; returns it in the form of a map
"""
def parse_author_page(page, num):
    soup = BeautifulSoup(page.content, 'html.parser')
    page_map = {}
    try:
        page_map["name"] = soup.find("span", itemprop="name").text
    except BaseException:
        print("No author name for {}".format(num))
    try:
        page_map["author_url"] = soup.find("link")['href']
    except BaseException:
        print("No author url for {}".format(num))
    try:
        page_map["author_id"] = num
    except BaseException:
        print("No author id for {}".format(num))
    try:
        page_map["rating"] = soup.find('span', 'average').text
    except BaseException:
        print("No rating for {}".format(num))
    try:
        page_map["rating_count"] = soup.find('span', itemprop='ratingCount')['title']
    except BaseException:
        print("No rating count for {}".format(num))
    try:
        page_map["review_count"] = soup.find('span', itemprop='reviewCount')['title']
    except BaseException:
        print("No review count for {}".format(num))
    try:
        page_map["image_url"] = soup.find('img', itemprop='image')['src']
    except BaseException:
        print("No image url for {}".format(num))
    try:
        page_map["author_books"] = soup.find('a', 'actionLink')['href']
    except BaseException:
        print("No author books for {}".format(num))
    return page_map

"""
Converts Map object to JSON string
"""
def map_to_json(page_map):
    try:
        return json.JSONEncoder().encode(page_map)
    except BaseException:
        print("Failed to encode map")
        return ""

"""
Converts JSON string to Map
"""
def json_to_map(json_str):
    try:
        return json.JSONDecoder().decode(json_str)
    except BaseException:
        print("Failed to decode json string")
        return {}

"""
Creates the database
"""
def create_database(base_name):
    try:
        db = TinyDB('{}.json'.format(base_name))
    except BaseException:
        print("Failed to create database")
    return db

"""
Inserts mapTodatabase
"""
def map_to_database(database, new_map):
    try:
        database.insert(new_map)
    except BaseException:
        print("Failed to insert into database")
    return database

"""
Writes to a JSON File
"""
def write_to_json(filename, json_str):
    with open('{}.json'.format(filename), 'w') as json_file:
        json.dump(json_str, json_file)
    return

"""
Read from a JSON file
"""
def read_from_json(filename):
    try:
        file = open('{}.json'.format(filename))
        json_str = file.read()
    except BaseException:
        print("Couldn't read from json file")
        json_str = ""

    return json_str
