from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self,base_url,page_url):
        super().__init__()
        self.base_url=base_url
        self.page_url=page_url
        self.links=set()

    def handle_starttag(self,tag,attrs):
        print("tag name : ",tag)
        for(attribute,value) in attrs:
            print("Attri nm : ",attribute," value : ",value)    

    def error(self,message):
        pass

finder=LinkFinder('E:/B.E/project material/project_files','index.html')
finder.feed("index")
    
