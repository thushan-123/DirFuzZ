

class FileUrlBuilder:
    def __init__(self,url: str, extension: str):
        self.url = url
        self.extension = extension
        
    def fileUrlPathBuilder(self,file_name: str):
        url: str = self.url.rstrip("/")
        url = url +"/"+ file_name + str(self.extension)
        return url
    
# if __name__ == "__main__":
#     furl = fileUrlBuilder("http://fb.com","hello",".html")
#     print(furl.fileUrlPathBuilder("index"))
        
    