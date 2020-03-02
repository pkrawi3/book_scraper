import scraper
import time

# Scrape 5 Books
"""
Main function - currently for testing
"""
def main():

    """
    Test 1: Book Page Scraping
    """
    # URL indices
    startBook = 1
    endBook   = 2

    # Iterate through book numbers and extract information about each book
    for pageNum in range(startBook, endBook):
        time.sleep(1)
        currentPage = scraper.get_page('book', pageNum)
        currentMap = scraper.parse_book_page(currentPage, pageNum)
        print(currentMap)

    """
    Test 2: Author Page Scraping
    """
    # URL indices
    startAuth = 20
    endAuth   = 25

    # Iterate through book numbers and extract information about each book
    totalMap = []
    for pageNum in range(startAuth, endAuth):
        time.sleep(1)
        currentPage = scraper.get_page('author', pageNum)
        currentMap = scraper.parse_author_page(currentPage, pageNum)
        totalMap.append(currentMap)
        print(currentMap)

    """
    Test 3: Converting page Map to JSON
    """
    jsonString = scraper.map_to_json(totalMap)
    print("JSON String:")
    print(jsonString)

    """
    Test 4: Converting JSON String to Map
    """
    resultMap = scraper.json_to_map(jsonString)
    print("Map from JSON:")
    print(resultMap)

    """
    Test 5: Create and append all instances to database
    """
    dataBase = scraper.create_database("unit_test")
    for i in totalMap:
        scraper.map_to_database(dataBase, i)

    print("Database:")
    for item in dataBase:
        print(item)

    """
    Test 6: Book Page Scraping 2
    """
    # URL indices
    startBook = 1000
    endBook   = 1002

    # Iterate through book numbers and extract information about each book
    for pageNum in range(startBook, endBook):
        time.sleep(1)
        currentPage = scraper.get_page('book', pageNum)
        currentMap = scraper.parse_book_page(currentPage, pageNum)
        print(currentMap)
    
    """
    Test 7: Book Page Scraping 2
    """
    # URL indices
    startBook = 88
    endBook   = 91

    # Iterate through book numbers and extract information about each book
    for pageNum in range(startBook, endBook):
        time.sleep(1)
        currentPage = scraper.get_page('book', pageNum)
        currentMap = scraper.parse_book_page(currentPage, pageNum)
        print(currentMap)

    """
    Test 8: Book Page Scraping 2
    """
    # URL indices
    startAuth = 1000
    endAuth   = 1002

    # Iterate through book numbers and extract information about each book
    totalMap = []
    for pageNum in range(startAuth, endAuth):
        time.sleep(1)
        currentPage = scraper.get_page('author', pageNum)
        currentMap = scraper.parse_author_page(currentPage, pageNum)
        totalMap.append(currentMap)
        print(currentMap)

    """
    Test 9: Writing to JSON
    """
    scraper.write_to_json("unittest", jsonString)


    """
    Test 10: Reading from JSON
    """
    scraper.read_from_json("unittest")

main()
