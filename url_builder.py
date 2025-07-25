
class UrlBuilder:
    
    def __init__(self, url: str):
        self.url: str = url
    
    def add_dir(self, dir_name: str):
        return f"{self.url}/{dir_name}"
    
    def add_more_dir(self, *dir_names):
        base_url: str = self.url.rstrip("/")
        base_path: str = "/".join(dir_names)
            
        return f"{base_url}/{base_path}"
    