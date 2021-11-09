import unittest
# from app.models import Article


class Article:
    """
     '''
    Article  class to define Article Objects
    '''
    """
    def __init__(self,id,name,author,url,title,urlToImage,content,publishedAt):
        self.id =id
        self.name = name
        self.author = author
        self.url = url
        self.title = title
        self.urlToImage=urlToImage
        self.content= content
        self.publishedAt=publishedAt

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('cnn-news','name','killer','www.cnn.com',"killer cat","https.tyyyyyy.com"," trusted source for breaking news, analysis, ","12/12/15")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


# if __name__ == '__main__':
#     unittest.main()