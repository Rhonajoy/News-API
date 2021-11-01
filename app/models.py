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
        
class Article:
    """
     '''
    Article  class to define Article Objects
    '''
    """
    def __init__(self,id,name,author,url,title,urlToImage,content):
        self.id =id
        self.name = name
        self.author = author
        self.url = url
        self.title = title
        self.urlToImage=urlToImage
        self.content= content
       