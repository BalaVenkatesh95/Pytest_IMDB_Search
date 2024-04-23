"""
 Test case file with all required test cases to execute
"""
from imdbsearch_functions import ImdbClass
import pytest

url = "https://www.imdb.com/search/name/"
#Creating Instance of SauceDemoClass to utilise its methods / functions
imdb = ImdbClass(url)

# Test to extract text
def test_name_search():
    imdb.name_search()

#Test Case to quit / shutdown browser
def test_shutdown():
   imdb.shutdown()
