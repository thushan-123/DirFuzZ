

class UrlBuilder:
    
    def __init__(self, url: str):
        self.url: str = url
    
    def add_dir(self, dir_name: str):
        return f"{self.url}/{dir_name}"
    
    def add_more_dir(self, *dir_names):
        base_url: str = self.url
        base_path: str = ""
        
        for k in dir_names:
            base_path += f"/{k}"
        
        if base_url[-1] == "/":
            del base_url[-1]
            
        return base_url + base_path
    