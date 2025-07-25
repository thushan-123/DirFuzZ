from ..url_builder import UrlBuilder


# def test_add_dir():
#     builder = UrlBuilder("http://example.com")
#     assert builder.add_dir("test") == "http://example.com/test"

def test_add_dir():
    builder = UrlBuilder("http://orange.com")
    assert builder.add_dir("voldemort") == "http://orange.com/voldemort"
    
    

