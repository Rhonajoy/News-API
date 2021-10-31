from werkzeug.datastructures import ContentRange


class Article:
    """
     '''
    Source class to define Source Objects
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
       