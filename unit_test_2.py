import unittest
import requests
import scraper

class BasicTests(unittest.TestCase):

    # Requests a get of an author that should exist
    def test_basic_response(self):
        response = requests.get('http://127.0.0.1:5000/authors?name=Delia+Sherman')
        self.assertTrue(response.ok)

    # Rquests a get of a author that should not exist
    def test_basic_bad_response(self):
        response = requests.get('http://127.0.0.1:5000/authors?name=Fake+Author')
        self.assertFalse(response.ok)

    # Tests to see if the information retrieved is what expected
    def test_author_get(self):
        response = requests.get('http://127.0.0.1:5000/authors?name=Delia+Sherman')
        expected = scraper.map_to_json({"author_books":"/friend/user/932901","author_id":24,"author_url":"https://www.goodreads.com/author/show/24.Delia_Sherman","image_url":"https://images.gr-assets.com/authors/1391010737p5/24.jpg","name":"Delia Sherman","rating":"3.91","rating_count":"56366","review_count":"5157"})
        self.assertEqual(response.text, expected)

    # Tests to see if getting book is what is excpeted
    def test_book_get(self):
        response = requests.get('http://127.0.0.1:5000/books?title=A+Short+History+of+Nearly+Everything+by+Bill+Bryson')
        expected = scraper.map_to_json({"ISBN":"9780738837802","author":"Luther Butler","author_url":"https://www.goodreads.com/author/show/17.Luther_Butler","book_id":49,"book_url":"https://www.goodreads.com/book/show/49.Bucaneer","image_url":"https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1156871604l/49.jpg","rating":"3.80","rating_count":"5\n  ratings","review_count":"1\n    review","title":"Bucaneer by Luther Butler"})
        self.assertEqual(response.text, expected)

    # Tests to see if you can get book by author
    def test_author_get_book(self):
        response = requests.get('http://127.0.0.1:5000/books?author==Luther+Butler')
        expected = scraper.map_to_json({"ISBN":"9780738837802","author":"Luther Butler","author_url":"https://www.goodreads.com/author/show/17.Luther_Butler","book_id":49,"book_url":"https://www.goodreads.com/book/show/49.Bucaneer","image_url":"https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1156871604l/49.jpg","rating":"3.80","rating_count":"5\n  ratings","review_count":"1\n    review","title":"Bucaneer by Luther Butler"})
        self.assertEqual(response.text, expected)

    # Tests to see if ok response from deletion
    def test_book_delete_basic(self):
        response = requests.delete('http://127.0.0.1:5000/books?author=Luther+Butler')
        self.assertTrue(response.ok)

    # Tests to see if deletion of fake author fails
    def test_author_delete_fail(self):
        response = requests.delete('http://127.0.0.1:5000/books?author=Fake+Author')
        self.assertFalse(response.ok)

    # Tests to see if successfully deletes book
    def test_book_delete(self):
        response = requests.delete('http://127.0.0.1:5000/books?title=The+Lord+of+the+Rings+by+Brian+Sibley')
        response = requests.get('http://127.0.0.1:5000/books?title=The+Lord+of+the+Rings+by+Brian+Sibley')
        self.assertFalse(response.ok)

    # Tests to see if successfully deletes author
    def test_author_delete(self):
        response = requests.delete('http://127.0.0.1:5000/authors?name=Kate+Horsley')
        response = requests.get('http://127.0.0.1:5000/authors?name=Kate+Horsley')
        self.assertFalse(response.ok)

    # Tests to see if successfully updates criteria
    def test_book_update(self):
        response = requests.post('http://127.0.0.1:5000/books?title=The+Bucaneers+by+Edith+Wharton', data = {"review_count":"666"})
        self.assertTrue(response.ok)

    # Tests if fails to update a field that does not exist
    def test_book_update_bad(self):
        response = requests.post('http://127.0.0.1:5000/books?title=The+Bucaneers+by+Edith+Wharton', data = {"fake_count":"666"})
        self.assertFalse(response.ok)

if __name__ == '__main__':
    unittest.main()