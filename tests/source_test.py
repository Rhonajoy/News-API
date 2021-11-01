 import unittest
class Source:
    """
     '''
    Source class to define Source Objects
    '''
    """
    def __init__(self,id,name,description,url,category):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category


# Source=source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('abc-news','ABC News','our trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com/','general')
         

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


