import unittest
from app.models import Article


# Article=article.Article

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('abc-news','ABC News','our trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com/','general')
        #  ','CNN','skjsdjfkd.jpg','killer cat','killer','www.cnn.com','12/12/15','name

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()