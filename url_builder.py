
class UrlBuilder:
    
    def __init__(self, url: str):
        self.url: str = url
    
    def add_dir(self, dir_name: str):
        base_url: str = self.url.rstrip("/")
        return base_url +"/" +dir_name
    
    def add_more_dir(self, *dir_names):
        base_url: str = self.url.rstrip("/")
        base_path: str = ""
        for x in dir_names:
            base_path += f"/{x}"
        
            
        return  base_url + base_path
    
    
if __name__ == "__main__":
    builder = UrlBuilder("http://fb.com")
    print(builder.add_more_dir("abc","fda"))