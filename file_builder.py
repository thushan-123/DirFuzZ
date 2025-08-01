from url_builder import UrlBuilder

class fileUrlBuilder(UrlBuilder):
    def __init__(self,url: str, file_w_list: str, extension: str):
        super().__init__(url)
        self.file_w_list = file_w_list
        self.extension = extension
        
    def fileUrlPathBuilder(self,file_name: str):
        u: str = self.add_dir(self.file_w_list)
        u = u +"/"+ file_name + str(self.extension)
        return u
    
if __name__ == "__main__":
    furl = fileUrlBuilder("http://fb.com","hello",".html")
    print(furl.fileUrlPathBuilder("index"))
        
    