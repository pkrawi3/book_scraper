"""
Gets 200 Books and 50 Authors; Saves to JSON
"""
import scraper 
import time

bookList = []
startBook = 1
endBook   = 201
# Iterate through book numbers and extract information about each book
for pageNum in range(startBook, endBook):
    time.sleep(1)
    currentPage = scraper.get_page('book', pageNum)
    currentMap = scraper.parse_book_page(currentPage, pageNum)
    bookList.append(currentMap)
    #print(currentMap)

dataBase = scraper.create_database("200_books")
for i in bookList:
    scraper.map_to_database(dataBase, i)


authorList = []
startAuth = 20
endAuth   = 70
# Iterate through book numbers and extract information about each book
for pageNum in range(startAuth, endAuth):
    time.sleep(1)
    currentPage = scraper.get_page('author', pageNum)
    currentMap = scraper.parse_author_page(currentPage, pageNum)
    authorList.append(currentMap)
    #print(currentMap)

dataBase = scraper.create_database("50_authors")
for i in authorList:
    scraper.map_to_database(dataBase, i)
