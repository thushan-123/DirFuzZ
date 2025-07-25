from ..url_builder import UrlBuilder


# def test_add_dir():
#     builder = UrlBuilder("http://example.com")
#     assert builder.add_dir("test") == "http://example.com/test"

""" 
    TEST CASE 1:
        url : http://orange.com
        dir name : voldemort
        expected result : http://orange.com/voldemort
"""
def test_add_dir():
    builder = UrlBuilder("http://orange.com")
    assert builder.add_dir("voldemort") == "http://orange.com/voldemort"
    
    
""" 
    TEST CASE 2:
        url : http://orange.com/
        dir name : voldemort
        expected result : http://orange.com/voldemort
"""
def test_url_slash():
    builder = UrlBuilder("http://orange.com/")
    assert UrlBuilder.add_dir("voldemort") == "http://orange.com/voldemort"

